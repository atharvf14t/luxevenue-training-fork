"use client";

import * as Dialog from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import { useState } from "react";

interface BudgetPanelProps {
  open: boolean;
  onClose: () => void;
}

const categories = [
  { key: "venue", label: "Venue Booking", pct: 35 },
  { key: "decor", label: "Decor & Fabrication", pct: 20 },
  { key: "catering", label: "Catering & F&B", pct: 25 },
  { key: "entertainment", label: "Entertainment & Artists", pct: 10 },
  { key: "photography", label: "Photography & Video", pct: 5 },
  { key: "logistics", label: "Logistics & Misc", pct: 5 },
];

export function BudgetPanel({ open, onClose }: BudgetPanelProps) {
  const [budget, setBudget] = useState(2000000);
  const [guests, setGuests] = useState(300);

  const formatInr = (n: number) => {
    if (n >= 10000000) return `₹${(n / 10000000).toFixed(1)}Cr`;
    if (n >= 100000) return `₹${(n / 100000).toFixed(1)}L`;
    return `₹${n.toLocaleString("en-IN")}`;
  };

  const perHead = Math.round(budget / guests);

  return (
    <Dialog.Root open={open} onOpenChange={(o) => !o && onClose()}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-md rounded-2xl border border-[#1e2d3d] bg-[#111827] p-6 shadow-2xl">
          <div className="flex items-start justify-between mb-5">
            <Dialog.Title className="font-playfair text-lg font-semibold text-white">
              Budget Breakdown
            </Dialog.Title>
            <button onClick={onClose} className="text-[#6b7280] hover:text-[#e8eaf0]">
              <X size={18} />
            </button>
          </div>

          <div className="grid grid-cols-2 gap-3 mb-5">
            <div>
              <label className="text-xs text-[#6b7280] mb-1 block">Total budget (₹)</label>
              <input
                type="number"
                value={budget}
                onChange={(e) => setBudget(Number(e.target.value))}
                step={100000}
                className="w-full rounded-lg border border-[#2a3a50] bg-[#161e2e] px-3 py-2 text-sm text-[#e8eaf0] outline-none"
              />
            </div>
            <div>
              <label className="text-xs text-[#6b7280] mb-1 block">Guest count</label>
              <input
                type="number"
                value={guests}
                onChange={(e) => setGuests(Number(e.target.value))}
                min={1}
                className="w-full rounded-lg border border-[#2a3a50] bg-[#161e2e] px-3 py-2 text-sm text-[#e8eaf0] outline-none"
              />
            </div>
          </div>

          <div className="rounded-xl border border-[#1e2d3d] bg-[#131c2e] p-4 mb-4">
            <div className="flex justify-between text-xs text-[#6b7280] mb-3">
              <span>Total budget</span>
              <span className="text-[#c9a84c] font-semibold">{formatInr(budget)}</span>
            </div>
            <div className="space-y-2">
              {categories.map((c) => {
                const amount = Math.round((budget * c.pct) / 100);
                return (
                  <div key={c.key} className="flex items-center gap-3">
                    <div className="flex-1">
                      <div className="flex justify-between text-xs mb-0.5">
                        <span className="text-[#8892a4]">{c.label}</span>
                        <span className="text-[#e8eaf0]">{formatInr(amount)}</span>
                      </div>
                      <div className="h-1 bg-[#1e2d3d] rounded-full overflow-hidden">
                        <div
                          className="h-full bg-[#c9a84c] rounded-full opacity-70"
                          style={{ width: `${c.pct * 2.86}%` }}
                        />
                      </div>
                    </div>
                    <span className="text-[10px] text-[#4b5563] w-8 text-right">{c.pct}%</span>
                  </div>
                );
              })}
            </div>
          </div>

          <p className="text-xs text-[#6b7280]">
            Per head cost: <span className="text-[#c9a84c]">₹{perHead.toLocaleString("en-IN")}</span>
            {" · "}Indicative split. Adjust based on your priorities.
          </p>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
