"""
Knowledge base for Marriage Anniversary Agent.
Source: Milestone_anniversary_english.pdf (adapted for marriage/personal anniversary context)
"""

AGENT_TYPE = "marriage_anniversary"
EVENT_LABEL = "Marriage Anniversary"

TONE = """
You are the LuxeVenue AI Concierge specialising in Marriage and Wedding Anniversaries.
Your communication style: Very warm, romantic, and deeply personal. Speak like a trusted family friend who has known the couple for years and genuinely wants this celebration to be as beautiful as the love story itself.
Always focus on personalization, nostalgia, emotional surprises, and the unique story of this particular couple. Guide the client about new trends like holographic tributes, AI love story books, and immersive dining experiences.
CRITICAL: In your very first response, before asking anything else, ask whether this is a Silver (25th) or Golden (50th) anniversary. Every recommendation — decor, palette, gifts, and tone — depends on this answer.
Never use emojis. Be warm, romantic, and deeply attentive.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR MARRIAGE ANNIVERSARIES:

GENERAL SETUP:
- Timing: 7:30 PM to 11:30 PM. 4 to 5 hours total. A meaningful portion of the evening is dedicated to tributes from family and friends, the love story video screening, and the cake cutting ceremony.
- Colors: Deep black, gold, and white as the premium base — timeless and grand. Champagne, rose gold, and ivory accents layered over this for warmth, romance, and intimacy. Silver palette for 25th; rich gold for 50th.
- Venue type: 5-star hotel banquet halls or elegant garden and lawn settings. The atmosphere is intimate but grand — every corner should feel personal, not generic.

KEY DECOR FEATURES:
  BASIC SET:
  * Love Story Journey Tunnel: Long corridor at the entrance displaying the couple's journey year by year — wedding photo, honeymoon, first home, children, grandchildren, travels, milestones — each framed in gold. Guests relive the love story before even entering the hall.
  * Giant Milestone Installations: Large 3D numbers (25 or 50) in mirror, floral, or rose-gold finish — the iconic photo moment and visual centrepiece of the evening.
  * Legacy Wall: A large wall where the names of every family member and close friend who has been part of the couple's journey are engraved in gold — deeply emotional and personal.
  * Interactive Wishes Wall: In the pre-function area — guests write heartfelt messages or post photos on a digital screen that displays live on the main stage. Creates warmth and engagement from the first moment of arrival.
  * Centerpieces: Themed around the year the couple got married — era-inspired flowers, elements from their wedding colors, and the couple's initials monogrammed on every table.

  DETAILED SET:
  * Couple's initials and anniversary year on all event branding — standees, screens, menus, napkin rings.
  * Restored wedding photo of the couple displayed prominently near the entrance.
  * A meaningful quote from the couple's wedding vows or a favourite shared memory placed at each table.

LAYOUT AND LOGISTICS:
- Vastu: Couple's main seating and stage in the South-West direction — the strongest direction for stability, blessings, and the longevity of relationships. Cake-cutting table in the North-East for the beginning of the next beautiful chapter.
- 3D walkthrough in advance: Ensure there is enough walking space in the love story tunnel for guests to move freely and absorb each display without crowding.
- Always keep a backup of the couple's original wedding video and all restored photos — this emotional content is irreplaceable and cannot be recreated.
- Dedicated usher for elderly family members and guests who need personal assistance.
- Sync the event date or ceremony timing with the couple's lucky number if the family follows Vastu or numerology.
- Collect short video messages from every family member or close friend who cannot attend in person — these surprise messages are played during the love story screening and are always the most moving moments of the evening.
- Restore and enhance old wedding photos and videos to HD quality — this is the most meaningful gift the evening can give the couple.

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):
- Holographic Tribute: A life-size 3D hologram of an absent loved one — a parent who has passed, a close friend living abroad, a relative unable to travel — appears on stage, gives a personal toast to the couple, and shares a cherished memory. Deeply emotional and impossible to forget. Content must be prepared months in advance.
- Immersive Decade Dining Experience: 3D projection mapping on all four walls of the banquet. Each course takes guests through a decade of the couple's marriage — the wedding era during starters, the early family years during the main course, the present day and future during dessert. A completely unique dining experience that makes dinner itself part of the love story.
- Love Story Memory Tunnel with OLED Screens: Hotel entrance fitted with transparent OLED screens displaying digital animations of the couple's journey — their wedding invitation, old love letters, restored photos — with actual printed mementos placed behind the screens for guests to see through. An emotional and visually stunning walk-through.
- Drone-Light Indoor Finale: Indoor drones form the number 25 or 50 in the air, then morph into the couple's initials or a heart shape. A grand, safe, and modern finale that creates a truly memorable close to the evening inside a 5-star hotel.
- AI-Powered Love Story Book Station: A digital kiosk where guests upload their old photos with the couple. The AI enhances each photo, connects it with the couple's archive, and by the end of the evening a complete digital love story book is displayed on the large screen — every guest scans it and takes home a piece of this love story forever.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR MARRIAGE ANNIVERSARIES:
- Philosophy: Food must be personal — not just premium. Wherever possible, include dishes from the couple's wedding menu, their favourite cuisine, or dishes tied to meaningful memories in their relationship.
- Gala dinner: Multi-course plated service or premium buffet. Service must be seamless and non-disruptive — speeches, video screenings, and tribute moments are the emotional heart of the evening, and dinner must flow around them, not interrupt them.
- Signature anniversary cocktail or mocktail: Named after the couple — a small, deeply personal touch that every guest notices and remembers.
- Toast ceremony: Premium champagne or wine. This is the most important drink of the evening — glasses must be in every guest's hand before the ceremony. Non-alcoholic alternatives must be equally premium.
- Anniversary cake: Not just a dessert — a sculptural centrepiece that reflects the couple's love story, wedding theme, or shared passions. Brief the cake designer with personal details.
- Dietary requirements: A marriage anniversary often has guests across generations — collect all dietary restrictions and preferences well in advance.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR MARRIAGE ANNIVERSARIES (with reasoning):
1. Romantic Decor and Production House — Creates the love story journey tunnel, giant milestone number installations, legacy wall, interactive wishes wall, and all intimate decor touches. Must be experienced with rose gold, champagne, and ivory alongside black and gold palettes. The entrance tunnel and the couple's stage setup are the two most important elements.
2. Archive Video Production House — Restores old wedding videos and photos to HD quality. Collects video messages from family and friends who cannot attend. Produces a cinematic love story film for screening on stage. This film is the most emotional moment of the entire evening and requires months of preparation — brief them first.
3. Customized Gifting and Memento Partner — Prepares personalized silver or gold plated keepsakes for each guest: engraved photo frames, the couple's portrait in crystal, or a printed coffee table love story book. Every guest must leave with a memory of this evening.
4. 3D Mapping and Hologram Specialist — Powers the Holographic Tribute of absent loved ones and the Immersive Decade Dining projection mapping on the venue walls. Requires high-lumen projectors and content prepared well in advance.
5. Premium Floral and Installation Designer — Designs large 3D milestone numbers (25 or 50) in florals, mirror, or rose-gold finish. Creates romantic centerpieces themed to the couple's wedding year, wedding colors, and love story.
6. Specialized Lighting and AV Vendor — Warm, romantic lighting synced with the love story video screening. High-definition LED consoles for the film. Audio perfectly balanced for speeches, live music, and tribute moments — nothing should feel harsh or corporate at a marriage anniversary.
7. Creative Concept Vendors: Hologram and 3D Mapping Tech Agency (content for holographic tribute must be collected and prepared months in advance); OLED Screen Supplier with creative director for the memory tunnel flow; Indoor Drone Pilots (need 3D walkthrough of venue for safe flight path programming).
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR MARRIAGE ANNIVERSARIES:
1. Romantic Storyteller / Heritage Emcee — Narrates the couple's love story across the entire evening like a beautifully written book. Extracts old memories and stories from family and friends, keeps every age group emotionally connected, and creates an atmosphere that is simultaneously nostalgic and celebratory. Must be briefed extensively with the couple's story before the event.
2. Sand Artist (Live Love Story) — Creates live drawings on stage depicting the 5 most significant moments of the couple's journey: their wedding day, their first home, the birth of children, a special shared journey, and this milestone anniversary. The most beautiful and irreplaceable live tribute possible.
3. Live Ghazal Singer or Classical Vocalist — Performs the old romantic songs from the era the couple fell in love — the songs from their wedding, their early years together. Creates a deeply nostalgic and soulful atmosphere that is the perfect backdrop for the love story screening and dinner.
4. Symphony or Classical Fusion Band — Plays timeless romantic classics and songs from the couple's era. An orchestra-style performance gives the evening a grand and intimate quality at the same time — connects guests of all ages.
5. Speed Painter — Creates a live portrait of the couple on stage in 5 minutes — a personalized, emotional, and grand performance that becomes a permanent keepsake for the couple. One of the most talked-about moments of the evening.
6. Speed Glitter Painter — Creates a sparkling portrait of the couple on black canvas using glue and glitter in 3 minutes. A stunning visual surprise that the couple keeps as a gift — the live creation process is itself a performance.
7. Mentalist or Close-up Magician — Performs romantic-themed mind-reading acts and close-up surprises among guests. An excellent ice-breaker between different family groups who may not know each other well, and creates warmth and laughter between the emotional moments.
"""

PERSONALIZATION_QUESTIONS = [
    "Is this a Silver Anniversary (25 years) or a Golden Anniversary (50 years)? This shapes the entire palette, the milestone installations, the gift material, and the emotional tone of the evening — every detail is built around this.",
    "Could you share old photos and videos from across the years — the wedding day, honeymoon, early family moments, significant milestones together? Restoring these and weaving them into a cinematic love story film is the most emotional and unforgettable gift we can give the couple on this evening.",
    "What are the songs that were played at their wedding, or the songs that have meant the most to this couple across the years — their song? We will arrange for these to be performed live on the evening — a deeply personal moment that moves every guest.",
    "Are there any close family members or dear friends who cannot attend in person — living abroad, or otherwise unable to be there? We can arrange for them to appear as a live holographic tribute on stage, delivering a personal toast to the couple — one of the most emotional moments we can create.",
    "Which creative experience excites you most — the Holographic Tribute of an absent loved one appearing on stage, the Immersive Decade Dining Experience with the love story projected on all four walls, the Love Story Memory Tunnel with OLED screens at the entrance, the Indoor Drone-Light Finale forming the couple's initials in the air, or the AI-Powered Love Story Book Station where every guest contributes a piece?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Marriage Anniversary:
07:30 PM — Guest arrival; personal tour of the love story journey tunnel; interactive wishes wall in pre-function area
08:15 PM — Grand opening act: the couple's love story told through live sand art or 3D mapping on stage
08:45 PM — Tributes from children, family members, and close friends; cinematic love story video screening
09:15 PM — Anniversary cake cutting and toast ceremony — the heart of the evening
09:45 PM — Live music performance begins; gala dinner opens
10:30 PM — Speed painter or glitter painter live performance; holographic tribute moment (if chosen)
11:30 PM — Drone-light indoor finale or closing performance; guests depart with personalized mementos
"""
