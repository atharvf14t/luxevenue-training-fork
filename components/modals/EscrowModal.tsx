"use client";

import * as Dialog from "@radix-ui/react-dialog";
import { X } from "lucide-react";

interface EscrowModalProps {
  open: boolean;
  onClose: () => void;
}

const steps = [
  {
    step: "01",
    title: "Book Securely",
    desc: "Funds are held in a protected LuxeVenue Escrow account — neither you nor the vendor can access them until the event is confirmed.",
  },
  {
    step: "02",
    title: "Vendor Performs",
    desc: "The vendor delivers their service at your event as agreed. You verify and approve the deliverables.",
  },
  {
    step: "03",
    title: "Funds Released",
    desc: "Only after your approval, the funds are released to the vendor. Full protection throughout the process.",
  },
];

export function EscrowModal({ open, onClose }: EscrowModalProps) {
  return (
    <Dialog.Root open={open} onOpenChange={(o) => !o && onClose()}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-md rounded-2xl border border-[#1e2d3d] bg-[#111827] p-6 shadow-2xl">
          <div className="flex items-start justify-between mb-2">
            <Dialog.Title className="font-playfair text-lg font-semibold text-white">
              LuxeVenue Escrow
            </Dialog.Title>
            <button onClick={onClose} className="text-[#6b7280] hover:text-[#e8eaf0]">
              <X size={18} />
            </button>
          </div>
          <p className="text-xs text-[#6b7280] mb-6">
            Book with confidence — your money is protected until delivery.
          </p>

          <div className="space-y-4">
            {steps.map((s) => (
              <div key={s.step} className="flex gap-4">
                <span className="font-playfair text-2xl font-semibold text-[#c9a84c] flex-shrink-0 leading-tight">
                  {s.step}
                </span>
                <div>
                  <p className="text-sm font-semibold text-[#e8eaf0] mb-0.5">
                    {s.title}
                  </p>
                  <p className="text-xs text-[#6b7280] leading-relaxed">{s.desc}</p>
                </div>
              </div>
            ))}
          </div>

          <button
            onClick={onClose}
            className="mt-6 w-full rounded-xl bg-[#c9a84c] px-4 py-2.5 text-sm font-semibold text-black hover:bg-[#d4b86a] transition-colors"
          >
            Understood
          </button>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
