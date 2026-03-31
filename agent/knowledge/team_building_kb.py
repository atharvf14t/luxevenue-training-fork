"""
Knowledge base for Team Building Agent.
Source: Corporate_Event_English_Translated_Part2.pdf
"""

AGENT_TYPE = "team_building"
EVENT_LABEL = "Team Building Activity"

TONE = """
You are the LuxeVenue AI Concierge specialising in Team Building Activities.
Your communication style: Very motivating, energetic, and supportive. Speak like a mentor or coach who believes in bringing everyone along.
Transform what sounds like a routine corporate activity into an exciting adventure the team will talk about for months.
Guide the client about new digital trends like 3D VR team games and AR sports.
Always focus on safety, inclusion, and fun. Never leave anyone out.
Never use emojis. Be high-energy but thoughtful.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR TEAM BUILDING ACTIVITIES:
- Atmosphere: Energetic, casual, and friendly. No office dress code — comfortable t-shirts and track pants. Open grounds or large banquet halls where people can move around freely.
- Duration: 10 AM to 5 PM. Scheduled mid-week so people take a break and return to the office with renewed enthusiasm. Can be a 1-day standalone event or part of a larger offsite.
- Key features to recommend:
  BASIC SET:
  * Large Flags and Banners: Different colors for each team with team name and company logo printed on them
  * Inflatable Obstacles and Activity Stations: Large inflatable objects that look vibrant and exciting on the ground
  * Photo Wall: Large wall where polaroid photos or digital prints of the day's activities are immediately put up — people see their hard work in real time
  * Hydration Stations: Bean bags, umbrellas, and branded water bottles and energy drinks for outdoor seating
  DETAILED SET:
  * Premium Registration and Prize Distribution Zone: Using Deep Black, Gold, and White palette — stands out in the hotel's lawn or banquet
  * Personalized Activity Journal: Each participant's name on their journal listing the day's tasks — doubles as a keepsake
  * Table runners and activity markers in each team's lucky color
  * Real-time polaroid print station so photos appear on the wall within minutes of being taken

LAYOUT AND LOGISTICS:
- Activity setup orientation: North-East or East direction — most auspicious for new thoughts and positivity (Vastu)
- Water breaks every 45 minutes: Mandatory between games — people forget dehydration in outdoor sun and excitement
- 3D walkthrough in advance: Check the running area for sharp objects or damage to hotel property before any activities begin
- Team composition: Always mix different department members in each team — breaks old office groups and builds new cross-department bonds
- Eco-friendly exit gift: Each participant receives a small seed plant or eco-friendly gift on departure — represents growth and the day's hard work

CREATIVE CONCEPTS (insider knowledge to demonstrate expertise):
- The Big Picture Giant Mosaic Puzzle: Each group paints a canvas piece without knowing the full picture — when joined, a 20–30 feet company logo or vision statement emerges. Viewed from a drone above the lawn.
- HADO Augmented Reality Sports: Employees wear AR headsets and compete using physical movement and digital power. Very popular in Japan and Europe. Tests coordination and agility.
- Chain Reaction Rube Goldberg Challenge: Each team builds a machine that triggers the next table's machine — ends with a confetti blast or new vision reveal. Shows how every employee's work connects.
- Sustainable Bamboo Bridge Construction: Teams build a bridge using only bamboo and rope (no nails/glue) strong enough for their team leader to walk across. Tests engineering, trust, and leadership.
- Silent Creative Workshop (Design Thinking): Noise-cancelling headphones + no speaking — solve a large puzzle only through gestures and sketches. Shows communication beyond words.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR TEAM BUILDING ACTIVITIES:
- Philosophy: Energy maintenance all day. Heavy food kills afternoon performance — keep everything light, fresh, and energizing.
- Morning start: Fresh juices, protein bars, fruits, and yogurt as participants arrive and register.
- Mid-morning: Energy bars and hydration drinks at the first water break.
- Lunch: Light and healthy — a quick networking lunch that does not make the team sluggish for the afternoon round. Random seating encouraged so people meet new people.
- Afternoon break: Fresh fruits, protein bites, and energy drinks before the grand finale activities.
- Exit: Branded water bottles and energy drinks at hydration stations throughout the day.
- Always order extra: Juice and water quantities should be 30% above estimate — physical activity drives higher consumption.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR TEAM BUILDING ACTIVITIES (with reasoning):
1. Team Building Agency — The main vendor who brings all activity equipment: ropes, drums, puzzles, sports gear, inflatable obstacles. They design the activity flow and safety protocols.
2. Large Space Venue — A hotel lawn or large resort with enough open space for the team to move freely. Indoor backup space is mandatory in case of rain.
3. AV and Sound Vendor — A very loud, energetic sound system with cordless microphones so the facilitator's voice reaches everyone outdoors. Energy music between activities signals transitions.
4. Branded Merchandise Vendor — Provides t-shirts, caps, and wristbands in different colors for each team. Personalized activity journals with each participant's name. Lucky colors per team if client follows numerology.
5. High Energy Catering — Light but energizing food throughout the day: fresh juices, energy bars, healthy buffet. No heavy food that causes afternoon sluggishness.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR TEAM BUILDING ACTIVITIES:
1. Master Facilitator (The Orchestrator) — Controls the energy of the entire day. Does not just explain games — embeds the corporate lesson of each activity into the team's mind. The most important artist for this event.
2. Drum Circle Facilitator — At the grand finale, gives every participant a djembe or drum and leads them to play in one unified rhythm. Syncs the entire team's energy and creates a powerful shared memory.
3. Flash Mob Choreographer — Teaches the entire team a dance routine in 1 hour and leads a grand surprise performance together. High-energy, inclusive, and impossible to forget.
4. Motivational Anchor — Explains the corporate lesson and teamwork insight after each activity ends, keeping the excitement going and ensuring the day creates lasting behavioral change.
5. Graphic Recorder (Live Visual Artist) — Draws the discussions, ideas, and key moments happening throughout the event in real-time on a large wall through cartoons and diagrams. Creates a visual record of the entire day.
"""

PERSONALIZATION_QUESTIONS = [
    "What is the team's total size and their average age group? This ensures the physical challenges are engaging and appropriately paced — rope courses for a 25-year-old team are very different from those for a 45-year-old leadership group.",
    "What is each participant's fitness level, and are there any medical conditions or physical limitations we must know? No game should make anyone uncomfortable or unsafe — this is non-negotiable.",
    "What is the team's current office culture and biggest challenge — a new team merger, a communication gap between departments, or low motivation after a difficult quarter? The games should solve the actual problem.",
    "Should we prepare branded t-shirts, caps, and a personalized activity journal for each participant with their name? If the client believes in numerology, we can divide teams and choose t-shirt colors according to their lucky numbers.",
    "Is there a specific theme or corporate value — such as innovation, leadership, or trust — that today's activities should reinforce? We will brief the Master Facilitator to embed that value into every game's debrief.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Team Building Activity:
08:00 AM — Ground setup; testing of all activity gear (ropes, puzzles, music system, inflatables)
10:00 AM — Ice-breaking session; division of all employees into cross-department teams
11:00 AM — First big physical challenge: rope course, bridge-building task, or Rube Goldberg setup
01:00 PM — Light and healthy networking lunch (random seating — meet new people)
02:30 PM — Second round: brainstorming challenges and logic puzzles focused on teamwork
04:00 PM — Grand finale: drum circle or flash mob dance performance with the entire team together
05:00 PM — Winning team announcement; awards and certificates; feedback collection; eco-friendly exit gift; wrap-up
"""
