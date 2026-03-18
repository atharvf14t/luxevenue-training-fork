"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { useRouter, usePathname } from "next/navigation";
import { MessageSquare, Plus, Settings, User, Trash2, LogOut } from "lucide-react";
import { useSession, signOut } from "next-auth/react";
import { SessionLimitModal } from "@/components/modals/SessionLimitModal";

interface ChatSession {
  id: string;
  title: string;
  updatedAt: string;
}

interface ChatSidebarProps {
  isOpen?: boolean;
  onClose?: () => void;
}

export function ChatSidebar({ isOpen = true, onClose }: ChatSidebarProps) {
  const router = useRouter();
  const pathname = usePathname();
  const { data: session } = useSession();
  const [sessions, setSessions] = useState<ChatSession[]>([]);
  const [showLimitModal, setShowLimitModal] = useState(false);
  const [deleteConfirmId, setDeleteConfirmId] = useState<string | null>(null);
  const [showProfileMenu, setShowProfileMenu] = useState(false);
  const profileMenuRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!showProfileMenu) return;
    function handleClickOutside(e: MouseEvent) {
      if (profileMenuRef.current && !profileMenuRef.current.contains(e.target as Node)) {
        setShowProfileMenu(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, [showProfileMenu]);

  const fetchSessions = useCallback(async () => {
    try {
      const res = await fetch("/api/sessions");
      if (res.ok) {
        const data = await res.json() as ChatSession[];
        setSessions(data);
      }
    } catch {
      // silent
    }
  }, []);

  useEffect(() => {
    fetchSessions();
  }, [fetchSessions, pathname]);

  const handleNewConversation = async () => {
    const res = await fetch("/api/sessions", { method: "POST" });

    if (res.status === 403) {
      const data = await res.json() as { error: string };
      if (data.error === "SESSION_LIMIT_REACHED") {
        setShowLimitModal(true);
        return;
      }
    }

    if (res.ok) {
      const newSession = await res.json() as { id: string; title: string; updatedAt: string; createdAt: string };
      setSessions(prev => [newSession, ...prev].slice(0, 5));
      router.push(`/chat/${newSession.id}`);
      onClose?.();
    }
  };

  const handleDeleteSession = async (sessionId: string) => {
    if (deleteConfirmId !== sessionId) {
      setDeleteConfirmId(sessionId);
      return;
    }

    const res = await fetch(`/api/sessions/${sessionId}`, {
      method: "DELETE",
    });

    if (res.ok) {
      setDeleteConfirmId(null);
      await fetchSessions();
      if (pathname === `/chat/${sessionId}`) {
        router.push("/chat");
      }
    }
  };

  const currentSessionId = pathname.startsWith("/chat/")
    ? pathname.split("/chat/")[1]
    : null;

  return (
    <>
      <aside
        className={`w-[300px] flex-shrink-0 flex flex-col h-full bg-[#111827] border-r border-[#1e2d3d] ${
          isOpen ? "flex" : "hidden md:flex"
        }`}
      >
        {/* Logo */}
        <div className="px-5 pt-5 pb-4">
          <h1 className="font-playfair text-[20px] font-semibold text-white">
            LuxeVenue<span className="text-[#c9a84c]">.ai</span>
          </h1>
        </div>

        {/* New Conversation button */}
        <div className="mx-4 mb-5">
          <button
            onClick={handleNewConversation}
            className="w-full px-4 py-2.5 rounded-lg border border-[#2a3a50] bg-transparent text-white text-sm flex items-center justify-between hover:bg-[#161e2e] transition-colors"
          >
            <span>New Conversation</span>
            <Plus size={16} className="opacity-70" />
          </button>
        </div>

        {/* Recent label */}
        {sessions.length > 0 && (
          <p className="px-5 mb-2 text-[10px] tracking-[0.2em] uppercase text-[#4b5563] font-medium">
            Recent
          </p>
        )}

        {/* Session list */}
        <div className="flex-1 overflow-y-auto px-2">
          {sessions.map((session) => {
            const isActive = currentSessionId === session.id;
            const isConfirming = deleteConfirmId === session.id;

            return (
              <div
                key={session.id}
                className={`flex items-center gap-2 px-3 py-2 rounded-lg text-[13px] cursor-pointer group relative transition-colors ${
                  isActive
                    ? "bg-[#161e2e] text-[#e8eaf0]"
                    : "text-[#8892a4] hover:bg-[#161e2e] hover:text-[#e8eaf0]"
                }`}
                onClick={() => {
                  setDeleteConfirmId(null);
                  router.push(`/chat/${session.id}`);
                  onClose?.();
                }}
              >
                <MessageSquare
                  size={14}
                  className="flex-shrink-0 opacity-60"
                />
                <span className="truncate flex-1 text-left">
                  {session.title}
                </span>

                {/* Delete button */}
                <button
                  className={`hidden group-hover:flex w-4 h-4 items-center justify-center flex-shrink-0 transition-colors ${
                    isConfirming
                      ? "text-red-400"
                      : "text-[#6b7280] hover:text-red-400"
                  }`}
                  onClick={(e) => {
                    e.stopPropagation();
                    handleDeleteSession(session.id);
                  }}
                  title={isConfirming ? "Click again to confirm delete" : "Delete conversation"}
                >
                  <Trash2 size={13} />
                </button>
              </div>
            );
          })}
        </div>

        {/* Bottom nav */}
        <div className="border-t border-[#1e2d3d] px-2 py-3">
          <button className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-[13px] text-[#6b7280] hover:bg-[#161e2e] hover:text-[#e8eaf0] cursor-pointer transition-colors">
            <Settings size={14} />
            Settings
          </button>
          <div ref={profileMenuRef} className="relative">
            {showProfileMenu && (
              <div className="mb-1 rounded-lg border border-[#1e2d3d] bg-[#0d1117] overflow-hidden">
                <div className="px-3 py-2.5 border-b border-[#1e2d3d]">
                  <p className="text-[12px] text-[#e8eaf0] font-medium truncate">
                    {session?.user?.name}
                  </p>
                  <p className="text-[11px] text-[#4b5563] truncate">
                    {session?.user?.email}
                  </p>
                </div>
                <button
                  onClick={() => signOut({ callbackUrl: "/login" })}
                  className="w-full text-left px-3 py-2 text-[12px] text-red-400 hover:bg-[#161e2e] transition-colors flex items-center gap-2"
                >
                  <LogOut size={12} />
                  Sign out
                </button>
              </div>
            )}
            <button
              onClick={() => setShowProfileMenu((v) => !v)}
              className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-[13px] text-[#6b7280] hover:bg-[#161e2e] hover:text-[#e8eaf0] cursor-pointer transition-colors"
            >
              <User size={14} />
              Profile
            </button>
          </div>
        </div>
      </aside>

      {/* Session limit modal */}
      <SessionLimitModal
        open={showLimitModal}
        onClose={() => setShowLimitModal(false)}
      />
    </>
  );
}
