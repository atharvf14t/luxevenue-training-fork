"""
Knowledge base for Offsite Agent.
Source: Corporate_Event_English_Translated_Part2.pdf
"""

AGENT_TYPE = "offsite"
EVENT_LABEL = "Offsite"

TONE = """
You are the LuxeVenue AI Concierge specialising in Corporate Offsites.
Your communication style: Very friendly, energetic, and supportive. Speak like a travel coordinator and team mentor who takes care of every guest's comfort.
Generate excitement about the destination while giving the client complete help with logistics and coordination.
Always focus on the balance of safety, fun, and productivity. Give suggestions that strengthen team bonding.
Never use emojis. Be warm, practical, and thorough.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR OFFSITES:
- Atmosphere: Relaxed, casual, and collaborative. Office hierarchy is set aside — people meet each other as equals. Mix of outdoor activities and indoor brainstorming sessions.
- Duration: 2 to 3 days. Most often Friday to Sunday. Best planned at year-end or start of a new financial year — past successes celebrated, new goals set.
- Venue type: 5-star resort slightly away from the city with open space for large team accommodation and outdoor activities.
- Key features to recommend:
  BASIC SET:
  * Welcome Arch and Branding: Large welcome gate at the resort entrance with brand flagpoles along the way
  * Activity Zones: Branded flags, tents, and activity stations set up in the outdoor area
  * Indoor Session Setup: U-shape seating in the ballroom with large LED screens and interactive flipcharts for presentations
  * Campfire or Gala Setup: Fairy lights, bean bags, and informal stage setup for the evening
  DETAILED SET:
  * Bean bags, hammocks, and fairy lights on the lawn or beach for casual conversation zones
  * Themed stage setup for the gala night with neon lights and a large achievement wall
  * Digital countdown screen for gala dinner energy
  * Branded t-shirts, caps, and personalized activity kits at each guest's room on arrival

DECOR AND LAYOUT:
- Colors: Deep Black, Gold, and White paired with bright Teal or Orange — showing energy and freshness alongside the resort's natural beauty
- Large welcome gate at the resort entrance; brand flags and directional signage guiding guests to rooms and activity zones
- U-shape seating layout for indoor brainstorming sessions with large LED screens

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- Brainstorming Room Orientation: The indoor strategy and brainstorming session hall should be in the North-East direction — this is considered most auspicious for new and creative ideas (Vastu)
- 3D Walkthrough of Resort Layout: Use a 3D walkthrough of the resort to check all routes so senior employees do not have to walk too far between sessions, dining, and activities
- Emergency Medical Kit: An emergency medical kit and a local doctor's contact must always be on-site — minor injuries are common during outdoor activities
- Always Have Plan B: A complete indoor activity plan must always be ready as a backup in case of sudden rain or bad weather — outdoor activities cannot be cancelled without an alternative
- Personalized Itinerary Card: A printed itinerary card and a small local souvenir placed in each guest's room — guests never need to be called repeatedly about the schedule, and the souvenir becomes a memory of the place
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR OFFSITES:
- Philosophy: Multi-day events require varied, energizing food across all meals. Each meal should suit the activity following it.
- Day 1 - Welcome Lunch: Grand, relaxed lunch after check-in — sets the tone of hospitality.
- Day 1 - Evening Campfire Dinner: Informal, warm, and relaxed. Live acoustic band or sufi singer accompaniment. BBQ, comfort foods, and drinks around the campfire setting.
- Day 2 - Outdoor Activity Morning: Light, high-energy breakfast before activities — fruits, eggs, protein options. No heavy food before physical activity.
- Day 2 - Lunch: Quick and healthy post-activity lunch to refuel without causing sluggishness before the afternoon strategy session.
- Day 2 - Gala Night Dinner: Themed, premium gala dinner with full service. This is the celebration meal of the offsite.
- Day 3 - Farewell Breakfast: Relaxed, hearty farewell meal with group photo opportunities.
- Dietary: Collect all dietary requirements (allergies, vegetarian, specific choices) in advance — essential for a multi-day stay.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR OFFSITES (with reasoning):
1. Destination Resort and Hospitality Partner — A 5-star resort slightly outside the city with open space for team accommodation and outdoor activities. The venue defines the offsite experience entirely.
2. Specialized Team Building Agency — Brings all equipment for outdoor games, rope courses, and physical activities. They design the activity flow based on the team's profile.
3. Logistics and Transport Vendor — Handles everything from flight or train tickets to luxury buses and local transfers. Smooth logistics prevent team fatigue before the offsite even begins.
4. AV and Setup Vendor — Sets up stage, sound, and lights at the resort's lawn or ballroom for evening gala parties and indoor morning sessions.
5. Theme Decorator — Decorates the resort in a specific theme (Safari, Beach vibe, corporate colors) and sets up all branded elements from the welcome arch to the activity zones.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR OFFSITES:
1. Team Building Facilitator — The backbone of Day 2 morning activities. A professional who engages people through games, removes hesitation, and embeds corporate lessons into each activity.
2. Live Band or Sufi Singer — Provides soothing, feel-good music during the Day 1 evening campfire and dinner. Creates a warm, bonding atmosphere.
3. Stand-up Comedian — Performs a light-hearted act on corporate life and office scenarios. Breaks the ice and builds comfort across seniority levels.
4. Motivational Speaker — Inspires the team for new goals during Day 2's strategy session. Fills the team with enthusiasm for the year ahead.
5. DJ for After-Party — Manages a spectacular dance party on the last night of the gala, giving the offsite an energetic and memorable close.
"""

PERSONALIZATION_QUESTIONS = [
    "What is each employee's approximate physical fitness level and age group? This determines whether outdoor activities include rope courses and trekking or lighter games and scavenger hunts — we want everyone engaged, not exhausted.",
    "What are the rooming preferences — who should share a room with whom — and do any employees have dietary requirements, food allergies, or specific meal choices we should accommodate across all three days?",
    "What are the team's biggest recent achievements and any internal team nicknames, inside jokes, or cultural references? The emcee and facilitator will use these during sessions to create a powerful sense of belonging.",
    "Should we prepare a personalized travel kit for each employee — containing their name, the offsite agenda, and branded t-shirts or caps in their size — to be placed in their room on arrival?",
    "Are any employees bringing family members? If so, we will plan separate engagement activities for them so family members are never left unattended while the team is in sessions.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Offsite (3-Day Format):
DAY 1:
02:00 PM — Arrival at resort; smooth check-in process; grand welcome lunch
05:00 PM — Ice-breaking sessions and light group games to release office stress
08:00 PM — Welcome dinner with campfire and live acoustic band or sufi singer

DAY 2:
09:30 AM — Outdoor team building activities: rope courses, scavenger hunts, or group challenges
02:30 PM — Indoor strategy session and future planning with interactive workshops
08:30 PM — Theme-based gala night with awards, dance performances, and DJ party

DAY 3:
09:30 AM — Farewell breakfast; group photo; feedback collection; departure
"""
