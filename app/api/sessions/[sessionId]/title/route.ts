import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { createAzureClient } from "@/lib/azure-openai";

export async function POST(
  req: NextRequest,
  { params }: { params: { sessionId: string } }
) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { message } = await req.json() as { message: string };

  // Verify session belongs to user
  const chatSession = await prisma.chatSession.findUnique({
    where: { id: params.sessionId },
  });

  if (!chatSession || chatSession.userId !== session.user.id) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  try {
    const client = createAzureClient();
    const completion = await client.chat.completions.create({
      model: process.env.AZURE_OPENAI_DEPLOYMENT ?? "gpt-4o-2024-08-06",
      messages: [
        {
          role: "user",
          content: `Generate a 4–6 word title for a conversation that starts with: "${message}". Return only the title, no quotes, no punctuation at end.`,
        },
      ],
      max_tokens: 20,
      temperature: 0.7,
    });

    const title =
      completion.choices[0]?.message?.content?.trim() ?? "New Conversation";

    await prisma.chatSession.update({
      where: { id: params.sessionId },
      data: { title },
    });

    return NextResponse.json({ title });
  } catch {
    // Title generation failure is non-critical
    return NextResponse.json({ ok: true });
  }
}
