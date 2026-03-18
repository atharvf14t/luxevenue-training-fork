import { NextAuthOptions } from "next-auth";
import GoogleProvider from "next-auth/providers/google";
import { PrismaAdapter } from "@auth/prisma-adapter";
import { prisma } from "./prisma";

export const authOptions: NextAuthOptions = {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  adapter: PrismaAdapter(prisma) as any,
  providers: [
    GoogleProvider({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!,
    }),
  ],
  session: {
    strategy: "database",
  },
  callbacks: {
    async session({ session, user }) {
      if (session.user) {
        session.user.id = user.id;
        try {
          const dbUser = await prisma.user.findUnique({
            where: { id: user.id },
            select: { maxImages: true, name: true },
          });
          session.user.maxImages = dbUser?.maxImages ?? 0;
          session.user.name = dbUser?.name ?? session.user.name ?? "";
        } catch {
          session.user.maxImages = 0;
          session.user.name = session.user.name ?? "";
        }
      }
      return session;
    },
  },
  pages: {
    signIn: "/login",
  },
  events: {
    async createUser({ user }) {
      // Set name from Google display name on first creation
      if (user.name && user.id) {
        await prisma.user.update({
          where: { id: user.id },
          data: { name: user.name },
        });
      }
    },
  },
};

// Extend next-auth types
declare module "next-auth" {
  interface Session {
    user: {
      id: string;
      name: string;
      email: string;
      image?: string;
      maxImages: number;
    };
  }
}
