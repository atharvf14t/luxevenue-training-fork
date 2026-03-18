"use client";

import { signIn, useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

export default function LoginPage() {
  const { data: session, status } = useSession();
  const router = useRouter();

  useEffect(() => {
    if (status === "authenticated") {
      router.push("/chat");
    }
  }, [status, router]);

  return (
    <div className="flex h-screen w-screen items-center justify-center bg-[#0d1117]">
      <div className="flex flex-col items-center gap-8 rounded-2xl border border-[#1e2d3d] bg-[#111827] p-10 w-full max-w-sm">
        {/* Logo */}
        <div className="text-center">
          <h1 className="font-playfair text-3xl font-semibold text-white">
            LuxeVenue<span className="text-[#c9a84c]">.ai</span>
          </h1>
          <p className="mt-2 text-sm text-[#6b7280]">
            Your intelligent event planning concierge
          </p>
        </div>

        {/* Divider */}
        <div className="h-px w-full bg-[#1e2d3d]" />

        {/* Sign in button */}
        <button
          onClick={() => signIn("google", { callbackUrl: "/chat" })}
          className="flex w-full items-center justify-center gap-3 rounded-xl border border-[#2a3a50] bg-[#161e2e] px-5 py-3 text-sm font-medium text-[#e8eaf0] transition-colors hover:bg-[#1e2d40] hover:border-[#3a4a60]"
        >
          <svg width="18" height="18" viewBox="0 0 18 18" fill="none">
            <path
              d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 01-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.875 2.684-6.615z"
              fill="#4285F4"
            />
            <path
              d="M9 18c2.43 0 4.467-.806 5.956-2.18l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 009 18z"
              fill="#34A853"
            />
            <path
              d="M3.964 10.71A5.41 5.41 0 013.682 9c0-.593.102-1.17.282-1.71V4.958H.957A8.996 8.996 0 000 9c0 1.452.348 2.827.957 4.042l3.007-2.332z"
              fill="#FBBC05"
            />
            <path
              d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 00.957 4.958L3.964 6.29C4.672 4.163 6.656 3.58 9 3.58z"
              fill="#EA4335"
            />
          </svg>
          Continue with Google
        </button>

        <p className="text-center text-[10px] text-[#374151]">
          By signing in, you agree to our Terms of Service and Privacy Policy.
        </p>
      </div>
    </div>
  );
}
