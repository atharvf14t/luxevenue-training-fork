import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { detectLanguage } from "@/lib/language-detect";
import { buildSystemPrompt } from "@/lib/knowledge-base";
import { handleToolCall, TOOL_DEFINITIONS } from "@/lib/tools";
import { createAzureClient } from "@/lib/azure-openai";
import OpenAI from "openai";

export const maxDuration = 60;

export async function POST(req: NextRequest) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { sessionId, message } = (await req.json()) as {
    sessionId: string;
    message: string;
  };

  if (!sessionId || !message?.trim()) {
    return NextResponse.json({ error: "Missing fields" }, { status: 400 });
  }

  // Verify session belongs to user
  const chatSession = await prisma.chatSession.findUnique({
    where: { id: sessionId },
    include: { messages: { orderBy: { createdAt: "asc" } } },
  });

  if (!chatSession || chatSession.userId !== session.user.id) {
    return NextResponse.json({ error: "Session not found" }, { status: 404 });
  }

  const language = detectLanguage(message);
  const userName = session.user.name?.split(" ")[0] ?? "there";
  const dbUser = await prisma.user.findUnique({
    where: { id: session.user.id },
    select: { gender: true },
  });
  const userGender = dbUser?.gender ?? "unknown";
  const systemPrompt = buildSystemPrompt(userName, language, userGender);

  // Save user message
  await prisma.message.create({
    data: { sessionId, role: "user", content: message, language },
  });

  await prisma.chatSession.update({
    where: { id: sessionId },
    data: { updatedAt: new Date() },
  });

  // Build message history (excluding the message we just added — we add it fresh below)
  const history: OpenAI.ChatCompletionMessageParam[] = chatSession.messages.map(
    (m) => ({ role: m.role as "user" | "assistant", content: m.content })
  );
  history.push({ role: "user", content: message });

  const client = createAzureClient();

  // Tool call loop (non-streaming iterations)
  const extraMessages: OpenAI.ChatCompletionMessageParam[] = [];
  const MAX_TOOL_ITERATIONS = 3;

  for (let i = 0; i < MAX_TOOL_ITERATIONS; i++) {
    const allMessages: OpenAI.ChatCompletionMessageParam[] = [
      { role: "system", content: systemPrompt },
      ...history,
      ...extraMessages,
    ];

    const response = await client.chat.completions.create({
      model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-4o-2024-08-06",
      messages: allMessages,
      tools: TOOL_DEFINITIONS,
      tool_choice: "auto",
      stream: false,
    });

    const choice = response.choices[0];

    if (
      choice.finish_reason !== "tool_calls" ||
      !choice.message.tool_calls?.length
    ) {
      break; // No tool calls needed — proceed to streaming final response
    }

    // Add assistant message (with tool_calls) to context
    extraMessages.push(choice.message as OpenAI.ChatCompletionMessageParam);

    // Execute each tool and add results
    for (const toolCall of choice.message.tool_calls) {
      // eslint-disable-next-line @typescript-eslint/no-explicit-any
      const tc = toolCall as any;
      const fnName: string = tc.function?.name ?? tc.name ?? "";
      const fnArgs: string = tc.function?.arguments ?? tc.arguments ?? "{}";
      const args = JSON.parse(fnArgs) as Record<string, unknown>;
      const result = await handleToolCall(fnName, args);

      extraMessages.push({
        role: "tool",
        content: result,
        tool_call_id: toolCall.id,
      } as OpenAI.ChatCompletionMessageParam);
    }
  }

  // Stream final response
  const finalMessages: OpenAI.ChatCompletionMessageParam[] = [
    { role: "system", content: systemPrompt },
    ...history,
    ...extraMessages,
  ];

  const stream = await client.chat.completions.create({
    model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-4o-2024-08-06",
    messages: finalMessages,
    stream: true,
  });

  let fullContent = "";

  const readable = new ReadableStream({
    async start(controller) {
      const encoder = new TextEncoder();
      try {
        for await (const chunk of stream) {
          const delta = chunk.choices[0]?.delta?.content ?? "";
          if (delta) {
            fullContent += delta;
            controller.enqueue(encoder.encode(delta));
          }
        }
      } finally {
        controller.close();
        // Save assistant message after stream finishes
        if (fullContent) {
          prisma.message
            .create({
              data: {
                sessionId,
                role: "assistant",
                content: fullContent,
                language,
              },
            })
            .catch(() => {});
        }
      }
    },
  });

  return new Response(readable, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "X-Content-Type-Options": "nosniff",
    },
  });
}
