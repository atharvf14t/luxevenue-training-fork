"use client";

import * as Dialog from "@radix-ui/react-dialog";
import { X } from "lucide-react";
import { useState } from "react";

interface LiquorModalProps {
  open: boolean;
  onClose: () => void;
}

export function LiquorModal({ open, onClose }: LiquorModalProps) {
  const [guests, setGuests] = useState(100);
  const [eventType, setEventType] = useState<"social" | "corporate" | "wedding">("wedding");
  const [drinkType, setDrinkType] = useState<"spirits" | "beer" | "both">("both");

  const spiritRatio = eventType === "corporate" ? 4 : 3;
  const beerPerPerson = eventType === "corporate" ? 2.5 : 3.5;

  const spirits = drinkType !== "beer" ? Math.ceil(guests / spiritRatio) : 0;
  const beer = drinkType !== "spirits" ? Math.ceil(guests * beerPerPerson) : 0;

  return (
    <Dialog.Root open={open} onOpenChange={(o) => !o && onClose()}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-md rounded-2xl border border-[#1e2d3d] bg-[#111827] p-6 shadow-2xl">
          <div className="flex items-start justify-between mb-5">
            <Dialog.Title className="font-playfair text-lg font-semibold text-white">
              Liquor Calculator
            </Dialog.Title>
            <button onClick={onClose} className="text-[#6b7280] hover:text-[#e8eaf0]">
              <X size={18} />
            </button>
          </div>

          <div className="space-y-4 mb-5">
            <div>
              <label className="text-xs text-[#6b7280] mb-1 block">Guests drinking</label>
              <input
                type="number"
                value={guests}
                onChange={(e) => setGuests(Number(e.target.value))}
                min={1}
                className="w-full rounded-lg border border-[#2a3a50] bg-[#161e2e] px-3 py-2 text-sm text-[#e8eaf0] outline-none focus:border-[#3a4a60]"
              />
            </div>
            <div>
              <label className="text-xs text-[#6b7280] mb-1 block">Event type</label>
              <select
                value={eventType}
                onChange={(e) => setEventType(e.target.value as typeof eventType)}
                className="w-full rounded-lg border border-[#2a3a50] bg-[#161e2e] px-3 py-2 text-sm text-[#e8eaf0] outline-none focus:border-[#3a4a60]"
              >
                <option value="wedding">Wedding</option>
                <option value="social">Social Event</option>
                <option value="corporate">Corporate</option>
              </select>
            </div>
            <div>
              <label className="text-xs text-[#6b7280] mb-1 block">Drink type</label>
              <select
                value={drinkType}
                onChange={(e) => setDrinkType(e.target.value as typeof drinkType)}
                className="w-full rounded-lg border border-[#2a3a50] bg-[#161e2e] px-3 py-2 text-sm text-[#e8eaf0] outline-none focus:border-[#3a4a60]"
              >
                <option value="both">Both spirits & beer</option>
                <option value="spirits">Spirits only</option>
                <option value="beer">Beer only</option>
              </select>
            </div>
          </div>

          {/* Results */}
          <div className="rounded-xl border border-[#1e2d3d] bg-[#131c2e] p-4 space-y-2 mb-4">
            {spirits > 0 && (
              <div className="flex justify-between text-sm">
                <span className="text-[#8892a4]">Spirits (750ml bottles)</span>
                <span className="text-[#e8eaf0] font-semibold">{spirits}</span>
              </div>
            )}
            {beer > 0 && (
              <div className="flex justify-between text-sm">
                <span className="text-[#8892a4]">Beer (bottles/cans)</span>
                <span className="text-[#e8eaf0] font-semibold">{beer}</span>
              </div>
            )}
            <div className="border-t border-[#1e2d3d] pt-2 flex justify-between text-sm">
              <span className="text-[#c9a84c] font-medium">Total units</span>
              <span className="text-[#c9a84c] font-bold">{spirits + beer}</span>
            </div>
          </div>

          <p className="text-xs text-[#6b7280] italic">
            ✦ Through LuxeVenue, purchase at <span className="text-[#c9a84c]">10% off</span>. Ask your concierge for the liquor menu.
          </p>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
