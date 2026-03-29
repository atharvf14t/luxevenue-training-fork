import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { detectLanguage } from "@/lib/language-detect";

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

  // Save user message
  await prisma.message.create({
    data: { sessionId, role: "user", content: message, language },
  });

  await prisma.chatSession.update({
    where: { id: sessionId },
    data: { updatedAt: new Date() },
  });

  // ── Forward to Python multi-agent service ──────────────────────────────────
  const pythonAgentUrl = process.env.PYTHON_AGENT_URL ?? "http://localhost:8000";
  const internalKey = process.env.INTERNAL_API_KEY ?? "";

  let pythonResponse: Response;
  try {
    pythonResponse = await fetch(`${pythonAgentUrl}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "x-internal-key": internalKey,
      },
      body: JSON.stringify({
        session_id: sessionId,
        message,
        user_id: session.user.id,
        user_name: userName,
        user_gender: userGender,
        language,
      }),
    });
  } catch (err) {
    console.error("[chat/route] Python agent unreachable:", err);
    return NextResponse.json(
      { error: "AI service temporarily unavailable. Please try again shortly." },
      { status: 503 }
    );
  }

  if (!pythonResponse.ok) {
    return NextResponse.json(
      { error: "AI service returned an error." },
      { status: 502 }
    );
  }

  // Stream the Python response body to the browser while capturing the full content
  let fullContent = "";

  const readable = new ReadableStream({
    async start(controller) {
      const encoder = new TextEncoder();
      const reader = pythonResponse.body?.getReader();
      if (!reader) {
        controller.close();
        return;
      }
      const decoder = new TextDecoder();
      try {
        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const text = decoder.decode(value, { stream: true });
          fullContent += text;
          controller.enqueue(encoder.encode(text));
        }
      } finally {
        controller.close();
        reader.releaseLock();
        // Save assistant message after stream finishes
        if (fullContent) {
          prisma.message
            .create({
              data: { sessionId, role: "assistant", content: fullContent, language },
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
