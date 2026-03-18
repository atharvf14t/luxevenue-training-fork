export type Language = 'en' | 'hi' | 'hinglish';

export function detectLanguage(text: string): Language {
  const devanagari = /[\u0900-\u097F]/;
  const latin = /[a-zA-Z]/;
  const hasDevanagari = devanagari.test(text);
  const hasLatin = latin.test(text);
  if (hasDevanagari && hasLatin) return 'hinglish';
  if (hasDevanagari) return 'hi';
  return 'en';
}
