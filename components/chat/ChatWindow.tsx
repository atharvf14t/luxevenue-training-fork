"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { useRouter } from "next/navigation";
import { useSession } from "next-auth/react";
import { Menu } from "lucide-react";
import { ChatInput } from "./ChatInput";
import { MessageBubble, TypingIndicator } from "./MessageBubble";
import { useSidebar } from "./SidebarContext";

interface Message {
  id: string;
  role: "user" | "assistant";
  content: string;
}

interface ChatWindowProps {
  sessionId?: string;
}

const SUGGESTION_CARDS = [
  "Find luxury wedding venues in Delhi for 300 guests",
  "Recommend a jazz band for a cocktail reception",
  "Help me shortlist ballroom venues for a corporate gala",
  "Suggest menu and hospitality options for a destination wedding",
];

export function ChatWindow({ sessionId }: ChatWindowProps) {
  const { data: session } = useSession();
  const { toggle: onSidebarToggle } = useSidebar();
  const router = useRouter();
  const [messages, setMessages] = useState<Message[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [isFirstMessage, setIsFirstMessage] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const activeSessionId = useRef<string | null>(sessionId ?? null);

  // Load messages when sessionId changes
  useEffect(() => {
    if (!sessionId) {
      setMessages([]);
      setIsFirstMessage(true);
      return;
    }

    activeSessionId.current = sessionId;

    fetch(`/api/sessions/${sessionId}`)
      .then((res) => res.ok ? res.json() : null)
      .then((data: { messages?: { id: string; role: string; content: string }[] } | null) => {
        if (data?.messages) {
          setMessages(
            data.messages.map((m) => ({
              id: m.id,
              role: m.role as "user" | "assistant",
              content: m.content,
            }))
          );
          setIsFirstMessage(data.messages.length === 0);
        }
      })
      .catch(() => {});
  }, [sessionId]);

  // Auto-scroll on new messages
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  const sendMessage = useCallback(
    async (text: string) => {
      if (!text.trim() || isLoading) return;

      let currentSessionId = activeSessionId.current;
      let pendingNavigation: string | null = null;

      // Create a new session if none exists
      if (!currentSessionId) {
        const res = await fetch("/api/sessions", { method: "POST" });
        if (res.status === 403) {
          const data = await res.json() as { error: string };
          if (data.error === "SESSION_LIMIT_REACHED") {
            // The sidebar handles this via its own state
            return;
          }
        }
        if (!res.ok) return;

        const newSession = await res.json() as { id: string };
        currentSessionId = newSession.id;
        activeSessionId.current = currentSessionId;
        pendingNavigation = currentSessionId; // defer navigation until stream completes
      }

      const userMessage: Message = {
        id: Date.now().toString(),
        role: "user",
        content: text,
      };

      setMessages((prev) => [...prev, userMessage]);
      setIsLoading(true);

      // Fire-and-forget title generation for first message
      const wasFirstMessage = isFirstMessage;
      if (wasFirstMessage) {
        setIsFirstMessage(false);
        fetch(`/api/sessions/${currentSessionId}/title`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: text }),
        }).catch(() => {});
      }

      try {
        const response = await fetch("/api/chat", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ sessionId: currentSessionId, message: text }),
        });

        if (!response.ok || !response.body) {
          throw new Error("Chat request failed");
        }

        // Stream the response
        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let aiContent = "";

        const aiMessage: Message = {
          id: (Date.now() + 1).toString(),
          role: "assistant",
          content: "",
        };
        setMessages((prev) => [...prev, aiMessage]);
        setIsLoading(false);

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const chunk = decoder.decode(value, { stream: true });
          aiContent += chunk;

          setMessages((prev) =>
            prev.map((m) =>
              m.id === aiMessage.id ? { ...m, content: aiContent } : m
            )
          );
        }

        // Navigate after stream completes so the response is visible immediately
        if (pendingNavigation) {
          router.push(`/chat/${pendingNavigation}`);
        }
      } catch {
        setIsLoading(false);
        if (pendingNavigation) {
          router.push(`/chat/${pendingNavigation}`);
        }
        setMessages((prev) => [
          ...prev,
          {
            id: (Date.now() + 1).toString(),
            role: "assistant",
            content:
              "I apologize, I encountered an issue processing your request. Please try again.",
          },
        ]);
      }
    },
    [isLoading, isFirstMessage, router]
  );

  const userName = session?.user?.name?.split(" ")[0] ?? "";
  const userInitial = (session?.user?.name ?? session?.user?.email ?? "U")[0].toUpperCase();

  return (
    <div className="flex-1 flex flex-col h-full overflow-hidden bg-[#0d1117]">
      {/* Top bar */}
      <div className="flex items-center justify-between px-4 md:px-6 py-4 border-b border-[#1e2d3d] flex-shrink-0">
        <div className="flex items-center gap-3">
          {/* Hamburger (mobile) */}
          <button
            onClick={onSidebarToggle}
            className="flex md:hidden w-8 h-8 items-center justify-center text-[#6b7280] hover:text-[#e8eaf0] transition-colors"
          >
            <Menu size={18} />
          </button>
          <div className="flex items-center gap-2">
            <span className="text-[11px] tracking-[0.25em] uppercase text-[#6b7280] font-medium">
              AI CONCIERGE
            </span>
            <span className="text-[#c9a84c] text-sm">✦</span>
          </div>
        </div>

        {/* User avatar */}
        <div className="w-8 h-8 rounded-full bg-[#1e2d40] border border-[#2a3a50] flex items-center justify-center text-xs text-[#e8eaf0] font-medium">
          {userInitial}
        </div>
      </div>

      {/* Content area */}
      {messages.length === 0 && !isLoading ? (
        /* Empty state */
        <div className="flex-1 flex flex-col items-center justify-center px-4 md:px-8 text-center overflow-y-auto py-8">
          {/* Sparkle circle */}
          <div className="w-20 h-20 rounded-full bg-[#111827] border border-[#1e2d3d] flex items-center justify-center text-[#c9a84c] text-2xl mb-8 flex-shrink-0">
            ✦
          </div>

          {/* Headline */}
          <h2 className="font-playfair text-[32px] md:text-[38px] font-semibold text-[#e8eaf0] leading-tight mb-4 max-w-lg">
            How may we assist your event today?
          </h2>

          {/* Subtitle */}
          <p className="text-sm text-[#6b7280] max-w-md leading-relaxed mb-8">
            From venue discovery to guest experience, the LuxeVenue AI
            Concierge helps you plan with intelligence, discretion, and ease.
          </p>

          {/* Suggestion cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3 w-full max-w-2xl mb-8">
            {SUGGESTION_CARDS.map((card, i) => (
              <button
                key={i}
                onClick={() => sendMessage(card)}
                className="p-4 rounded-xl bg-[#111827] border border-[#1e2d3d] text-left text-sm text-[#e8eaf0] cursor-pointer hover:border-[#2a3a50] hover:bg-[#131c2e] transition-all min-h-[80px] flex items-start"
              >
                {card}
              </button>
            ))}
          </div>
        </div>
      ) : (
        /* Message list */
        <div className="flex-1 overflow-y-auto px-4 md:px-6 py-4 space-y-6">
          {messages.map((msg) => (
            <MessageBubble
              key={msg.id}
              message={msg}
              onChipClick={sendMessage}
            />
          ))}
          {isLoading && <TypingIndicator />}
          <div ref={messagesEndRef} />
        </div>
      )}

      {/* Input bar (always visible) */}
      <ChatInput onSend={sendMessage} disabled={isLoading} />
    </div>
  );
}
