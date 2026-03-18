import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

const PROTECTED = ["/chat", "/onboarding"];

export function middleware(req: NextRequest) {
  const isProtected = PROTECTED.some((p) =>
    req.nextUrl.pathname.startsWith(p)
  );
  if (!isProtected) return NextResponse.next();

  // NextAuth sets this cookie on successful sign-in
  // http (dev): next-auth.session-token
  // https (prod): __Secure-next-auth.session-token
  const sessionCookie =
    req.cookies.get("next-auth.session-token") ??
    req.cookies.get("__Secure-next-auth.session-token");

  if (!sessionCookie) {
    return NextResponse.redirect(new URL("/login", req.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/chat/:path*", "/onboarding"],
};
