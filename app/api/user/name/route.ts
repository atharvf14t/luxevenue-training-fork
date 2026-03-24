import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";

export async function POST(req: NextRequest) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { name } = await req.json() as { name: string };
  if (!name?.trim()) {
    return NextResponse.json({ error: "Name is required" }, { status: 400 });
  }

  const firstName = name.trim().split(" ")[0];
  let gender = "unknown";
  try {
    const gRes = await fetch(`https://api.genderize.io/?name=${encodeURIComponent(firstName)}`);
    if (gRes.ok) {
      const gData = await gRes.json() as { gender: string | null };
      if (gData.gender) gender = gData.gender;
    }
  } catch { /* silently fall back to "unknown" */ }

  await prisma.user.update({
    where: { id: session.user.id },
    data: { name: name.trim(), gender },
  });

  return NextResponse.json({ ok: true });
}
