"use client";

import { ChatSidebar } from "@/components/chat/ChatSidebar";
import { SidebarProvider, useSidebar } from "@/components/chat/SidebarContext";

function ChatLayoutInner({ children }: { children: React.ReactNode }) {
  const { isOpen, close } = useSidebar();

  return (
    <div className="flex h-screen w-screen overflow-hidden">
      {/* Mobile sidebar overlay */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/60 z-30 md:hidden"
          onClick={close}
        />
      )}

      {/* Sidebar — always visible on desktop, overlay on mobile */}
      <div
        className={`${
          isOpen ? "fixed inset-y-0 left-0 z-40" : "hidden"
        } md:relative md:flex md:flex-shrink-0 md:z-auto md:!flex`}
      >
        <ChatSidebar isOpen={isOpen} onClose={close} />
      </div>

      {/* Main content */}
      <main className="flex-1 flex flex-col h-full overflow-hidden min-w-0">
        {children}
      </main>
    </div>
  );
}

export default function ChatLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <SidebarProvider>
      <ChatLayoutInner>{children}</ChatLayoutInner>
    </SidebarProvider>
  );
}
