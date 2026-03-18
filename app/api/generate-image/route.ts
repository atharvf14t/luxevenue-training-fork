import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import { prisma } from "@/lib/prisma";
import { checkImageQuota } from "@/lib/image-quota";
import OpenAI from "openai";
import sharp from "sharp";
import path from "path";
import fs from "fs";

export const maxDuration = 60;

export async function POST(req: NextRequest) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const userId = session.user.id;

  // Server-side quota check
  const quota = await checkImageQuota(userId);
  if (!quota.allowed) {
    const message =
      quota.reason === "not_enabled"
        ? "Image generation is not enabled for your account. Contact LuxeVenue to unlock this feature."
        : "You have used all your image credits. Contact LuxeVenue to get more.";

    return NextResponse.json(
      { error: quota.reason, message },
      { status: 403 }
    );
  }

  const { area, theme, event, style, prompt } = (await req.json()) as {
    area: string;
    theme: string;
    event: string;
    style?: string;
    prompt?: string;
  };

  // Build a descriptive prompt for decor image generation
  const imagePrompt =
    prompt ??
    `Luxury Indian ${event} event decor for ${area}. Color theme: ${theme}. Style: ${style ?? "elegant and opulent"}. Professional event photography style, warm ambient lighting, highly detailed, magazine quality.`;

  try {
    const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY! });

    const response = await openai.images.generate({
      model: "gpt-image-1",
      prompt: imagePrompt,
      n: 1,
      size: "1024x1024",
    });

    const imageData = response.data?.[0];
    if (!imageData) {
      return NextResponse.json({ error: "No image generated" }, { status: 500 });
    }

    // Get image as buffer
    let imageBuffer: Buffer;

    if (imageData.b64_json) {
      imageBuffer = Buffer.from(imageData.b64_json, "base64");
    } else if (imageData.url) {
      const imgResponse = await fetch(imageData.url);
      const arrayBuffer = await imgResponse.arrayBuffer();
      imageBuffer = Buffer.from(arrayBuffer);
    } else {
      return NextResponse.json({ error: "No image data" }, { status: 500 });
    }

    // Apply watermark
    const watermarkPath = path.join(process.cwd(), "public", "luxevenue-watermark.png");
    let watermarkedBuffer = imageBuffer;

    if (fs.existsSync(watermarkPath)) {
      const watermarkBuffer = await sharp(watermarkPath)
        .resize(154)
        .toBuffer();

      watermarkedBuffer = await sharp(imageBuffer)
        .composite([
          {
            input: watermarkBuffer,
            gravity: "southeast",
            blend: "over",
          },
        ])
        .png()
        .toBuffer();
    }

    const base64Image = watermarkedBuffer.toString("base64");

    // Record generation
    await prisma.imageGeneration.create({
      data: {
        userId,
        prompt: imagePrompt,
        area,
      },
    });

    return NextResponse.json({
      image: `data:image/png;base64,${base64Image}`,
    });
  } catch (error) {
    console.error("Image generation error:", error);
    return NextResponse.json(
      { error: "Generation failed" },
      { status: 500 }
    );
  }
}
