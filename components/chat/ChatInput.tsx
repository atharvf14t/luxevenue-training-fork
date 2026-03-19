"use client";

import React, { useRef, useState, useEffect, useCallback } from "react";
import { Mic, ArrowRight } from "lucide-react";

interface ChatInputProps {
  onSend: (message: string, file?: File) => void;
  disabled?: boolean;
}

declare global {
  interface Window {
    SpeechRecognition?: new () => SpeechRecognition;
    webkitSpeechRecognition?: new () => SpeechRecognition;
  }
}

export function ChatInput({ onSend, disabled = false }: ChatInputProps) {
  const [value, setValue] = useState("");
  const [isRecording, setIsRecording] = useState(false);
  const [supportsSpeech, setSupportsSpeech] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const recognitionRef = useRef<SpeechRecognition | null>(null);

  useEffect(() => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    setSupportsSpeech(!!SpeechRecognition);
  }, []);

  // Auto-resize textarea
  useEffect(() => {
    const textarea = textareaRef.current;
    if (!textarea) return;
    textarea.style.height = "auto";
    textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`;
  }, [value]);

  const handleSend = useCallback(() => {
    const trimmed = value.trim();
    if (!trimmed || disabled) return;
    onSend(trimmed);
    setValue("");
    if (textareaRef.current) {
      textareaRef.current.style.height = "auto";
    }
  }, [value, disabled, onSend]);

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  };

  const handleMicClick = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) return;

    if (isRecording) {
      recognitionRef.current?.stop();
      setIsRecording(false);
      return;
    }

    const recognition = new SpeechRecognition();
    recognition.lang = "en-IN";
    recognition.continuous = false;
    recognition.interimResults = false;

    recognition.onresult = (e: SpeechRecognitionEvent) => {
      const transcript = e.results[0][0].transcript;
      setValue((prev) => (prev ? `${prev} ${transcript}` : transcript));
    };

    recognition.onend = () => setIsRecording(false);
    recognition.onerror = () => setIsRecording(false);

    recognition.start();
    recognitionRef.current = recognition;
    setIsRecording(true);
  };


  const hasText = value.trim().length > 0;

  return (
    <div className="flex-shrink-0 px-4 md:px-6 pb-4 pt-2">

      {/* Input box */}
      <div className="rounded-2xl bg-[#161e2e] border border-[#2a3a50] px-3 py-2.5 flex items-end gap-2 focus-within:border-[#3a4a60] transition-colors">
        {/* Textarea */}
        <textarea
          ref={textareaRef}
          value={value}
          onChange={(e) => setValue(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Ask the AI Concierge about venues, planning, or hospitality..."
          rows={1}
          className="flex-1 bg-transparent resize-none text-[#e8eaf0] placeholder-[#4b5563] italic text-sm outline-none py-0.5 leading-relaxed min-h-[22px] max-h-[120px]"
        />

        {/* Mic button */}
        {supportsSpeech && (
          <button
            onClick={handleMicClick}
            className={`w-7 h-7 rounded-full flex items-center justify-center transition-colors flex-shrink-0 mb-0.5 relative ${
              isRecording
                ? "text-red-400 ring-2 ring-red-500 ring-offset-1 ring-offset-[#161e2e] animate-pulse"
                : "text-[#6b7280] hover:text-[#e8eaf0]"
            }`}
            title={isRecording ? "Stop recording" : "Voice input"}
          >
            <Mic size={14} />
          </button>
        )}

        {/* Send button */}
        <button
          onClick={handleSend}
          disabled={!hasText || disabled}
          className={`w-7 h-7 rounded-full flex items-center justify-center flex-shrink-0 mb-0.5 transition-colors ${
            hasText && !disabled
              ? "bg-[#c9a84c] text-black cursor-pointer hover:bg-[#d4b86a]"
              : "bg-[#1e2d40] text-[#374151] cursor-not-allowed"
          }`}
        >
          <ArrowRight size={14} />
        </button>
      </div>

      {/* Disclaimer */}
      <p className="text-center text-[10px] text-[#374151] mt-2 px-4">
        The AI Concierge provides tailored guidance. Information may improve over time.
      </p>
    </div>
  );
}
