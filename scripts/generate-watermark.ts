import sharp from "sharp";
import path from "path";

// Generate a simple LuxeVenue watermark PNG
const svg = `<svg width="200" height="40" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="28"
        font-family="Georgia, serif"
        font-size="18"
        font-weight="600"
        fill="white"
        opacity="0.7"
        letter-spacing="1">
    ✦ LuxeVenue
  </text>
</svg>`;

const outputPath = path.join(process.cwd(), "public", "luxevenue-watermark.png");

sharp(Buffer.from(svg))
  .png()
  .toFile(outputPath)
  .then(() => {
    console.log(`✅ Watermark generated: ${outputPath}`);
  })
  .catch((err) => {
    console.error("❌ Failed to generate watermark:", err);
    process.exit(1);
  });
