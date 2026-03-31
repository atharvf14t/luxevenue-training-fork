"""
Knowledge base for Workshop & Training Session Agent.
Source: Corporate_Event_English_Translation_Part2.pdf
"""

AGENT_TYPE = "workshop_training"
EVENT_LABEL = "Workshop & Training Session"

TONE = """
You are the LuxeVenue AI Concierge specialising in Workshops and Training Sessions.
Your communication style: Very encouraging, energetic, and supportive. Like a coach or mentor.
Suggest new ideas and creative solutions that transform a boring training into an exciting workshop.
Always focus on engagement and participant comfort.
Give the client tips that make their training memorable and effective.
Never use emojis. Be energetic but precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR WORKSHOPS AND TRAINING SESSIONS:
- Atmosphere: Interactive and energetic. Focus is on doing and learning, not just listening.
- Seating: Cluster style — round tables so people can sit in groups and discuss.
- Brainstorming boards and flipcharts are essential. Creativity must be supported by the setup.
- Duration: 9:30 AM–4:30 PM typically. Some are 2–3 days long. Best on Thursday or Friday.
- Key features to recommend:
  BASIC SET:
  * Vision Boards: Large boards on hall walls where people can pin ideas
  * Motivational Graphics: Quotes and graphics on walls representing innovation and teamwork
  * Zone Branding: Different corners branded as Idea Zone, Chill Zone, Execution Zone
  * Digital Countdown Clocks: Timers on large screens to manage activity time
  DETAILED SET:
  * Interactive Wall Panels: Large whiteboards or pin-up boards for live brainstorming
  * Zone-Based Branding: Hall divided into Innovation Lab and Chill-out Zone with different colors and furniture
  * Motivational Decals: Graphics and quotes on walls and floors representing teamwork and growth mindset
  * Flexible Cluster Seating: Round tables with premium linen and a stationery caddy at center (markers, post-its, fidget toys)
  * Digital Progress Tracker: Large screen live-updating team points or progress after each session

LAYOUT AND LOGISTICS:
- Gap of 3–4 feet between each table so the trainer can move freely around the room
- Lighting: Bright lights during activities; warm lights during presentations
- Fragrance: Light lemon or peppermint scent helps increase focus and alertness

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- The Post-Lunch Slump: People become sluggish immediately after lunch — schedule the most energetic activity right after lunch
- The 2:00 PM Rule: Most sleepiness occurs post-lunch — the noisiest and most physical activity should be at this time
- Activity Buffer: Always add 15 extra minutes for activities — group discussions consistently run long
- The Quiet Table Logic: If any group is quiet, seat them closest to the facilitator — proximity increases engagement
- Sensory Learning: Light lemon or peppermint fragrance increases focus — suggest it to the venue manager
- Stationery Buffer: Always order 25% extra markers and sticky notes — they are used extensively
- Transition Music: A specific high-energy music clip played between activities signals task-switching without announcements
- Instant Feedback Wall: A board at the exit gate where participants write their one-word experience as they leave
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR WORKSHOPS AND TRAINING SESSIONS:
- Philosophy: Energy maintenance is the top priority. People get mentally tired quickly during training.
- Avoid: Heavy meals, fried food, excessive sugar — these cause sluggishness and loss of focus.
- Recommend: Fruits, nuts, dark chocolate, light high-protein meals throughout the day.
- Morning: Welcome with protein bars, fresh juices, yogurt, dry fruits.
- Mid-morning break: Tea and coffee with energy snacks — no heavy pastries.
- Lunch: Light and healthy. Networking seating (random) so people meet new people. Quick service.
- Afternoon break: Fresh fruits, protein bites, herbal teas — to combat the post-lunch slump.
- High-protein, sugar-free, and custom dietary options should be arranged in advance.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR WORKSHOPS AND TRAINING SESSIONS (with reasoning):
1. Interactive Tech Vendor — Smart boards, tablets, and high-speed internet for live exercises. Without these, interactive learning becomes passive listening.
2. Specialised Stationery Vendor — Beyond pens and pads: sticky notes, colored markers, chart papers, activity kits. Always order 25% extra — usage is very high.
3. Healthy Catering Service — Energy-focused menu with fruits, nuts, dark chocolate, and light meals. Heavy food kills engagement in afternoon sessions.
4. Furniture Rental — Flexible round tables and comfortable movable chairs. Fixed furniture makes cluster activities impossible.
5. Branding & Print Partner — Training modules, workbooks, and personalised certificates. Each participant should receive a workbook with their name printed on it.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR WORKSHOPS AND TRAINING SESSIONS:
1. Certified Trainer or Coach — The main session leader. Their energy and methodology define the entire experience.
2. Ice Breaker Specialist — Professional who conducts short activities at the start to remove participants' hesitation. Critical for day one.
3. Graphic Facilitator — Live-draws the key points of the entire training on large wall panels. Creates a visual record and keeps visual learners engaged.
4. Team Building Coordinator — Organises 15–20 minute physical activities or games after lunch or between sessions. Prevents the post-lunch slump from derailing the programme.
"""

PERSONALIZATION_QUESTIONS = [
    "What is the current skill level and learning history of your participants? This ensures the training content is neither too basic nor too advanced.",
    "What are the team's roles and departments? This allows us to create the right mix in group activities and customise the workbook content per role.",
    "Would you like personalised workbooks with each participant's name, and role-specific tool kits? For example, code references for the tech team, scripts for the sales team.",
    "Are there specific dietary preferences for participants — high-protein meals, sugar-free snacks, or other requirements? Energy management during the day directly affects learning outcomes.",
    "Has a pre-training survey been conducted? If so, please share the results — this helps us identify specific skill gaps and brief the trainer accordingly.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Workshop & Training Session:
07:30 AM — Hall furniture layout; all stationery checked at each table
08:30 AM — Participants' registration; personalised kit distribution
09:15 AM — Ice-breaking activity; start of first session
11:00 AM — Energy tea break — protein bars and fresh fruits served
01:00 PM — Networking lunch with random seating (people meet new people)
02:15 PM — Hands-on group activity with physical movement and collaboration
04:00 PM — Recap session; digital forms for feedback collection
04:45 PM — Certificate distribution; wrap-up with group photo
"""
