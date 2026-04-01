"""
Knowledge base for Milestone Birthday Agent.
Source: Milestone_birthday_english.pdf
"""

AGENT_TYPE = "milestone_birthday"
EVENT_LABEL = "Milestone Birthday"

TONE = """
You are the LuxeVenue AI Concierge specialising in Milestone Birthday celebrations.
Your communication style: Very warm, cheerful, and enthusiastic — speak like an old family member or close friend who genuinely wants to double every joy and make this birthday unforgettable.
Always focus on personalization, surprise elements, and deeply emotional experiences.
Guide the client on new digital trends like holographic toasts, bioluminescent themes, and AI-driven experiences.
CRITICAL: In your very first response, before asking anything else, ask which milestone birthday this is — the 1st, 18th, 50th, or 60th. Every recommendation depends on this answer.
Never use emojis. Be warm, heartfelt, and precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR MILESTONE BIRTHDAYS:

MILESTONE-SPECIFIC ATMOSPHERE:
- 1st Birthday: Cute, colorful, and pastel. Afternoon timing — 4:00 PM to 7:00 PM. Soft play areas, balloons, gentle lighting. Everything must be completely child-safe and parent-friendly.
- 18th Birthday: Energetic, trendy, and vibrant. Evening from 8:00 PM onwards. Neon lounge setup, high-tables, DJ setup. Young, lively crowd — the energy must match.
- 50th Birthday: Elegant and grand. Evening from 8:00 PM onwards. Deep black, gold, and white palette. Royal and classy setup with velvet lounge sofas and luxury finishes.
- 60th Birthday: Nostalgic and soulful. Evening from 8:00 PM onwards. Same royal palette. Always include a dedicated quiet seating zone for old friends — less noise, comfortable conversation, comfortable chairs.

GENERAL REQUIREMENTS (ALL MILESTONES):
- Venue type: 5-star hotel banquet halls or large lawns
- Duration: 4 to 5 hours — focused, emotional, and memorable
- The cake cutting ceremony is the main highlight of the entire event — everything builds toward it
- Colors: Deep black, gold, and white for 50th and 60th; bright pastels for 1st; neon accents for 18th

KEY DECOR FEATURES:
  BASIC SET:
  * Life-Size Photo Gallery: At the entrance — one special photo from each year of the birthday person's life displayed in gold frames. Guests relive the journey before even entering the hall.
  * Giant 3D Age Installation: Large 3D numbers (1, 18, 50, 60) in the middle of the hall — mirror or floral finish. Iconic photo moment and visual centrepiece.
  * Interactive Memory Wall: In the pre-function area — guests write messages by hand or post photos on a digital screen. Creates emotional engagement from the moment guests arrive.
  * Luxury Lounge Seating: Comfortable velvet sofas with customized cushions bearing the birthday person's initials.

  DETAILED SET:
  * Entrance Tunnel and Stage: Fabricated by the decor partner — defines the grand entry moment and the stage for cake cutting and performances.
  * Neon Lounge Zones (18th): High-tables, bar stools, and neon branding — creates a trendy, Instagram-worthy atmosphere.
  * Soft Play Areas (1st): Safe padded zones for toddlers and young children.

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):
- Human Claw Machine (1st or 18th Birthday): A large mechanical crane setup installed in the lawn or banquet. Guests are attached to the crane and lowered into a pit filled with toys, chocolates, and branded gifts — they grab as many as they can. Hugely popular in USA and Japan. A super-fun activity that becomes the most talked-about moment.
- Bioluminescent Garden Party (18th or 50th Birthday): For large hotel lawns — plants, pathways, furniture, and cocktails all glow in the dark using UV lighting and food-grade glowing elements. Creates a magical world like the Avatar movie — completely unlike any regular decor in India.
- AI-Driven Virtual Toast (50th or 60th Birthday): Absent friends or relatives who live abroad appear as life-size 3D holograms on stage. They raise a glass and give a personal toast — looks completely real. Brings old memories and relationships back through technology. Deeply emotional moment.
- Underwater Banquet Theme (any milestone): 360-degree high-definition projection mapping transforms the entire hall into an ocean. Digital fish and sharks swim around guests. The atmosphere changes with each course — takes hospitality to a completely new level.
- Time-Travel Elevator Experience (any milestone): The hotel elevator or a fake setup covered with digital screens shows a year-by-year journey (e.g., 1970 to 2026). Upon stepping out, the guest arrives at a party themed to that specific era. Very immersive and deeply emotional.

LAYOUT AND LOGISTICS:
- Vastu: Cake-cutting table should be in the East or North-East direction — considered auspicious for new beginnings and growth
- Always align the decor theme with the birthday person's lucky color if the family follows numerology
- 3D walkthrough in advance: Confirm the path between guest seating and the buffet is completely clear — no bottlenecks
- Grand entry with cold pyros or flower shower is non-negotiable — it is the most photographed moment of the night
- Always have a backup microphone — technical issues during the emcee's speech cannot happen
- Always have a backup cake — the cake is the centrepiece of the entire event; no last-minute surprises
- Each guest should receive a small sapling or eco-friendly gift upon leaving — represents longevity of life and leaves a lasting impression
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR MILESTONE BIRTHDAYS:
- 1st Birthday: Mini-sliders, child-friendly finger foods, and colorful bites for children. Full fine-dining service for adult guests. No alcohol — focus on premium mocktails and fresh juices.
- 18th Birthday: Trendy food stations, gourmet finger foods, a mix of street-style and fine-dining options. Mocktails and cocktails equally prominent. High-energy food that matches the party vibe.
- 50th Birthday: Premium fine-dining buffet with full service. Elaborate dessert spread. Signature cocktails and premium spirits.
- 60th Birthday: Warm, comfort-food-oriented fine-dining. Easy to eat for older guests. Premium service. Digestive-friendly options alongside the main spread.
- All milestones: A signature cocktail or mocktail named and designed around the birthday person's favorites is essential. Live nitrogen stations and molecular food counters elevate the experience. Fluorescent cocktails available for the Bioluminescent Garden Party concept.
- The cake is not just a dessert — it is an event in itself. The 3D cake designer creates it as a sculpture, not a regular cake.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR MILESTONE BIRTHDAYS (with reasoning):
1. Theme Decor and Production House — The foundation of the entire event. Customizes every element to the milestone: pastel soft-play zones for 1st, neon lounge for 18th, royal black-gold-white for 50th and 60th. Fabricates the entrance tunnel, stage, giant number installations, and all seating zones.
2. Specialized 3D Cake Designer — Creates life-size or gravity-defying 3D sculpture cakes depicting the birthday person's hobbies or life story (golf, travel, business, passions). This is not a regular cake — it is a statement piece and the centrepiece of the cake-cutting ceremony.
3. Professional AV and LED Screen Partner — Manages the surprise life journey film display on large HD LED consoles, synced with lighting changes for the grand entry and cake cutting impact. The emotional centrepiece of the evening.
4. Luxury Gifting and Hamper Vendor — Personalizes return gifts for each guest. 1st birthday: toys and soft items for children. 50th and 60th: personalized silver-plated utility items or luxury chocolates. Each gift serves as a lasting reminder of the milestone.
5. Gourmet Catering and Mixology Team — Full fine-dining service with signature cocktails built around the birthday person's favorites. Live nitrogen stations, molecular food counters, and fluorescent cocktails for themed concepts.
6. Creative Concept Vendors (based on chosen experience):
   - Mechanical and Robotics Engineers: For the Human Claw Machine — ensures safety, weight-bearing, and smooth mechanical operation
   - AR/VR and Projection Mapping Experts: For the Underwater Banquet Theme or AI-Driven Holographic Toast — provides high-end projectors, motion sensors, and digital content design
   - Bio-Tech and Special Effects Lighting Team: For the Bioluminescent Party — manages UV lighting, food-grade glowing chemicals, and ensures complete guest safety
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR MILESTONE BIRTHDAYS:

MILESTONE-SPECIFIC PERFORMERS:
- 1st Birthday: Kids' entertainers — magicians, puppet shows, costumed characters. Everything must be gentle, colorful, and age-appropriate.
- 18th Birthday: Trendy DJ playing international EDM and Bollywood remixes. High energy from start to finish.
- 50th Birthday: Sufi band or Bollywood band — nostalgic hits that the birthday person and their peer group grew up with.
- 60th Birthday: Ghazal singer or Saxophone artist — soulful, timeless music that moves the heart without overpowering conversation.

ALL MILESTONE PERFORMERS:
1. High-Energy Anchor or Celebrity Emcee — The backbone of the evening. Keeps guests engaged, shares fun anecdotes about the birthday person, extracts old stories from friends and family, and makes the atmosphere simultaneously emotional and entertaining. Manages every age group in the room.
2. Mentalist or Close-up Magician — Performs mind-reading acts and close-up surprises among guests. An excellent ice-breaker that creates conversation between guests who do not know each other.
3. Professional Photographer and Cinematographer — Uses cinema-style cameras for movie-quality shooting. Not ordinary event videographers — every grand entry, emotion, and cake-cutting moment is captured cinematically.
4. Digital Caricaturist — Draws funny, personalized illustrations of guests on an iPad and instantly sends them to their phone. A major attraction at 18th and 50th birthday parties.
5. LED Laser Violinist — Plays violin with lasers creating light patterns across the entire hall in sync with the music. Best deployed for the birthday person's grand entry at the 18th or 50th.
6. Speed Sand Artist — Performs live on stage, drawing the 5 biggest moments of the birthday person's life through sand art: first day of school, marriage, first company, travel milestone, milestone birthday. Deeply moving and unique.
7. Celebrity Impressionist — Performs as the birthday person's favourite international or Bollywood celebrity, interacting with them directly. A personalized, surprising, and memorable moment.
"""

PERSONALIZATION_QUESTIONS = [
    "Which birthday milestone are we celebrating — the 1st, 18th, 50th, or 60th? Each milestone calls for a completely different atmosphere, music, decor, and experience — I want to make sure every single detail is crafted precisely for this occasion.",
    "What are the biggest highlights of the birthday person's life — their achievements, passions, favourite memories, and hobbies? These become the heart of the surprise film, the 3D cake design, and the sand artist's live on-stage performance.",
    "Could we gather old photos from each year of their life, and short video bites from close friends or family who cannot attend in person? The surprise life journey film is consistently the most emotional and talked-about moment of any milestone birthday.",
    "Does the family follow any lucky number, colour, or Vastu principles? We can position the cake-cutting table in the East or North-East direction and align the entire decor theme with their lucky colour — a detail that resonates deeply with many families.",
    "Which creative experience excites you most — the Human Claw Machine, the Bioluminescent Garden Party, the AI-Driven Virtual Toast with a life-size hologram of an absent loved one, the Underwater Banquet Theme, or the Time-Travel Elevator Experience?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Milestone Birthday (Evening Format):
07:30 PM — Guest arrival; welcome drinks and interactive memory wall experience in the pre-function area
08:15 PM — Birthday person's grand entry with special effects (cold pyros or flower shower)
08:45 PM — Surprise video screening: complete life journey from childhood to today
09:15 PM — Grand cake cutting ceremony and toast raised by all guests
09:45 PM — Live music performance begins; dinner buffet opens
11:00 PM — Personalized return gifts distributed; celebration wrap-up

NOTE FOR 1st BIRTHDAY (Afternoon Format):
04:00 PM — Guest arrival; children's entertainment begins
04:30 PM — Interactive play and kids' activities
05:30 PM — Cake cutting ceremony — the main highlight
06:00 PM — Snacks and dinner; more entertainment
07:00 PM — Return gifts; wrap-up
"""
