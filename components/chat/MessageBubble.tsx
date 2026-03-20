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

// ─── Types for new markers ─────────────────────────────────────────────────

interface VenueCardData {
  name: string;
  city: string;
  state: string;
  capacity: number;
  rooms: number;
  priceMin: number;
  priceMax: number;
  style: string;
  url: string;
  totalMin: number;
  totalMax: number;
}

interface VenueCardsPayload {
  venues: VenueCardData[];
  guestCount: number;
}

interface MenuCardsPayload {
  venueName: string;
  city: string;
  guestCount: number;
  priceMin: number;
  priceMax: number;
}

interface ArtistData {
  name: string;
  type: string;
  city: string;
  description: string;
  priceMin: number;
  priceMax: number;
}

interface ArtistCardsPayload {
  category: string;
  artists: ArtistData[];
}

interface VendorData {
  name: string;
  type: string;
  city: string;
  description: string;
  priceMin: number;
  priceMax: number;
}

interface VendorCardsPayload {
  category: string;
  vendors: VendorData[];
}

interface BookingTotalItem {
  label: string;
  amount: number;
}

interface BookingTotalPayload {
  items: BookingTotalItem[];
  total: number;
}

// ─── Marker parsers ────────────────────────────────────────────────────────

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
  const imageMatch = content.match(/\[GENERATE_IMAGE:\s*([^\]]+)\]/);
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
  const inviteMatch = content.match(/\[GENERATE_INVITE:\s*([^\]]+)\]/);
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

function parseJsonMarker<T>(
  content: string,
  tag: string
): { text: string; data: T | null } {
  const regex = new RegExp(`\\[${tag}:\\s*(\\{[\\s\\S]*?\\})\\]`);
  const match = content.match(regex);
  if (!match) return { text: content, data: null };

  try {
    const data = JSON.parse(match[1]) as T;
    const text = content.replace(regex, "").trim();
    return { text, data };
  } catch {
    return { text: content, data: null };
  }
}

// ─── Helpers ───────────────────────────────────────────────────────────────

function inr(amount: number): string {
  return "₹" + amount.toLocaleString("en-IN");
}

// ─── UI Components ─────────────────────────────────────────────────────────

function VenueCards({
  payload,
  onChipClick,
}: {
  payload: VenueCardsPayload;
  onChipClick: (text: string) => void;
}) {
  return (
    <div className="mt-3 flex flex-col gap-3">
      {payload.venues.map((v) => (
        <div
          key={v.name}
          className="rounded-xl border border-[#1e2d3d] bg-[#0d1b2a] p-4 flex flex-col gap-2"
        >
          <div className="flex items-start justify-between gap-2">
            <div>
              <p className="font-semibold text-[#e8eaf0] text-sm">{v.name}</p>
              <p className="text-xs text-[#6b7280]">
                {v.city}, {v.state}
              </p>
            </div>
            <span className="text-xs text-[#c9a84c] bg-[#1a2a1a] border border-[#2d4a1e] px-2 py-0.5 rounded-full whitespace-nowrap">
              {v.style}
            </span>
          </div>

          <div className="flex gap-4 text-xs text-[#9ca3af]">
            <span>👥 Up to {v.capacity} guests</span>
            <span>🛏 {v.rooms} rooms</span>
          </div>

          <div className="text-xs text-[#c9a84c]">
            Est. total for {payload.guestCount} guests:{" "}
            <span className="font-semibold">
              {inr(v.totalMin)} – {inr(v.totalMax)}
            </span>
            <span className="text-[#6b7280] ml-1">
              (₹{v.priceMin}–₹{v.priceMax}/plate)
            </span>
          </div>

          <div className="flex gap-2 mt-1">
            {v.url && v.url !== "" && (
              <a
                href={v.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-xs px-3 py-1.5 rounded-lg border border-[#1e2d3d] text-[#c9a84c] hover:bg-[#1e2d3d] transition-colors"
              >
                View →
              </a>
            )}
            <button
              onClick={() =>
                onChipClick(
                  `I want to book ${v.name}, ${v.city} for my event`
                )
              }
              className="text-xs px-3 py-1.5 rounded-lg bg-[#c9a84c] text-[#0a0f1a] font-semibold hover:opacity-90 transition-opacity"
            >
              Book This Venue
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

const MENU_TIERS = [
  {
    key: "2+2 Essential",
    label: "2+2 Essential",
    description: "2 starters + 2 mains + dessert + soft beverages",
    priceFn: (min: number, _max: number) => min,
  },
  {
    key: "3+3 Premium",
    label: "3+3 Premium",
    description:
      "3 starters + 3 mains + 2 desserts + welcome drink + live counter",
    priceFn: (min: number, max: number) => Math.round((min + max) / 2),
  },
  {
    key: "5+5 Grand",
    label: "5+5 Grand",
    description:
      "5 starters + 5 mains + 3 desserts + welcome drink + 2 live stations + midnight snack",
    priceFn: (_min: number, max: number) => max,
  },
];

function MenuCards({
  payload,
  onChipClick,
}: {
  payload: MenuCardsPayload;
  onChipClick: (text: string) => void;
}) {
  return (
    <div className="mt-3 flex flex-col gap-3">
      {MENU_TIERS.map((tier) => {
        const pricePerPlate = tier.priceFn(payload.priceMin, payload.priceMax);
        const totalAmount = payload.guestCount * pricePerPlate;
        return (
          <button
            key={tier.key}
            onClick={() =>
              onChipClick(
                `I choose the ${tier.label} menu for ${inr(totalAmount)} — ${payload.guestCount} guests × ₹${pricePerPlate}/plate`
              )
            }
            className="text-left rounded-xl border border-[#1e2d3d] bg-[#0d1b2a] p-4 hover:border-[#c9a84c] hover:bg-[#0f1f30] transition-all group"
          >
            <div className="flex items-center justify-between">
              <p className="font-semibold text-[#e8eaf0] text-sm group-hover:text-[#c9a84c] transition-colors">
                {tier.label}
              </p>
              <div className="text-right">
                <p className="text-sm font-bold text-[#c9a84c]">
                  {inr(totalAmount)}
                </p>
                <p className="text-xs text-[#6b7280]">
                  ₹{pricePerPlate}/plate × {payload.guestCount}
                </p>
              </div>
            </div>
            <p className="mt-1 text-xs text-[#9ca3af]">{tier.description}</p>
          </button>
        );
      })}
    </div>
  );
}

function ArtistCards({
  payload,
  onChipClick,
}: {
  payload: ArtistCardsPayload;
  onChipClick: (text: string) => void;
}) {
  return (
    <div className="mt-3 flex flex-col gap-3">
      {payload.artists.map((a) => (
        <div
          key={a.name}
          className="rounded-xl border border-[#1e2d3d] bg-[#0d1b2a] p-4 flex flex-col gap-2"
        >
          <div className="flex items-start justify-between gap-2">
            <div>
              <p className="font-semibold text-[#e8eaf0] text-sm">{a.name}</p>
              <p className="text-xs text-[#6b7280]">
                {a.type} · {a.city}
              </p>
            </div>
            <span className="text-xs text-[#c9a84c] whitespace-nowrap font-semibold">
              {inr(a.priceMin)} – {inr(a.priceMax)}
            </span>
          </div>
          <p className="text-xs text-[#9ca3af] leading-relaxed">
            {a.description}
          </p>
          <button
            onClick={() =>
              onChipClick(`Book ${a.name} for my event at ₹${a.priceMin}`)
            }
            className="mt-1 w-fit text-xs px-3 py-1.5 rounded-lg bg-[#c9a84c] text-[#0a0f1a] font-semibold hover:opacity-90 transition-opacity"
          >
            Book {a.name}
          </button>
        </div>
      ))}
    </div>
  );
}

function VendorCards({
  payload,
  onChipClick,
}: {
  payload: VendorCardsPayload;
  onChipClick: (text: string) => void;
}) {
  return (
    <div className="mt-3 flex flex-col gap-3">
      {payload.vendors.map((v) => (
        <div
          key={v.name}
          className="rounded-xl border border-[#1e2d3d] bg-[#0d1b2a] p-4 flex flex-col gap-2"
        >
          <div className="flex items-start justify-between gap-2">
            <div>
              <p className="font-semibold text-[#e8eaf0] text-sm">{v.name}</p>
              <p className="text-xs text-[#6b7280]">
                {v.type} · {v.city}
              </p>
            </div>
            <span className="text-xs text-[#c9a84c] whitespace-nowrap font-semibold">
              {inr(v.priceMin)} – {inr(v.priceMax)}
            </span>
          </div>
          <p className="text-xs text-[#9ca3af] leading-relaxed">
            {v.description}
          </p>
          <button
            onClick={() =>
              onChipClick(`Enquire about ${v.name} for my event`)
            }
            className="mt-1 w-fit text-xs px-3 py-1.5 rounded-lg border border-[#c9a84c] text-[#c9a84c] font-semibold hover:bg-[#c9a84c] hover:text-[#0a0f1a] transition-all"
          >
            Enquire
          </button>
        </div>
      ))}
    </div>
  );
}

function BookingTotal({ payload }: { payload: BookingTotalPayload }) {
  return (
    <div className="mt-3 rounded-xl border border-[#2d4a1e] bg-[#0a150a] p-4 max-w-sm">
      <p className="text-xs font-semibold text-[#c9a84c] uppercase tracking-wider mb-3">
        Booking Summary
      </p>
      <div className="flex flex-col gap-1.5">
        {payload.items.map((item, i) => (
          <div key={i} className="flex items-start justify-between gap-4">
            <span className="text-xs text-[#9ca3af] flex-1">{item.label}</span>
            <span className="text-xs text-[#e8eaf0] whitespace-nowrap font-medium">
              {inr(item.amount)}
            </span>
          </div>
        ))}
      </div>
      <div className="mt-3 pt-3 border-t border-[#1e2d3d] flex items-center justify-between">
        <span className="text-sm font-semibold text-[#e8eaf0]">Total</span>
        <span className="text-sm font-bold text-[#c9a84c]">
          {inr(payload.total)}
        </span>
      </div>
    </div>
  );
}

// ─── Image & Invite components ─────────────────────────────────────────────

function InlineImage({ args }: { args: Record<string, string> }) {
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
          const data = (await res.json()) as { message?: string };
          setState({
            status: "error",
            errorMsg:
              data.message ?? "Image generation not available for your account.",
          });
          return;
        }
        if (!res.ok) {
          setState({ status: "error", errorMsg: "Image generation failed." });
          return;
        }
        const data = (await res.json()) as { image?: string };
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
      <p className="mt-2 text-xs italic text-[#6b7280]">{state.errorMsg}</p>
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
        const data = (await res.json()) as { image?: string };
        if (data.image) setState({ status: "done", src: data.image });
        else
          setState({ status: "error", errorMsg: "No invite image returned." });
      })
      .catch(() => {
        if (!cancelled)
          setState({ status: "error", errorMsg: "Invite generation failed." });
      });

    return () => {
      cancelled = true;
    };
  }, [args.event, args.hosts, args.date, args.venue, args.color]);

  if (state.status === "loading") {
    return (
      <div className="mt-3 w-48 h-64 rounded-xl bg-[#111827] border border-[#1e2d3d] animate-pulse flex items-center justify-center">
        <span className="text-[#4b5563] text-xs">Creating invite...</span>
      </div>
    );
  }

  if (state.status === "error") {
    return (
      <p className="mt-2 text-xs italic text-[#6b7280]">{state.errorMsg}</p>
    );
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

// ─── Main MessageBubble ────────────────────────────────────────────────────

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

  // Parse all markers
  let content = message.content;

  const { text: t1, chips } = parseChips(content);
  content = t1;

  const { text: t2, imageArgs } = parseImageMarker(content);
  content = t2;

  const { text: t3, inviteArgs } = parseInviteMarker(content);
  content = t3;

  const { text: t4, data: venueCardsData } =
    parseJsonMarker<VenueCardsPayload>(content, "VENUE_CARDS");
  content = t4;

  const { text: t5, data: menuCardsData } =
    parseJsonMarker<MenuCardsPayload>(content, "MENU_CARDS");
  content = t5;

  const { text: t6, data: artistCardsData } =
    parseJsonMarker<ArtistCardsPayload>(content, "ARTIST_CARDS");
  content = t6;

  const { text: t7, data: vendorCardsData } =
    parseJsonMarker<VendorCardsPayload>(content, "VENDOR_CARDS");
  content = t7;

  const { text: t8, data: bookingTotalData } =
    parseJsonMarker<BookingTotalPayload>(content, "BOOKING_TOTAL");
  content = t8;

  return (
    <div className="flex gap-3 items-start">
      {/* AI avatar */}
      <div className="w-7 h-7 rounded-full bg-[#111827] border border-[#1e2d3d] flex items-center justify-center text-[#c9a84c] text-xs flex-shrink-0 mt-0.5">
        ✦
      </div>

      <div className="flex-1 text-sm text-[#e8eaf0] leading-relaxed">
        {/* Markdown content */}
        {content && (
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
        )}

        {/* Venue cards */}
        {venueCardsData && (
          <VenueCards payload={venueCardsData} onChipClick={onChipClick} />
        )}

        {/* Menu tier cards */}
        {menuCardsData && (
          <MenuCards payload={menuCardsData} onChipClick={onChipClick} />
        )}

        {/* Artist cards */}
        {artistCardsData && (
          <ArtistCards payload={artistCardsData} onChipClick={onChipClick} />
        )}

        {/* Vendor cards */}
        {vendorCardsData && (
          <VendorCards payload={vendorCardsData} onChipClick={onChipClick} />
        )}

        {/* Booking total */}
        {bookingTotalData && <BookingTotal payload={bookingTotalData} />}

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
