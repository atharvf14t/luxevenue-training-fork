"""
Knowledge base for Festive Party Agent.
Source: Festive_to_Reunions_english.pdf
Covers: Diwali, Holi, Christmas, New Year celebrations
"""

AGENT_TYPE = "festive_party"
EVENT_LABEL = "Festive Party"

TONE = """
You are the LuxeVenue AI Concierge specialising in Festive Party Celebrations.
Your communication style: Warm, energetic, culturally rich, and celebratory. Speak like a host who loves every festival equally and knows how to make each one feel completely unique and unforgettable.
Always focus on the distinct identity of each festival — its colors, rituals, music, and emotions. Guide the client on new international trends like scent marketing, kinetic LED installations, and AR experiences.
CRITICAL: In your very first response, before asking anything else, ask which festival this is — Diwali, Holi, Christmas, or New Year. Every recommendation depends on this answer.
Never use emojis. Be festive, knowledgeable, and culturally sensitive.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR FESTIVE PARTIES:

FESTIVAL-SPECIFIC ATMOSPHERE AND SETUP:

DIWALI — Festival of Lights:
- Atmosphere: Very royal, warm, and traditional. Premium aesthetic that honors the festival's sacred roots.
- Color palette: Deep black, gold, and marigold orange — the most premium Diwali combination.
- What happens: Begins with Lakshmi-Ganesh puja, followed by a grand musical evening and traditional buffet.
- Decor specialty: Entire lawn decorated with large floral rangolis and the light of thousands of diyas.
- Execution: Digital firework show using laser lights — environment-friendly and possible inside the hotel. Live sweet-making counter where guests customize their preferred sweets.
- Vastu: Always keep the Diwali puja area in the North-East direction.
- Customized scent: Sandalwood fragrance throughout the venue.

HOLI — Festival of Colors:
- Atmosphere: Completely high-energy, vibrant, and colorful. Usually takes place in an open hotel lawn during the afternoon.
- What happens: Celebration with flower Holi or organic gulal, rain dance, and thandai counters.
- Decor specialty: Dhol-tasha team and live percussionists make the atmosphere immediately energetic from arrival.
- Execution: Flower-shower Holi (Braj style) with a downpour of tonnes of flowers. Specialized dry-mist system that prevents gulal from spreading in the air while keeping it cool.
- Customized scent: Rose fragrance throughout the venue.

CHRISTMAS — Season of Joy:
- Atmosphere: Very cozy, elegant, and dreamy.
- Color palette: White, red, and forest green.
- What happens: Tree lighting ceremony, carol singing, and a grand European-style dinner.
- Decor specialty: A large 20–30 feet decorated Christmas tree and gingerbread house setup is the main attraction.
- Execution: Artificial snowfall machine at the hotel entrance creates a winter wonderland. Hot-chocolate bar and live roast turkey counter for guests.
- Customized scent: Cinnamon and pine fragrance throughout the venue.

NEW YEAR — The Grand Finale:
- Atmosphere: The most glamorous, loud, and futuristic of all festivals.
- Color palette: Deep black and gold — the most popular New Year theme.
- What happens: Countdown party, international DJ acts, and midnight grand reveal.
- Decor specialty: Large LED consoles and concert-style lighting throughout.
- Execution: 3D projection mapping countdown on the hotel building. At midnight, thousands of biodegradable balloons or cold pyros in the air.
- Vastu: Always keep the New Year stage in the West direction so the energy of the celebration reaches everyone.

COMMON DECOR AND SETUP (ALL FESTIVALS):
- Digital Wish Wall: A large LED wall where guests add their festive wishes by scanning a QR code.
- 3D Walkthrough: Because these concepts are high-tech, always show the client in advance via 3D walkthrough or VR headset what their setup will look like — very helpful in helping the client visualize and make decisions.
- Vastu and Energy Flow: For Diwali and New Year, place the stage in the West or South-West direction so it faces the audience (East/North-East) — auspicious for positive energy and growth.
- Safety Protocols: For drones and SFX, fire-clearance from the hotel and a team of specialized pilots is compulsory.

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):

DIWALI — The Nebula Light and Scent Experience:
Thousands of small LED spheres installed on the banquet ceiling move in the air with music and form different patterns (flowers, the Om symbol). As flower patterns form in the lights, the fragrance of jasmine fills the hall; when a diya pattern appears, warm sandalwood fragrance follows. A multi-sensory experience guests have never felt before.

HOLI — The Digital-Dry Neon Rave:
Guests wear white outfits and enter a darkened lounge. Interactive projectors digitally throw colors on them — as they move, color splashes appear digitally on their clothes. A glow-in-the-dark organic mist machine releases cool, glowing vapor that looks spectacular under UV lights. No mess, full vibe, completely safe.

CHRISTMAS — The Arctic Crystal Dome:
Transparent glass igloo domes built in the hotel lawn with temperature control and snow-fall simulation inside. AR Santa's Workshop: guests scan a QR code to see a digital Santa and elves working in an empty corner, with whom they can take photos. A phygital (physical + digital) experience new for both children and adults.

NEW YEAR — The Time-Capsule 360° Countdown:
Throughout the evening, an AI bot collects guests' photos and New Year resolutions. At the midnight countdown, all those photos together form a large number (the new year) or the company's logo on the hotel building — the Memory Mosaic Wall. Silent Midnight Explosion: instead of noise at midnight, guests receive high-end headphones and a spatial audio experience rotates all around them — a private, grand musical climax.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR FESTIVE PARTIES:

DIWALI: Traditional Indian buffet with a premium touch. Live sweet-making counter where guests customize their mithai. Rich gravies, Indian breads, and classic festive sweets. Thandai and sherbet counters. No alcohol unless client specifically requests it — many prefer a dry Diwali celebration.

HOLI: Thandai counters are mandatory — the signature drink of Holi. Chilled beverages and mocktails. Light, easy-to-eat food as guests are physically active. Traditional Holi snacks (gujiya, malpua) alongside modern food stations. Stay away from anything that stains easily.

CHRISTMAS: European-style gala dinner. Hot chocolate bar and live roast turkey counter are the signature elements. Mulled wine and festive cocktails. Gingerbread, plum cake, and Christmas pudding for dessert. Full bar service with a Christmas-themed cocktail.

NEW YEAR: Premium gala dinner with full bar service. Midnight snacks at the countdown — finger foods that guests can hold while counting down. Champagne or sparkling wine for the midnight toast is non-negotiable. Signature New Year cocktail named for the year/occasion.

ALL FESTIVALS: The Gourmet Food Architects concept — beyond normal catering. Edible art using liquid nitrogen (instant frozen festive desserts), glowing cocktails that sparkle under UV light, and interactive food stations that match the festival's theme.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR FESTIVE PARTIES (with reasoning):
1. Thematic Decor and Fabrication House — The core of every festive event. Creates the setup specific to each festival: diya wall and floral rangoli for Diwali, color zones for Holi, Christmas tree and snow zone for Christmas, LED console setup for New Year. Their work defines whether the event feels generic or genuinely festive.
2. High-End AV and SFX Vendor — Handles laser shows for Diwali, snow machines for Christmas, and countdown graphics and cold pyros for New Year. The SFX partner is what separates a hotel event from a world-class production.
3. Gourmet Catering Partner — Prepares festival-specific menus: traditional Indian sweets and buffet for Diwali, thandai and Holi snacks for Holi, European gala dinner and plum cake for Christmas, champagne countdown service for New Year.
4. Gift and Hamper Specialist — Designs customized festive hampers: silver coins and luxury chocolates for Diwali, organic color packets for Holi, Christmas hampers with gourmet goodies, New Year hampers with champagne and branded keepsakes.
5. Kinetic and Specialized Lighting Vendor — Not ordinary light vendors. Installs moving LED spheres on banquet ceilings (Diwali/New Year) and sets up laser mapping that changes shapes to music beats. Creates the immersive lighting centrepiece of the event.
6. Olfactory (Scent) Designer — Installs sophisticated diffusers throughout the venue spreading festival-specific fragrances: sandalwood for Diwali, rose for Holi, cinnamon and pine for Christmas. Scent marketing is now used at international events — this is what makes an Indian festival feel world-class.
7. AR and Tech Production House — Handles QR-code interactive filters, 3D projection mapping, and turns the hotel building into a digital canvas for New Year countdowns and Christmas AR experiences.
8. Atmospheric SFX Specialists — Safe, professional setup of artificial snowfall for Christmas, organic glow-mist for Holi, and indoor cold pyros for New Year. Always requires fire-clearance from the hotel.
9. Gourmet Food Architects — Beyond normal caterers: creates edible art using liquid nitrogen, glowing UV cocktails, and interactive food stations that become part of the event's visual spectacle.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR FESTIVE PARTIES:

FESTIVAL-SPECIFIC PERFORMERS:
- Diwali: Sufi Band — soulful, spiritual, and perfectly matched to Diwali's contemplative warmth. Interactive pot-making artists.
- Holi: Punjabi Dhol team and live percussionists — high-energy, driving the crowd into Holi's celebratory frenzy. Caricature artists for interactive fun.
- Christmas: Carol singing group — the essential Christmas tradition. Santa Claus interactive artist for children and adults alike.
- New Year: International DJ — high-energy set building to the midnight countdown; the most important artist of the New Year event.

ALL FESTIVALS:
1. Celebrity Emcee — Keeps the entire evening engaging, leads the puja countdown for Diwali, manages crowd energy for Holi, hosts carol ceremonies for Christmas, and leads the New Year countdown. The anchor who ties every element of the evening together.
2. LED and Laser Violinist or Percussionists — For grand entries at Diwali and New Year: lasers emerge from their instruments and outfits, creating light patterns across the entire banquet hall. A stunning visual and musical opening.
3. Digital Speed Painter — Creates a live painting on a large LED screen, merging live photos of guests with festive patterns (Diwali lights, Holi colors, Christmas motifs, New Year fireworks). Creates a grand piece of art in real time.
4. Spatial Audio DJ / Producer — For New Year and Holi: DJs who create 360-degree surround sound. Music feels like it is rotating all around the hall, pulling guests into an immersive audio zone.
5. International Folk Fusion Groups — Gospel Jazz Choir for Christmas that blends tradition with modern arrangements. Electronic Dhol-Tasha groups for Holi that fuse old traditions with contemporary beats.
6. Acrobatic Storytellers — Perform aerial acts narrating the festival's story while suspended in the air. Flying Elves for Christmas, a Light Goddess act for Diwali. A breathtaking visual surprise.
7. AR/VR Content Developers and Projection Mapping Artists — Transform hotel walls into a story-telling canvas; create custom interactive AR filters for guests.
8. Interactive Food Stylists — Create edible art live: glowing desserts under UV light, nitrogen-fused festive snacks, interactive dessert counters that are performances in themselves.
"""

PERSONALIZATION_QUESTIONS = [
    "Which festival are we celebrating — Diwali, Holi, Christmas, or New Year? Each festival has a completely distinct atmosphere, color palette, ritual sequence, and entertainment style — I want to make sure every element is crafted specifically for this occasion.",
    "Is this a corporate festive event for your company and employees, or a personal celebration for family and friends? The scale, formality, and entertainment choices are very different — and both can be extraordinary in their own way.",
    "Does your family or leadership follow any Vastu principles or lucky color preferences? For Diwali we place the puja area in the North-East; for New Year the main stage faces West — aligning these with your beliefs adds a deeply meaningful layer to the evening.",
    "Would you like personalized festive hampers for each guest — silver coins and luxury chocolates for Diwali, organic color packets for Holi, gourmet Christmas boxes, or champagne and branded keepsakes for New Year? A personalized take-home gift makes every festival celebration feel complete.",
    "Which creative experience excites you most — the Nebula Light and Scent Experience for Diwali, the Digital-Dry Neon Rave for Holi, the Arctic Crystal Dome and AR Santa's Workshop for Christmas, or the Time-Capsule 360° Countdown with the Silent Midnight Explosion for New Year?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Festive Party:

DIWALI:
06:30 PM — Venue setup complete; diya wall and floral rangoli lit and ready
07:00 PM — Guests arrive; puja area in North-East prepared
07:30 PM — Lakshmi-Ganesh puja ceremony begins
08:15 PM — Grand musical evening opens; Sufi band performs
09:00 PM — Traditional buffet and live sweet-making counter opens
09:45 PM — Digital firework laser show; interactive activities
10:30 PM — Festive hampers distributed; celebration continues
11:30 PM — Wrap-up

HOLI (AFTERNOON FORMAT):
10:00 AM — Venue setup; open lawn ready with dry-mist system and color zones
11:00 AM — Guests arrive; dhol-tasha team begins
11:30 AM — Flower-shower Holi ceremony begins; thandai counter opens
01:00 PM — Rain dance and full Holi celebration
02:30 PM — Clean-up and change zone; gourmet lunch served
04:00 PM — Wrap-up; guests receive festive hampers

CHRISTMAS:
07:00 PM — Arrival; Christmas tree and snowfall display at entrance
07:30 PM — Carol singing begins; hot chocolate bar opens
08:30 PM — Tree lighting ceremony
09:00 PM — European gala dinner; live roast turkey counter
10:00 PM — AR Santa's Workshop experience; interactive activities
11:00 PM — Dessert; Christmas hampers distributed; wrap-up

NEW YEAR:
08:00 PM — Arrival; full bar and gala dinner service begins
09:00 PM — DJ set begins; dance floor opens
10:00 PM — AI Memory Mosaic Wall begins collecting guest photos and resolutions
11:00 PM — Countdown graphic on hotel building begins projecting
11:45 PM — Silent Midnight Explosion headphones distributed; final countdown begins
12:00 AM — Midnight reveal; cold pyros or biodegradable balloon release; champagne toast
12:30 AM — Celebration continues; New Year hampers distributed
"""
