import { NextRequest, NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "@/lib/auth";
import sharp from "sharp";

export const maxDuration = 30;

export async function POST(req: NextRequest) {
  const session = await getServerSession(authOptions);
  if (!session?.user?.id) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
  }

  const { event_name, host_names, date, venue, theme_color } =
    (await req.json()) as {
      event_name: string;
      host_names: string;
      date: string;
      venue: string;
      theme_color?: string;
    };

  // Generate a simple, elegant digital invite as SVG → PNG
  const gold = theme_color ?? "#c9a84c";
  const width = 800;
  const height = 1100;

  const svgContent = `
<svg width="${width}" height="${height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117"/>
      <stop offset="100%" style="stop-color:#111827"/>
    </linearGradient>
    <linearGradient id="gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:${gold}"/>
      <stop offset="100%" style="stop-color:#e8c97a"/>
    </linearGradient>
  </defs>

  <!-- Background -->
  <rect width="${width}" height="${height}" fill="url(#bg)"/>

  <!-- Outer border -->
  <rect x="20" y="20" width="${width - 40}" height="${height - 40}"
        fill="none" stroke="${gold}" stroke-width="1" opacity="0.4"/>
  <rect x="28" y="28" width="${width - 56}" height="${height - 56}"
        fill="none" stroke="${gold}" stroke-width="0.5" opacity="0.2"/>

  <!-- Corner ornaments -->
  <text x="40" y="70" font-size="28" fill="${gold}" opacity="0.6" font-family="serif">✦</text>
  <text x="${width - 68}" y="70" font-size="28" fill="${gold}" opacity="0.6" font-family="serif">✦</text>
  <text x="40" y="${height - 35}" font-size="28" fill="${gold}" opacity="0.6" font-family="serif">✦</text>
  <text x="${width - 68}" y="${height - 35}" font-size="28" fill="${gold}" opacity="0.6" font-family="serif">✦</text>

  <!-- LuxeVenue branding -->
  <text x="${width / 2}" y="130"
        text-anchor="middle" font-family="Georgia, serif" font-size="13"
        fill="${gold}" opacity="0.7" letter-spacing="6">LUXEVENUE.AI</text>

  <!-- Divider top -->
  <line x1="80" y1="150" x2="${width - 80}" y2="150" stroke="${gold}" stroke-width="0.5" opacity="0.3"/>

  <!-- Event type -->
  <text x="${width / 2}" y="210"
        text-anchor="middle" font-family="Georgia, serif" font-size="11"
        fill="${gold}" opacity="0.8" letter-spacing="8">INVITATION</text>

  <!-- Main event name -->
  <text x="${width / 2}" y="310"
        text-anchor="middle" font-family="Georgia, serif" font-size="44"
        font-weight="600" fill="#ffffff">${escapeXml(event_name)}</text>

  <!-- Sparkle divider -->
  <text x="${width / 2}" y="370" text-anchor="middle" font-size="18" fill="${gold}">✦</text>

  <!-- Hosted by -->
  <text x="${width / 2}" y="430"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="11"
        fill="#8892a4" letter-spacing="4">HOSTED BY</text>
  <text x="${width / 2}" y="480"
        text-anchor="middle" font-family="Georgia, serif" font-size="28"
        fill="#e8eaf0">${escapeXml(host_names)}</text>

  <!-- Divider middle -->
  <line x1="120" y1="520" x2="${width - 120}" y2="520" stroke="${gold}" stroke-width="0.5" opacity="0.3"/>

  <!-- Date label -->
  <text x="${width / 2}" y="580"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="10"
        fill="${gold}" letter-spacing="5" opacity="0.8">DATE &amp; TIME</text>
  <text x="${width / 2}" y="620"
        text-anchor="middle" font-family="Georgia, serif" font-size="22"
        fill="#e8eaf0">${escapeXml(date)}</text>

  <!-- Venue label -->
  <text x="${width / 2}" y="690"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="10"
        fill="${gold}" letter-spacing="5" opacity="0.8">VENUE</text>
  <text x="${width / 2}" y="730"
        text-anchor="middle" font-family="Georgia, serif" font-size="20"
        fill="#e8eaf0">${escapeXml(venue)}</text>

  <!-- Bottom divider -->
  <line x1="80" y1="800" x2="${width - 80}" y2="800" stroke="${gold}" stroke-width="0.5" opacity="0.3"/>

  <!-- RSVP note -->
  <text x="${width / 2}" y="860"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="11"
        fill="#6b7280" letter-spacing="3">KINDLY RESPOND BY</text>
  <text x="${width / 2}" y="900"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="13"
        fill="#8892a4">Smart RSVP powered by LuxeVenue</text>

  <!-- LuxeVenue footer -->
  <text x="${width / 2}" y="1040"
        text-anchor="middle" font-family="Arial, sans-serif" font-size="10"
        fill="${gold}" opacity="0.5" letter-spacing="4">LUXEVENUE.AI</text>
</svg>`;

  try {
    const pngBuffer = await sharp(Buffer.from(svgContent))
      .png()
      .toBuffer();

    const base64 = pngBuffer.toString("base64");

    return NextResponse.json({
      image: `data:image/png;base64,${base64}`,
    });
  } catch (error) {
    console.error("Invite generation error:", error);
    return NextResponse.json(
      { error: "Failed to generate invite" },
      { status: 500 }
    );
  }
}

function escapeXml(str: string): string {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}
