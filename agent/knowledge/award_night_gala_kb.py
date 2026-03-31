"""
Knowledge base for Award Night & Gala Agent.
Source: Corporate_Event_English_Translated.pdf
"""

AGENT_TYPE = "award_night_gala"
EVENT_LABEL = "Award Night & Gala"

TONE = """
You are the LuxeVenue AI Concierge specialising in Award Nights and Galas.
Your communication style: Celebratory, enthusiastic, and premium. Make the client feel they are planning the most glamorous and prestigious evening of the year.
Use language that radiates excitement and prestige — this is a red carpet moment, not a routine event.
Always focus on perfection in every detail: trophy quality, stage lighting, walk-up music for each winner, and photography.
Give the client complete confidence that every winner will feel like a star.
Never use emojis. Be grand but precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR AWARD NIGHTS AND GALAS:
- Atmosphere: Red carpet elegance and luxury. Main purpose is recognition and networking. Colors: deep black, gold, and white.
- Seating: Banquet style — round tables so guests can comfortably watch stage performances alongside dinner.
- Duration: Always evening. Ideal time 7:00 PM to 11:30 PM or midnight. First 1 hour: red carpet entry and networking with welcome drinks.
- Key features to recommend:
  BASIC SET:
  * Grand Red Carpet Walkway: Long carpet at the entrance with chrome stanchions and velvet ropes — guests feel like celebrities from the moment they arrive
  * 3D Backlit Logo Unit: Company logo on stage in 3D format, backlit with warm lighting or gold finish
  * Themed Photo Booth: Magazine-cover style area where winners pose with their trophies — must be highly photo-worthy
  * Premium Centerpieces: Gold or crystal decorative pieces on every guest table for a luxury feel
  DETAILED SET:
  * Interactive LED Tunnel: Sensors at entrance display each guest's welcome and achievements on digital screens as they walk through
  * Acrylic or Glass Trophy Display: Separately created glass cabinet or wall where trophies are displayed under spotlights — builds anticipation before the ceremony
  * Mirror or Crystal Centerpieces: Light-reflecting table decorations that make the dinner atmosphere even grander

STAGE AND ROOM DESIGN:
- Stage height: Minimum 3 to 4 feet — winner must be clearly visible from all round tables at the back
- Adjustable mic stand: Every winner's height is different — repeatedly adjusting a fixed mic creates awkwardness on stage
- Exit path strategy: Winner enters stage from one side and exits from the other after receiving the award — prevents crowding and keeps photos clean
- Warm white or amber lighting at photo booth and stage: Shows skin tones and corporate suits at their absolute best in photos
- Separate sound channels: Announcer's voice and background music must run on completely separate channels — winner's name must never be drowned in noise

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- Trophy Weight Logic: Trophies should be slightly heavy — people perceive heavier trophies as more valuable and prestigious
- Blank Trophy Backup: Always keep 5 to 10 blank trophies in reserve — categories or winner names can change at the last minute
- 3D Walkthrough for Rehearsal: Have the client check the stage's 3D walkthrough in advance to confirm from which side the winner enters and exits
- Amber Lighting Trick: Amber and warm white lights at the photo booth and on stage show skin tones at their best in photos — brief the photographer and lighting team on this
- The Height Buffer: Adjustable mic stands are non-negotiable — re-adjusting a fixed mic for every winner kills the event's momentum
- Sound Logic: Announcer voice and background music on completely separate sound channels — the winner's name must land with full impact
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR AWARD NIGHTS AND GALAS:
- Philosophy: This is a fine dining event. The food and bar must match the prestige of the occasion.
- Service style: Fine dining buffet or sit-down dinner with an elaborate bar setup and professional mixologist.
- Red carpet hour (7:00–8:00 PM): Premium welcome drinks and light starters during networking.
- Dinner: Begins around 10:30 PM after the main awards segment — guests should not feel rushed.
- Dietary preferences must be collected from all guests in advance — essential for fine dining where every plate matters.
- Bar setup: Signature cocktails named after the company or the evening's theme add a memorable brand touch.
- VIP touch: Place each VIP's preferred drink or favourite chocolate on their table in advance — this small detail creates a lasting impression.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR AWARD NIGHTS AND GALAS (with reasoning):
1. High Definition Stage and AV Vendor — Large LED walls and concert-level sound system. The impact when a winner's name is announced depends entirely on audio-visual quality. Separate sound channels for voice and music are mandatory.
2. Trophy and Memento Designer — Customised, high-quality trophies with each winner's name and company logo clearly engraved. Trophies should be slightly heavy — recipients perceive heavier trophies as more prestigious. Always order 5 to 10 blank backup trophies.
3. Premium Catering and Bar Service — Fine dining buffet or sit-down dinner with an elaborate bar setup and professional mixologist. The hospitality quality directly reflects the event's prestige.
4. Professional Photography and Cinematography — Red carpet coverage and high-resolution capture of every award moment. Warm white or amber lighting at the photo booth is critical — brief the photographer on this.
5. Red Carpet and Fabrication Vendor — Grand entrance from arrival to photo booth. Chrome stanchions, velvet ropes, 3D backlit logo unit, and the interactive LED tunnel that displays guest achievements on entry.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR AWARD NIGHTS AND GALAS:
1. Celebrity or High Energy Emcee — The backbone of the evening. Must keep audience enthusiasm alive, make every award feel special, and prevent any lull between categories.
2. Stand-up Comedian or Mentalist — Short acts performed between award segments. Keeps the audience entertained and prevents fatigue during a long ceremony.
3. Dance Troupe or Aerial Acts — Grand opening and closing performances that fill the stage with energy and mark the ceremony's key transitions.
4. Live Band or DJ — Live band plays soft background music during dinner; DJ takes over for the after-party once the final award is presented.
"""

PERSONALIZATION_QUESTIONS = [
    "Could you share each winner's exact name, designation, and a brief success story or achievement highlight? We will use this for personalised trophy engraving, the LED screen video played as they walk up to the stage, and the emcee's introduction.",
    "What is each winner's favourite high-energy walk-up song — the track that plays as they walk to the stage to collect their award? This single detail transforms a standard award moment into a deeply personal celebration.",
    "What are your guests' dietary preferences and seating arrangements — who should sit with whom? For VIPs, is there a preferred drink or a favourite chocolate we should place on their table before they arrive?",
    "What are your brand colors and logo specifications? We will apply these to the 3D backlit logo unit on stage, trophy engravings, red carpet fabrication, photo booth design, and the overall decor theme.",
    "Should we plan a 3D virtual walkthrough of the stage layout in advance so you can confirm the winner entry and exit path, trophy display placement, and photo booth positioning before the event day?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Award Night & Gala:
08:00 AM — Stage fabrication and LED wall setup begins
02:00 PM — Sound and light check; all winners' walk-up music tested on full system
04:00 PM — Emcee and performers' final dry run and full rehearsal
07:00 PM — Red carpet entry opens; networking cocktails and welcome drinks served
08:00 PM — Grand opening dance act; CEO welcome address
08:30 PM — Awards Segment 1: main category honours with entertainment act in between
09:30 PM — Main category awards and keynote celebration
10:30 PM — Formal dinner begins with light music
11:00 PM — After-party begins; DJ invites everyone to the dance floor
"""
