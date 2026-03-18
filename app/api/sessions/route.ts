import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";

export async function GET() {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const sessions = await prisma.chatSession.findMany({
    where: { userId: session.user.id },
    orderBy: { updatedAt: "desc" },
    take: 5,
    select: { id: true, title: true, createdAt: true, updatedAt: true },
  });

  return NextResponse.json(sessions);
}

export async function POST() {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const count = await prisma.chatSession.count({
    where: { userId: session.user.id },
  });

  if (count >= 5) {
    return NextResponse.json(
      { error: "SESSION_LIMIT_REACHED" },
      { status: 403 }
    );
  }

  const chatSession = await prisma.chatSession.create({
    data: {
      userId: session.user.id,
      title: "New Conversation",
    },
  });

  return NextResponse.json(chatSession);
}
