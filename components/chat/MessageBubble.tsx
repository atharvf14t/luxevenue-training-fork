"use client";

import React, { useEffect, useState } from "react";
import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";
import { SuggestionChips } from "./SuggestionChips";
import { Download } from "lucide-react";

interface Message {
  role: "user" | "assistant";
  content: string;
}

interface MessageBubbleProps {
  message: Message;
  onChipClick: (text: string) => void;
}

interface ImageGenerationState {
  status: "loading" | "done" | "error";
  src?: string;
  errorMsg?: string;
}

function parseChips(content: string): { text: string; chips: string[] } {
  const chipsMatch = content.match(/\[CHIPS:\s*([^\]]+)\]/);
  if (!chipsMatch) return { text: content, chips: [] };

  const chips = chipsMatch[1]
    .split("|")
    .map((c) => c.trim())
    .filter(Boolean);

  const text = content.replace(/\[CHIPS:\s*[^\]]+\]/, "").trim();
  return { text, chips };
}

function parseImageMarker(content: string): {
  text: string;
  imageArgs: Record<string, string> | null;
} {
  const imageMatch = content.match(
    /\[GENERATE_IMAGE:\s*([^\]]+)\]/
  );
  if (!imageMatch) return { text: content, imageArgs: null };

  const argsStr = imageMatch[1];
  const args: Record<string, string> = {};
  const argRegex = /(\w+)="([^"]+)"/g;
  let m: RegExpExecArray | null;
  while ((m = argRegex.exec(argsStr)) !== null) {
    args[m[1]] = m[2];
  }

  const text = content.replace(/\[GENERATE_IMAGE:\s*[^\]]+\]/, "").trim();
  return { text, imageArgs: args };
}

function parseInviteMarker(content: string): {
  text: string;
  inviteArgs: Record<string, string> | null;
} {
  const inviteMatch = content.match(
    /\[GENERATE_INVITE:\s*([^\]]+)\]/
  );
  if (!inviteMatch) return { text: content, inviteArgs: null };

  const argsStr = inviteMatch[1];
  const args: Record<string, string> = {};
  const argRegex = /(\w+)="([^"]+)"/g;
  let m: RegExpExecArray | null;
  while ((m = argRegex.exec(argsStr)) !== null) {
    args[m[1]] = m[2];
  }

  const text = content.replace(/\[GENERATE_INVITE:\s*[^\]]+\]/, "").trim();
  return { text, inviteArgs: args };
}

function InlineImage({
  args,
}: {
  args: Record<string, string>;
}) {
  const [state, setState] = useState<ImageGenerationState>({
    status: "loading",
  });

  useEffect(() => {
    let cancelled = false;
    fetch("/api/generate-image", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        area: args.area,
        theme: args.theme,
        event: args.event,
        style: args.style,
      }),
    })
      .then(async (res) => {
        if (cancelled) return;
        if (res.status === 403) {
          const data = await res.json() as { message?: string };
          setState({
            status: "error",
            errorMsg: data.message ?? "Image generation not available for your account.",
          });
          return;
        }
        if (!res.ok) {
          setState({ status: "error", errorMsg: "Image generation failed." });
          return;
        }
        const data = await res.json() as { image?: string };
        if (data.image) {
          setState({ status: "done", src: data.image });
        } else {
          setState({ status: "error", errorMsg: "No image returned." });
        }
      })
      .catch(() => {
        if (!cancelled)
          setState({ status: "error", errorMsg: "Image generation failed." });
      });

    return () => {
      cancelled = true;
    };
  }, [args.area, args.theme, args.event, args.style]);

  if (state.status === "loading") {
    return (
      <div className="mt-3 w-64 h-40 rounded-xl bg-[#111827] border border-[#1e2d3d] animate-pulse flex items-center justify-center">
        <span className="text-[#4b5563] text-xs">Generating decor image...</span>
      </div>
    );
  }

  if (state.status === "error") {
    return (
      <p className="mt-2 text-xs italic text-[#6b7280]">
        {state.errorMsg}
      </p>
    );
  }

  return (
    <div className="mt-3 flex flex-col gap-2">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={state.src}
        alt={`Decor — ${args.area}`}
        className="rounded-xl max-w-sm border border-[#1e2d3d]"
      />
      <a
        href={state.src}
        download={`luxevenue-decor-${args.area}.png`}
        className="inline-flex items-center gap-1.5 text-xs text-[#c9a84c] hover:opacity-80 transition-opacity w-fit"
      >
        <Download size={12} />
        Download image
      </a>
    </div>
  );
}

function InlineInvite({ args }: { args: Record<string, string> }) {
  const [state, setState] = useState<ImageGenerationState>({
    status: "loading",
  });

  useEffect(() => {
    let cancelled = false;
    fetch("/api/generate-invite", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        event_name: args.event,
        host_names: args.hosts,
        date: args.date,
        venue: args.venue,
        theme_color: args.color,
      }),
    })
      .then(async (res) => {
        if (cancelled) return;
        if (!res.ok) {
          setState({ status: "error", errorMsg: "Could not generate invite." });
          return;
        }
        const data = await res.json() as { image?: string };
        if (data.image) setState({ status: "done", src: data.image });
        else setState({ status: "error", errorMsg: "No invite image returned." });
      })
      .catch(() => {
        if (!cancelled)
          setState({ status: "error", errorMsg: "Invite generation failed." });
      });

    return () => { cancelled = true; };
  }, [args.event, args.hosts, args.date, args.venue, args.color]);

  if (state.status === "loading") {
    return (
      <div className="mt-3 w-48 h-64 rounded-xl bg-[#111827] border border-[#1e2d3d] animate-pulse flex items-center justify-center">
        <span className="text-[#4b5563] text-xs">Creating invite...</span>
      </div>
    );
  }

  if (state.status === "error") {
    return <p className="mt-2 text-xs italic text-[#6b7280]">{state.errorMsg}</p>;
  }

  return (
    <div className="mt-3 flex flex-col gap-2">
      {/* eslint-disable-next-line @next/next/no-img-element */}
      <img
        src={state.src}
        alt="Digital Invite"
        className="rounded-xl max-w-xs border border-[#1e2d3d]"
      />
      <a
        href={state.src}
        download="luxevenue-invite.png"
        className="inline-flex items-center gap-1.5 text-xs text-[#c9a84c] hover:opacity-80 transition-opacity w-fit"
      >
        <Download size={12} />
        Download invite
      </a>
    </div>
  );
}

export function MessageBubble({ message, onChipClick }: MessageBubbleProps) {
  if (message.role === "user") {
    return (
      <div className="flex justify-end">
        <div className="max-w-[85%] md:max-w-[70%] bg-[#1a3a4a] text-[#e8eaf0] rounded-2xl rounded-tr-sm px-4 py-3 text-sm leading-relaxed">
          {message.content}
        </div>
      </div>
    );
  }

  // Parse markers from AI content
  let content = message.content;
  const { text: afterChips, chips } = parseChips(content);
  content = afterChips;

  const { text: afterImage, imageArgs } = parseImageMarker(content);
  content = afterImage;

  const { text: afterInvite, inviteArgs } = parseInviteMarker(content);
  content = afterInvite;

  return (
    <div className="flex gap-3 items-start">
      {/* AI avatar */}
      <div className="w-7 h-7 rounded-full bg-[#111827] border border-[#1e2d3d] flex items-center justify-center text-[#c9a84c] text-xs flex-shrink-0 mt-0.5">
        ✦
      </div>

      <div className="flex-1 text-sm text-[#e8eaf0] leading-relaxed">
        {/* Markdown content */}
        <div className="chat-markdown">
          <ReactMarkdown
            remarkPlugins={[remarkGfm]}
            components={{
              a: ({ href, children }) => (
                <a
                  href={href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="text-[#c9a84c] underline underline-offset-2 hover:opacity-80 transition-opacity"
                >
                  {children}
                </a>
              ),
            }}
          >
            {content}
          </ReactMarkdown>
        </div>

        {/* Inline image */}
        {imageArgs && <InlineImage args={imageArgs} />}

        {/* Inline invite */}
        {inviteArgs && <InlineInvite args={inviteArgs} />}

        {/* Suggestion chips */}
        {chips.length > 0 && (
          <SuggestionChips chips={chips} onChipClick={onChipClick} />
        )}
      </div>
    </div>
  );
}

const LOADER_PHRASES = [
  "Curating ideas...",
  "Generating options...",
  "Curating recommendations...",
  "Generating your plan...",
];

export function TypingIndicator() {
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [visible, setVisible] = useState(true);

  useEffect(() => {
    const interval = setInterval(() => {
      setVisible(false);
      setTimeout(() => {
        setPhraseIndex((i) => (i + 1) % LOADER_PHRASES.length);
        setVisible(true);
      }, 300);
    }, 2000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex gap-3 items-start">
      <div className="w-7 h-7 rounded-full bg-[#111827] border border-[#1e2d3d] flex items-center justify-center text-[#c9a84c] text-xs flex-shrink-0 mt-0.5">
        ✦
      </div>
      <div className="flex items-center py-2">
        <span
          className="text-sm text-[#4b5563] transition-opacity duration-300"
          style={{ opacity: visible ? 1 : 0 }}
        >
          {LOADER_PHRASES[phraseIndex]}
        </span>
      </div>
    </div>
  );
}
