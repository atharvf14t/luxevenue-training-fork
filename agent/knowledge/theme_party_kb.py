"""
Knowledge base for Theme Party Agent.
Source: Theme_Parties.pdf
Covers: All themed party celebrations — Bollywood, Hollywood/Oscars, Great Gatsby/1920s,
Masquerade, Retro 70s/80s/90s, Space/Futuristic, Arabian Nights, Casino Royale, Under the Sea, and any custom theme.
"""

AGENT_TYPE = "theme_party"
EVENT_LABEL = "Theme Party"

TONE = """
You are the LuxeVenue AI Concierge specialising in Theme Parties.
Your communication style: Creative, imaginative, and theatrical. Speak like a visionary event director who can build an entire world inside a hotel banquet hall. Make the client feel like they are not just booking a party — they are commissioning an experience.
Always focus on total immersion — every detail from the entrance to the exit, from the food to the lighting to the costumes, must feel like it belongs to the chosen theme. Guide the client on new international trends like bio-responsive environments, mixed reality zones, and edible art galleries.
CRITICAL: In your very first response, ask what theme the client has in mind. The entire event — decor, lighting, food, music, entertainment, costumes — is built around this single answer.
Never use emojis. Be imaginative, confident, and precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR THEME PARTIES:

CONCEPT AND PHILOSOPHY:
- A theme party is a celebration built around a specific subject where every single detail — from the entrance tunnel to the table centerpieces, from the cocktail names to the music — reflects that theme. The goal is total immersion: guests should feel they have stepped out of the real world and into the theme's universe.
- Venue: 5-star hotel banquet halls with high ceilings (essential for aerial acts and kinetic sculptures), large open lawns, or premium indoor spaces that can be completely transformed by the decor team.
- Duration: 4 to 5 hours — enough time to explore, experience, eat, and be entertained within the theme.
- Colors, lighting, and atmosphere are entirely dictated by the chosen theme. Nothing in the room should contradict it.

POPULAR THEME SETUPS AND THEIR SIGNATURE ELEMENTS:

BOLLYWOOD THEME:
- Colors: Jewel tones — deep red, gold, turquoise, and magenta. Vibrant and opulent.
- Decor: Film reel installations, director's chair photo-ops, vintage Bollywood poster gallery, award statue centrepieces, red carpet entrance with velvet ropes.
- Atmosphere: Glamorous, dramatic, and celebratory — like an awards night meets a film set.

HOLLYWOOD / OSCARS THEME:
- Colors: Black, gold, and silver. Classic Hollywood glamour.
- Decor: Oscar trophy installations, Walk of Fame stars with guests' names on them, clapperboard props, large LED screens playing classic film scenes, red carpet and paparazzi photo wall.
- Atmosphere: Elegant, prestigious, black-tie with a touch of theatricality.

GREAT GATSBY / 1920s THEME:
- Colors: Black, gold, champagne, and ivory. Art Deco patterns and feather accents.
- Decor: Art Deco archways, feather and pearl centrepieces, vintage gramophone props, large Gatsby-era backdrops, gold and black geometric patterns throughout.
- Atmosphere: Opulent, mysterious, and intoxicatingly glamorous. Character actors speak in 1920s style among guests.

MASQUERADE THEME:
- Colors: Deep black, red, gold, and purple. Rich, mysterious, and theatrical.
- Decor: Oversized masquerade masks as wall art and table centrepieces, baroque-style chandeliers, velvet draping, candelabras, dramatic arched entrances.
- Atmosphere: Mysterious, theatrical, and seductive. Guests receive masks upon arrival.

RETRO 70s / 80s / 90s THEME:
- Colors: Era-specific — warm oranges/browns for 70s, neon pinks/blues for 80s, bright primary colors for 90s.
- Decor: Vintage posters, era-specific props (lava lamps for 70s, cassette tapes for 80s, CDs and gameboys for 90s), retro disco balls, vinyl record walls.
- Atmosphere: Energetic, nostalgic, and fun. Everyone arrives in era-specific costumes.

SPACE / FUTURISTIC THEME:
- Colors: Black, silver, electric blue, and neon purple. Dark and otherworldly.
- Decor: The entire hall is transformed into a spaceship — LED star-ceiling, planet sphere centrepieces, astronaut suit props, tunnel entrance with galaxy projection, metallic and holographic surfaces throughout.
- Atmosphere: Futuristic, awe-inspiring, and immersive. Feels like stepping into another dimension.

ARABIAN NIGHTS THEME:
- Colors: Deep jewel tones — emerald green, sapphire blue, ruby red, and gold. Rich and exotic.
- Decor: Large Moroccan lanterns, silk draping in jewel colors, low seating with cushions and hookah props, ornate arched doorways, lantern-lit pathways, incense and oud scent.
- Atmosphere: Exotic, mysterious, warm, and deeply sensory.

CASINO ROYALE THEME:
- Colors: Black, red, gold, and silver. Sleek and sophisticated.
- Decor: Casino game tables (roulette, blackjack, poker — non-gambling), large playing card installations, dice centrepieces, James Bond-style moody lighting, martini bar setup.
- Atmosphere: Suave, sophisticated, and thrillingly competitive.

UNDER THE SEA / OCEAN THEME:
- Colors: Deep blue, turquoise, seafoam green, and pearl white.
- Decor: 360-degree projection mapping of an underwater ocean on the walls, hanging jellyfish and fish installations from the ceiling, coral centerpieces, seashell and pearl table accents.
- Atmosphere: Dreamy, immersive, and magical. Feels like dining at the bottom of the ocean.

KEY DECOR ELEMENTS (ALL THEMES):
  BASIC SET:
  * Themed Entrance Tunnel: A full walk-through tunnel at the banquet entrance built by the concept decor team that immediately transports guests into the theme before they even enter the main hall.
  * 3D Props and Set Builds: Large-scale three-dimensional props specific to the theme that transform the hall from a venue into a world.
  * Themed Furniture: All standard hotel chairs and tables replaced or covered with furniture appropriate to the theme — velvet for Masquerade, chrome for Space, ornate for Arabian Nights.
  * Costume and Styling Station: A mini styling station at the venue entrance where guests are given a quick makeover — mask, accessory, costume element — before entering the event.

  DETAILED SET:
  * Full Lighting Transformation: Moody, colored, and laser lighting that makes the room feel like the theme rather than a hotel banquet hall. Lighting is the single most powerful tool in a theme party.
  * Character Actors Roaming: Immersive performers dressed as theme characters who do not stand on a stage but move among guests, interact with them, and make the theme feel real.
  * Themed Scent: A specific scent diffused throughout the venue matched to the theme — oud and incense for Arabian Nights, pine and cold air for Space, floral and powdery for Great Gatsby.
  * Special Effects: Fog machines, bubble machines, artificial snow, cold pyros, or UV reactive elements — all deployed to heighten the sensory immersion.

LAYOUT AND LOGISTICS:
- The entrance tunnel is non-negotiable — the first 30 seconds of a guest's arrival sets the entire mood. The tunnel is where the theme first becomes real.
- High ceilings are essential for aerial acts and kinetic sculptures — confirm ceiling height with the venue before booking these elements.
- 3D walkthrough in advance: Because theme party setups are complex and client-dependent, always show the client a 3D visualization or mood board of the transformed venue before execution. This also helps in closing the deal.
- Costume and styling station must be placed at or near the entrance — guests who arrive without a full costume must be given something to wear before entering.
- Stage placement: West or South-West direction — facing the audience in the East/North-East — considered auspicious for energy flow and crowd engagement.
- Special effects clearance: For fog machines, cold pyros, and smoke elements, always obtain fire-clearance from the hotel in advance.

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):
- Bio-Responsive Environment: A new international trend from the USA — the hall's lights and visuals change according to guests' movement or heart rate. When the dance floor is energetic, lights automatically become brighter and more vibrant. When the crowd slows, the atmosphere changes. The party literally responds to the people inside it.
- Mixed Reality Interactive Zone: Without heavy headsets, guests see digital theme characters and objects on their phones or specialized tablets that appear to exist physically in the hall. A Space theme might have digital astronauts walking among guests. A Gatsby theme might show digital flapper dancers. Turns the theme into a genuinely magical world.
- Edible Art and Molecular Gallery: A gallery area at the event where the art on the walls is made from actual food. Guests both admire it visually and can taste it. A completely unique concept that is a conversation piece for the entire evening. Liquid nitrogen desserts, UV-glowing cocktails, and edible sculptures.
- Kinetic Sculpture Centrepiece: A large central installation in the middle of the hall that slowly and continuously changes its shape throughout the evening. This blend of technology and art becomes the most photographed element of the party and remains the topic of conversation from arrival to departure.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR THEME PARTIES:
- Philosophy: In a theme party, the food is not a separate element — it is part of the theme. Every dish, every cocktail, and every piece of crockery must feel like it belongs to the world being created. Generic catering breaks the immersion.
- Themed menu naming: All cocktails and signature dishes are named after characters, places, or iconic elements of the theme. A Great Gatsby dinner has "Daisy's Delight" and "The Green Light Martini." A Bollywood event has dishes named after famous films.
- Themed plating: Food presentation and plating reflect the theme's colors and style. A Space theme uses dark plates with geometric presentation; an Under the Sea theme uses blue-tinted glassware and ocean-inspired garnishes.
- Signature cocktail bar: A full themed cocktail bar is essential. The bartenders are briefed on the theme and their cocktail names, glassware, and garnishes all reflect it.
- Molecular and edible art: The Gourmet Food Architects concept — liquid nitrogen desserts, glowing UV cocktails, edible installations, and interactive food stations that are performances as much as food service.
- Live counters: A live counter specific to the theme — a roast counter for a European theme, a sushi station for a Japanese theme, a chaat counter for Bollywood.
- Dietary requirements: Always collect in advance. Theme parties often have large, mixed guest lists.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR THEME PARTIES (with reasoning):
1. Concept Decor and Technical Production House — The soul of a theme party. These are not ordinary decorators — they build an entirely new world. Their job involves creating large 3D props, preparing the themed entrance tunnel, changing all the furniture, and transforming the hall from a venue into a universe. If the theme is Space, they build a spaceship. If it is Great Gatsby, they recreate 1920s New York. Brief them with mood boards and reference images as early as possible.
2. Professional AV and Lighting Specialist — Lighting is the single biggest factor in a theme party. This vendor runs moody and colored lighting, laser shows, and high-definition theme-related visuals and animations on LED walls. Their job is to synchronize sound and light with every moment of the theme — from the entrance tunnel to the climax of the evening. Without excellent lighting, even the best decor falls flat.
3. Themed Costume and Styling Partner — Arranges theme-appropriate clothes, masks, or accessories for guests. Sets up a mini styling station at the venue entrance where guests receive a quick makeover according to the theme before entering. Ensures that every guest, regardless of how much effort they made with their own costume, feels part of the theme from the moment they arrive.
4. Gourmet Food and Mixology Architects — Work with the hotel chef to create a menu where even the food feels like part of the theme. Signature cocktails named after theme characters, plating that reflects the theme's colors, live counters that fit the world being built. Moving beyond normal catering to edible art, liquid nitrogen desserts, and UV-glowing cocktails.
5. Special Effects and Atmospheric Team — Brings the air itself to life according to the theme. Fog machines for mystery (Masquerade, Space), bubble machines for whimsy (Under the Sea, 1920s), artificial snow for Christmas or fantasy themes, cold pyros for dramatic reveals, and theme-specific scent diffusion throughout the hall. Always requires fire-clearance from the hotel in advance.
6. AR and Tech Production House — Manages the Mixed Reality Interactive Zone, Bio-Responsive Environment sensors, and any projection mapping elements. Brief them with the exact theme and desired digital characters or environments months in advance.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR THEME PARTIES:
1. Character Actors and Immersive Performers — The most important artists in a theme party. These performers do not stand on a stage — they roam among guests, embodying theme characters completely. A Great Gatsby event has 1920s socialites engaging guests in period-appropriate conversation. A Masquerade has mysterious characters who speak in riddles. They are the biggest contributors to making the atmosphere feel genuinely real rather than just decorative.
2. Themed Musical Band or DJ — Performs only music that belongs to the theme's world. A jazz band for Great Gatsby or Masquerade. An electronic music producer with laser instruments for a Space or Futuristic theme. A Bollywood band for a Bollywood theme. A retro DJ for 70s/80s/90s nights. The music must never break from the theme — even transitions between acts stay within the theme's sonic world.
3. High-Energy Emcee or Narrator (In Character) — An anchor who plays a character within the theme rather than just hosting a party. They take guests forward through the evening via a storyline connected to the theme — every act, every performance, every transition is narrated as part of the theme's world. The best theme party emcees blur the line between host and performer.
4. 3D Digital Artist — Creates live digital paintings on a large LED screen, merging live photos of guests with the theme's characters and visual world. A Space theme digital artist places guests in spacesuits on the surface of the moon. A Bollywood theme artist puts guests on a film poster. Can instantly print these in digital frames as personalized guest gifts.
5. Aerial and Gravity-Defying Act — Performs stunning aerial stunts according to the theme, making full use of the high ceilings of 5-star hotel banquets. Flying angels for a Masquerade or fantasy theme, astronauts descending from the ceiling for a Space theme, acrobats in period costume for a Great Gatsby event. Leaves guests completely astonished and makes the party feel like a live production.
"""

PERSONALIZATION_QUESTIONS = [
    "What theme do you have in mind for this party? The entire event — from the entrance tunnel and decor to the food, cocktails, music, costumes, and performers — is built around your chosen theme, so this is the single most important decision we make together.",
    "Is this a corporate event, a personal celebration (birthday, anniversary, farewell), or a social gathering? The scale, formality, and entertainment style of a theme party change significantly based on the occasion it is marking — and both can be extraordinary.",
    "How adventurous would you like guests to be with costumes — full character costumes, a simple accessory or color code, or just a themed dress code? We can set up a full styling station at the entrance so every guest feels part of the theme from the moment they arrive, regardless of what they wore.",
    "Are there specific characters, eras, films, cultural references, or visual elements from your chosen theme that you want highlighted most prominently? The more specific and personal the theme's references, the more immersive and memorable the experience — generic themes are never as powerful as deeply specific ones.",
    "Which creative experience excites you most — the Bio-Responsive Environment where the lighting responds to guests' energy on the dance floor, the Mixed Reality Interactive Zone where digital theme characters appear in the room via phones, the Edible Art and Molecular Gallery where the food is also art, or the Kinetic Sculpture Centrepiece that continuously changes shape throughout the evening?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Theme Party:
05:00 PM — Full venue transformation complete; all 3D props, lighting, and special effects tested
06:30 PM — Costume and styling station ready at entrance; character actors in position
07:00 PM — Guests begin arriving; entrance tunnel experience begins
07:00 PM — Themed cocktail bar opens; character actors roaming and engaging guests
07:30 PM — Themed musical band or DJ begins; 3D digital artist station opens
08:00 PM — Emcee (in character) formally opens the event with themed narrative
08:30 PM — Gala dinner and themed food counters open fully
09:00 PM — Aerial act or gravity-defying performance — the first major entertainment peak
09:30 PM — Mixed Reality Interactive Zone and Kinetic Sculpture centrepiece revealed
10:00 PM — Bio-Responsive dance floor at peak energy; DJ or band builds to climax
10:30 PM — 3D digital artist creates grand collaborative theme artwork with guests' photos on main screen
11:00 PM — Special effects finale (cold pyros, bubble shower, or fog reveal depending on theme)
11:30 PM — Guests depart with personalized digital frame prints from the 3D digital artist
"""
