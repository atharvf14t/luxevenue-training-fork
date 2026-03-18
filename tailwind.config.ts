import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        playfair: ["var(--font-playfair)", "Georgia", "serif"],
        sans: ["var(--font-inter)", "system-ui", "sans-serif"],
      },
      colors: {
        gold: "#c9a84c",
        "gold-light": "#d4b86a",
        "navy-darkest": "#0d1117",
        "navy-dark": "#0e1420",
        "navy-sidebar": "#111827",
        "navy-input": "#161e2e",
        "navy-card": "#131c2e",
        "border-subtle": "#1e2d3d",
        "border-medium": "#2a3a50",
        "border-focus": "#3a4a60",
        "text-primary": "#e8eaf0",
        "text-secondary": "#8892a4",
        "text-muted": "#6b7280",
        "text-faint": "#4b5563",
        "text-disabled": "#374151",
        "bubble-user": "#1a3a4a",
        "avatar-bg": "#1e2d40",
      },
      animation: {
        "bounce-1": "bounce 1s infinite 0ms",
        "bounce-2": "bounce 1s infinite 150ms",
        "bounce-3": "bounce 1s infinite 300ms",
      },
    },
  },
  plugins: [],
};

export default config;
