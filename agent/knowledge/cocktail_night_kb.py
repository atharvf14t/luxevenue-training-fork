"""
Knowledge base for Cocktail Night Agent.
Source: Corporate_Event_English_Translated_Part2.pdf
"""

AGENT_TYPE = "cocktail_night"
EVENT_LABEL = "Cocktail Night"

TONE = """
You are the LuxeVenue AI Concierge specialising in Cocktail Nights.
Your communication style: Smooth, sophisticated, and classy. Use language that reflects luxury and tranquility.
Always focus on the balance of bar quality, lighting, and sound. Introduce the client to new trends like molecular mixology and sensory bar experiences.
Make the client feel they are curating an atmosphere, not just booking an event.
Never use emojis. Be refined, warm, and precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR COCKTAIL NIGHTS:
- Atmosphere: Sophisticated and moody. Dim lighting, premium decor, no formal seating or long speeches. People enjoy drinks and snacks standing or sitting on lounge sofas.
- Duration: 8:00 PM to 11:30 PM. 3 to 4 hours — focused on quality networking, not length.
- Colors: Deep black, gold, and white — gives an expensive and luxury feel that perfectly suits this event.
- Key features to recommend:
  BASIC SET:
  * Infinity Mirror Bar: Bar counter made of mirrors and LED lights that looks never-ending — an instant visual centrepiece
  * Ice Sculptures: Large ice sculpture of the company's logo in the middle of the bar through which drinks flow
  * Branded Cocktail Napkins and Stirrers: Company logo and theme colors on every small item
  * Floating Candle Installations: If the hotel has a pool, floating lights and candles create an unforgettable atmosphere
  DETAILED SET:
  * Warm Amber Lighting: Creates the moody, sophisticated atmosphere essential for a cocktail night
  * Velvet Lounge Sofas + High-Tables + Bar Stools: Replace all normal chairs — people must be able to mingle freely
  * Light Fragrance Throughout the Hall: A subtle scent that complements the drinks and candle-lit table decor
  * Personalized Coasters or Glass Markers: Each guest's name on their glass or coaster — a powerful hospitality detail

LAYOUT AND LOGISTICS:
- Bar orientation: North-West direction (Vastu — considered most auspicious for social gatherings and enjoyment)
- 3D walkthrough for bar placement: Check in advance that the bar is not positioned at the entry — crowding at the bar blocks the entire event flow
- Crystal and heavy cocktail glasses: Corporate guests associate heavy, high-quality crystal glasses with luxury — brief the bar partner on this
- Always have a backup bartender and extra stock: Service must never slow down during the peak rush between 9 PM and 10:30 PM

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):
- Molecular Alchemist Bar: Bartenders use molecular mixology — drinks transform into bubbles, smoke, and foam. Edible cocktail spheres and liquid nitrogen slushies. Feels like a live performance.
- Interactive Projection Bar Counter: Sensors placed on the bar surface — when a guest places their glass, digital light patterns emerge and follow the glass's movement. Can display the company logo or product journey.
- Scent-Paired Cocktail Experience: Each drink is paired with a matching fragrance mist. Before receiving the drink, guests experience aromatic dry ice smoke that enhances the flavor. A multi-sensory premium journey.
- Floating Bar in the Pool with Drone Delivery: A floating island bar in the pool; drones deliver drinks to VIP tables. Unique blend of technology and hospitality.
- Silent Mixology Masterclass: A small silent zone with noise-cancelling headphones — an international mixologist teaches guests step-by-step how to make their own drink. From outside, silence; inside, a high-energy masterclass.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR COCKTAIL NIGHTS:
- Philosophy: This is not a dinner event. The focus is on premium cocktails and high-end pass-around snacks that complement the drinks — not a buffet.
- Bar: An elaborate bar setup with professional bartenders who craft flaming drinks and customized cocktails. A signature cocktail named after the client/company is essential.
- Finger foods: High-end pass-around snacks and appetizers that pair well with drinks. Light, elegant, and bite-sized.
- Dessert cocktails: A special dessert cocktail round served around 10:45 PM — sweet finish before the event closes.
- Client's preferred liquor brands should be stocked. Collect this information in advance.
- Non-alcoholic premium options must be available alongside the cocktail menu — mocktails should be equally crafted.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR COCKTAIL NIGHTS (with reasoning):
1. Premium Mixology and Bar Partner — The centrepiece of the entire event. Professional bartenders who craft flaming drinks, customized cocktails, and the client's named signature cocktail. They also bring the full bar setup including the Infinity Mirror Bar.
2. Gourmet Finger Food Caterer — High-end pass-around snacks and appetizers. Not a buffet. Food must be elegant, bite-sized, and pair well with cocktails — the quality of bites reflects the event's prestige.
3. Mood Lighting and AV Vendor — Warm amber lights, neon accents, and a soft but crystal-clear sound system. Lighting alone determines 50% of the cocktail night's atmosphere.
4. Luxury Furniture Rental — Bar stools, high-tables, and comfortable velvet lounge sofas. No normal chairs. The furniture arrangement defines the networking flow.
5. Fragrance and Ambient Decor Vendor — A light, carefully chosen scent throughout the hall and candle-lit table decor. Transforms the space from an event to an experience.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR COCKTAIL NIGHTS:
1. International or Jazz Saxophonist — Roams through the crowd playing live music and maintains a classy, sophisticated vibe throughout the early hours. The perfect cocktail night opener.
2. Mentalist or Close-up Magician — Moves among guests performing close-up acts that surprise and delight. Creates conversation topics and breaks the ice between guests who don't know each other.
3. Soulful Live Band or Trio — Plays acoustic versions of classics or modern songs that are soothing without overpowering conversation. Background that elevates without distracting.
4. Deep House or Lounge DJ — Gradually increases the pace of music as the night progresses, maintaining the sophisticated atmosphere while adding energy. Guests can still talk — music never becomes noise.
5. Flair Bartender Champions — Don't just make drinks; perform international-level juggling stunts with bottles and shakers. Turns the bar into a performance stage.
6. Electric Violinist or Cellist — Live performance on modern lounge music or deep house beats. Instrumental music that becomes the perfect networking background.
"""

PERSONALIZATION_QUESTIONS = [
    "What are your preferred liquor brands, and what would you like to name the signature cocktail? We can name it after the company, the occasion, or the evening's theme — this becomes a memorable talking point for every guest.",
    "Could you share your guest list profile and their general drink and food preferences? A cocktail night menu curated for the specific audience — whisky lovers, wine enthusiasts, non-drinkers — elevates the experience significantly.",
    "Does your leadership follow any lucky number or Vastu principles? We can position the bar in the North-West direction and align the entry flow accordingly for positive energy throughout the evening.",
    "Would you like personalized coasters or glass markers with each guest's name? This small detail consistently leaves the biggest impression in post-event feedback at cocktail nights.",
    "Which creative bar concept excites you most — the Molecular Alchemist Bar with liquid nitrogen and edible cocktail spheres, the Interactive Projection Bar Counter, the Scent-Paired Cocktail Experience, the Floating Pool Bar with drone delivery, or the Silent Mixology Masterclass?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Cocktail Night:
08:00 PM — Guests welcomed; first round of signature cocktails served
08:30 PM — Live saxophonist or acoustic band performance begins; networking in full flow
09:15 PM — Premium finger foods and pass-around appetizers intensify
10:00 PM — Mentalist or close-up magician moves among guests to interact and surprise
10:45 PM — Dessert cocktails served; final networking session
11:30 PM — Closing drinks; event wrap-up; guests thanked personally
"""
