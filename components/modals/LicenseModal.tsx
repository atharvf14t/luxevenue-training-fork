"use client";

import * as Dialog from "@radix-ui/react-dialog";
import * as Tabs from "@radix-ui/react-tabs";
import { X } from "lucide-react";

interface LicenseModalProps {
  open: boolean;
  onClose: () => void;
}

const licenses = {
  IPRS: [
    { type: "5-star indoor non-ticketed", fee: "₹60,000/event" },
    { type: "4-star indoor", fee: "₹40,000/event" },
    { type: "Other venue non-ticketed (indoor/outdoor)", fee: "₹1,50,000/event" },
    { type: "Shopping mall indoor", fee: "₹40,000/event" },
    { type: "Non-ticketed sponsored", fee: "₹3,00,000/event" },
    { type: "Telecast Hindi channel", fee: "₹15,00,000/event" },
    { type: "Telecast non-Hindi", fee: "₹10,00,000/event" },
    { type: "Ticketed events", fee: "3% of ticket + sponsorship (min ₹75K indoor / ₹1.5L outdoor)" },
  ],
  PPL: [
    { type: "5-star hotel (area-based)", fee: "₹1,00,000 – ₹2,00,000/year" },
    { type: "Other venues", fee: "As assessed by PPL" },
    { type: "Note", fee: "Annual license covers background music playback" },
  ],
  ISAMRA: [
    { type: "Base rate", fee: "₹3,650 – ₹5,000/year" },
    { type: "Scales with", fee: "Number of rooms, outlets, and event spaces" },
    { type: "Hotels", fee: "Per property, annual basis" },
  ],
  Novex: [
    { type: "Per label", fee: "Varies by label and catalogue" },
    { type: "5-star hotels", fee: "Typically negotiate annual blanket deals" },
    { type: "Events", fee: "Case by case, contact Novex directly" },
    { type: "Note", fee: "Separate from IPRS — covers different sound recordings" },
  ],
};

export function LicenseModal({ open, onClose }: LicenseModalProps) {
  return (
    <Dialog.Root open={open} onOpenChange={(o) => !o && onClose()}>
      <Dialog.Portal>
        <Dialog.Overlay className="fixed inset-0 bg-black/60 backdrop-blur-sm z-40" />
        <Dialog.Content className="fixed left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 z-50 w-full max-w-lg rounded-2xl border border-[#1e2d3d] bg-[#111827] p-6 shadow-2xl max-h-[80vh] overflow-y-auto">
          <div className="flex items-start justify-between mb-2">
            <Dialog.Title className="font-playfair text-lg font-semibold text-white">
              Music License Fees
            </Dialog.Title>
            <button onClick={onClose} className="text-[#6b7280] hover:text-[#e8eaf0]">
              <X size={18} />
            </button>
          </div>
          <p className="text-xs text-[#6b7280] mb-4">
            Clients arrange these licenses themselves. LuxeVenue provides information and can help coordinate.
          </p>

          <Tabs.Root defaultValue="IPRS">
            <Tabs.List className="flex gap-1 mb-4 bg-[#131c2e] rounded-lg p-1">
              {(["IPRS", "PPL", "ISAMRA", "Novex"] as const).map((tab) => (
                <Tabs.Trigger
                  key={tab}
                  value={tab}
                  className="flex-1 px-3 py-1.5 rounded-md text-xs font-medium text-[#6b7280] data-[state=active]:bg-[#1e2d40] data-[state=active]:text-[#e8eaf0] transition-colors"
                >
                  {tab}
                </Tabs.Trigger>
              ))}
            </Tabs.List>

            {(["IPRS", "PPL", "ISAMRA", "Novex"] as const).map((tab) => (
              <Tabs.Content key={tab} value={tab}>
                <div className="space-y-2">
                  {licenses[tab].map((row, i) => (
                    <div
                      key={i}
                      className="flex justify-between gap-4 rounded-lg bg-[#131c2e] px-3 py-2.5"
                    >
                      <span className="text-xs text-[#8892a4] flex-1">{row.type}</span>
                      <span className="text-xs text-[#c9a84c] font-medium text-right flex-shrink-0">
                        {row.fee}
                      </span>
                    </div>
                  ))}
                </div>
              </Tabs.Content>
            ))}
          </Tabs.Root>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
