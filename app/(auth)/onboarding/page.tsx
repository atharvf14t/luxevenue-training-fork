"use client";

import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useState, useEffect } from "react";

export default function OnboardingPage() {
  const { data: session, status, update } = useSession();
  const router = useRouter();
  const [displayName, setDisplayName] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    if (status === "unauthenticated") {
      router.push("/login");
    }
    // Pre-fill with Google display name
    if (session?.user?.name) {
      setDisplayName(session.user.name.split(" ")[0] ?? "");
    }
  }, [status, session, router]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!displayName.trim()) return;

    setLoading(true);
    setError("");

    try {
      const res = await fetch("/api/user/name", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name: displayName.trim() }),
      });

      if (!res.ok) throw new Error("Failed to save name");

      await update({ name: displayName.trim() });
      router.push("/chat");
    } catch {
      setError("Something went wrong. Please try again.");
      setLoading(false);
    }
  };

  return (
    <div className="flex h-screen w-screen items-center justify-center bg-[#0d1117]">
      <div className="flex flex-col items-center gap-8 rounded-2xl border border-[#1e2d3d] bg-[#111827] p-10 w-full max-w-sm">
        {/* Logo */}
        <div className="text-center">
          <div className="mb-3 flex items-center justify-center">
            <div className="w-14 h-14 rounded-full bg-[#111827] border border-[#1e2d3d] flex items-center justify-center text-[#c9a84c] text-xl">
              ✦
            </div>
          </div>
          <h1 className="font-playfair text-2xl font-semibold text-white">
            Welcome to LuxeVenue
          </h1>
          <p className="mt-2 text-sm text-[#6b7280]">
            What should we call you?
          </p>
        </div>

        <form onSubmit={handleSubmit} className="w-full flex flex-col gap-4">
          <input
            type="text"
            value={displayName}
            onChange={(e) => setDisplayName(e.target.value)}
            placeholder="Your first name"
            className="w-full rounded-xl border border-[#2a3a50] bg-[#161e2e] px-4 py-3 text-sm text-[#e8eaf0] placeholder-[#4b5563] outline-none focus:border-[#3a4a60] transition-colors"
            autoFocus
            maxLength={50}
          />

          {error && <p className="text-xs text-red-400">{error}</p>}

          <button
            type="submit"
            disabled={!displayName.trim() || loading}
            className="w-full rounded-xl bg-[#c9a84c] px-5 py-3 text-sm font-semibold text-black transition-colors hover:bg-[#d4b86a] disabled:bg-[#1e2d40] disabled:text-[#374151] disabled:cursor-not-allowed"
          >
            {loading ? "Saving..." : "Continue"}
          </button>
        </form>
      </div>
    </div>
  );
}
