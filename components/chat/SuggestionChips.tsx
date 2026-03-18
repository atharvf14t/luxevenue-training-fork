"use client";

interface SuggestionChipsProps {
  chips: string[];
  onChipClick: (text: string) => void;
}

export function SuggestionChips({ chips, onChipClick }: SuggestionChipsProps) {
  return (
    <div className="flex gap-2 flex-wrap mt-3">
      {chips.map((chip, i) => (
        <button
          key={i}
          onClick={() => onChipClick(chip)}
          className="px-3 py-1.5 rounded-full text-xs text-[#e8eaf0] bg-[#131c2e] border border-[#1e2d40] hover:border-[#2a3a50] hover:bg-[#1a2640] transition-all whitespace-nowrap"
        >
          {chip}
        </button>
      ))}
    </div>
  );
}
