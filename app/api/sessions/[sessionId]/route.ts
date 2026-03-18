import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";

export async function GET(
  _req: NextRequest,
  { params }: { params: { sessionId: string } }
) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const chatSession = await prisma.chatSession.findUnique({
    where: { id: params.sessionId },
    include: {
      messages: { orderBy: { createdAt: "asc" } },
    },
  });

  if (!chatSession || chatSession.userId !== session.user.id) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  return NextResponse.json(chatSession);
}

export async function DELETE(
  _req: NextRequest,
  { params }: { params: { sessionId: string } }
) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const chatSession = await prisma.chatSession.findUnique({
    where: { id: params.sessionId },
  });

  if (!chatSession) {
    return NextResponse.json({ error: "Not found" }, { status: 404 });
  }

  if (chatSession.userId !== session.user.id) {
    return NextResponse.json({ error: "Forbidden" }, { status: 403 });
  }

  await prisma.chatSession.delete({ where: { id: params.sessionId } });

  return NextResponse.json({ ok: true });
}
