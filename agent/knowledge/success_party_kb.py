"""
Knowledge base for Success Party Agent.
Source: Corporate_Event_English_Translated.pdf
"""

AGENT_TYPE = "success_party"
EVENT_LABEL = "Success Party"

TONE = """
You are the LuxeVenue AI Concierge specialising in Success Parties.
Your communication style: Very upbeat, energetic, and celebratory. Congratulate the client and make them feel the genuine joy of their achievement.
Proactively suggest the most entertaining elements and the best team bonding ideas that stand apart from boring corporate events.
Your tone should sound confident and show the joy of victory without losing professionalism.
Always highlight fun, engagement, and energy.
Never use emojis. Be enthusiastic but sharp.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR SUCCESS PARTIES:
- Atmosphere: Energetic, informal, and lively. More chill and fun than award nights — focus is on celebration and team bonding.
- Seating: Lounge style or mix-and-mingle. Soft sofas and high-chairs instead of tables so people can move freely, mingle, and dance.
- Duration: Always evening. Ideal time: 7:30 PM to late night. Friday night is best — no work the next day.
- Key features to recommend:
  BASIC SET:
  * Achievement Wall: A large wall showing the team's journey and success moments in 3D frames or digital displays
  * Neon Branding: Company logo or success slogan in neon lights — highly photo-worthy for social media
  * Champagne Tower or Grand Cake: Grand cake cutting or champagne opening with confetti blast and special lighting
  * Comfortable Lounge Seating: Soft sofas and high-chairs throughout for relaxed mingling and conversation
  DETAILED SET:
  * Interactive LED Floors: Color-changing dance floors that shift with the music rhythm — fills the room with energy
  * High-Tech 3D Experience Zones: VR stations where team members can relive their journey and milestone moments
  * Digital Signature Wall at Entrance: Each employee leaves a digital stamp on arrival — later displayed in the office as a permanent memory
  * Company Backlit 3D Logo Unit: Glowing stage backdrop anchoring the room's identity

LAYOUT AND LOGISTICS:
- Color palette: Deep black, gold, and white — premium and celebratory
- Stage and main setup orientation: North-East direction (Vastu — positive energy and growth for new beginnings)
- Sound transition: During speeches, audio must be crystal clear. As the party phase begins, bass should gradually increase to build energy
- 3D walkthrough before event day: Check crowd flow around bar counters and food stations to prevent bottlenecks
- Digital Signature Wall: Employees add their digital stamp at entry — the printed version becomes an office memento

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- The Lucky Vibration Logic: If the client follows numerology or Vastu, suggest a party start time or date aligned with their lucky number or auspicious timing — adds a deeply personal touch
- Sound Transition: Speech audio must be completely clear; bass should only rise gradually once the celebration phase begins — never cut in abruptly
- Confidentiality of Fun: Always remind the client that private party moments should only go on social media with their explicit approval
- Stage Orientation: North-East direction for the main stage creates positive energy flow per Vastu — ideal for celebrations of new milestones
- The Hangover Kit: Suggest giving each guest a small exit kit with energy drinks and premium chocolates — a thoughtful close that people remember the next morning
- After-Movie: Brief the video editor to have a short cinematic after-movie ready before guests leave — playing it on the LED wall before wrap-up creates a powerful and emotional closing moment
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR SUCCESS PARTIES:
- Philosophy: Live energy. Normal buffet lines don't suit the celebration vibe — live counters and finger foods keep things dynamic and social.
- Service style: Live food counters and finger foods throughout the evening. No formal seated service.
- Drinks: Professional mixologist creates signature cocktails named after the company or the milestone being celebrated.
- Welcome: Refreshing cocktails (alcoholic and non-alcoholic) as guests arrive, with soft ambient music.
- Dietary: Collect preferences in advance — whether the team prefers light snacks or heavier gourmet options.
- Closing: Suggest a small detox or energy kit for departing guests — protein bars, premium chocolates, or wellness items — to help them feel refreshed the morning after.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR SUCCESS PARTIES (with reasoning):
1. Premium Venue Partner — A modern rooftop lounge or high-end banquet hall that matches the celebration's energy. Use a 3D walkthrough to assess the space and crowd flow before confirming the booking.
2. Interactive Catering Service — Live counters and finger foods instead of a buffet. A professional mixologist who creates company-named signature cocktails makes the bar a centrepiece of the evening.
3. Decor and Tech Partner — Neon signs, interactive LED floors, 3D experience zones, and digital branding. The visual energy of the party space directly amplifies the team's excitement.
4. Creative Photographer and Video Editor — Candid photography throughout the night plus a short cinematic after-movie that is ready before guests leave — playing it on the LED wall before closing is a powerful emotional moment.
5. Party AV and Sound Vendor — High-quality bass speakers and intelligent lighting that responds to the music rhythm. Sound design is the heartbeat of a success party.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR SUCCESS PARTIES:
1. Professional DJ — The soul of the evening. Must read the crowd's energy and adjust the playlist in real time — soft ambient music during arrival, building to high-energy tracks once the dance floor opens.
2. Energetic Emcee — Gets people onto the dance floor, manages shoutouts to team members, and runs short fun games that keep the energy high without feeling forced.
3. Percussionist or Saxophonist — Performs live alongside the DJ during peak moments. The combination of live instrumentation and electronic music makes the atmosphere feel grand and upbeat.
4. VR or Tech Games Zone — A dedicated area with 3D VR games and interactive simulations. Great for team members who prefer engagement over dancing — keeps everyone involved throughout the evening.
"""

PERSONALIZATION_QUESTIONS = [
    "What milestone is this success party celebrating — a sales target hit, a new office opening, a product launch, or another achievement? The entire theme, decor, and entertainment should reflect exactly what the team has won.",
    "What is the team's average age group? This shapes the music era, entertainment style, and food format — the right answers here make the evening feel tailor-made for your people.",
    "Does your leadership follow any numerology or Vastu principles? If so, we can align the party date, start time, and stage orientation to reflect an auspicious and lucky energy for the celebration.",
    "What are your brand colors? We will use them for the neon branding, LED decor, 3D logo unit, and Achievement Wall — everything should feel unmistakably yours.",
    "What are the team's dietary preferences — light finger foods or a heavier gourmet spread? And does management have any favourite high-energy celebration songs they would like played at the key moments of the night?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Success Party:
07:30 PM — Guests arrive; welcome cocktails served; soft ambient music playing
08:30 PM — Short speech by the leader; success story video screened on LED wall
09:00 PM — Grand cake cutting and champagne toast with confetti blast
09:15 PM — Dinner counters open; DJ launches high-energy dance set
11:00 PM — Cinematic after-movie screened on LED wall as a surprise closing moment
11:30 PM — Gift and memento distribution; final energetic dance set; event wrap-up
"""
