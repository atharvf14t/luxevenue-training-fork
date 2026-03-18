"use client";

import * as Dialog from "@radix-ui/react-dialog";
import { X } from "lucide-react";

interface SessionLimitModalProps {
  open: boolean;
  onClose: () => void;
}

export function SessionLimitModal({ open, onClose }: SessionLimitModalProps) {
  return (
    <Dialog.Root open={open} onOpenChange={(o) => !o && onClose()}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-sm rounded-2xl border border-[#1e2d3d] bg-[#111827] p-6 shadow-2xl">
          <div className="flex items-start justify-between mb-4">
            <Dialog.Title className="font-playfair text-lg font-semibold text-white">
              Conversation Limit Reached
            </Dialog.Title>
            <button
              onClick={onClose}
              className="text-[#6b7280] hover:text-[#e8eaf0] transition-colors"
            >
              <X size={18} />
            </button>
          </div>

          <p className="text-sm text-[#8892a4] leading-relaxed mb-6">
            You&apos;ve reached the limit of{" "}
            <span className="text-[#c9a84c]">5 conversations</span>. Delete an
            existing conversation to start a new one.
          </p>

          <button
            onClick={onClose}
            className="w-full rounded-xl bg-[#161e2e] border border-[#2a3a50] px-4 py-2.5 text-sm text-[#e8eaf0] hover:bg-[#1e2d40] transition-colors"
          >
            Got it
          </button>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
