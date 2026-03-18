# LuxeVenue Setup Guide

## Prerequisites
- Node.js 18+
- PostgreSQL running locally (or a hosted Postgres URL)

## 1. Environment Variables

Edit `.env.local` and fill in your credentials:

```env
# Azure OpenAI (chat)
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_DEPLOYMENT=gpt-4o-2024-08-06
AZURE_OPENAI_API_VERSION=2024-08-01-preview

# OpenAI (image generation — gpt-image-1)
OPENAI_API_KEY=your-key

# Google OAuth
# Create at https://console.cloud.google.com → APIs & Services → OAuth 2.0 Client IDs
# Authorized redirect URI: http://localhost:3000/api/auth/callback/google
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=

# NextAuth
NEXTAUTH_SECRET=run-openssl-rand-base64-32-to-generate
NEXTAUTH_URL=http://localhost:3000

# PostgreSQL
DATABASE_URL=postgresql://postgres:password@localhost:5432/luxevenue

# Web search (optional)
SERPER_API_KEY=
```

## 2. Database Setup

```bash
# Create the database (if using local PostgreSQL)
createdb luxevenue

# Also update prisma.config.ts if needed — it reads DATABASE_URL automatically

# Run migrations
npm run db:push

# Seed with real venue/artist/vendor data
npm run db:seed
```

## 3. Generate Watermark (one-time)

```bash
npm run watermark
```

## 4. Run Development Server

```bash
npm run dev
```

Open http://localhost:3000

## 5. First Login

1. Navigate to http://localhost:3000 → redirects to /login
2. Click "Continue with Google"
3. On first login → /onboarding → enter your display name
4. You're in! The chat interface should match the design exactly.

## 6. Testing Image Generation

Image generation is disabled by default (maxImages = 0).
To enable for a user, run in psql:

```sql
UPDATE "User" SET "maxImages" = 10 WHERE email = 'your@email.com';
```

## 7. Deploying to Vercel

See Phase 13 of the implementation plan. Key steps:
- Move DATABASE_URL to Neon or Supabase
- Set all env vars in Vercel dashboard
- Deploy with `vercel --prod`
