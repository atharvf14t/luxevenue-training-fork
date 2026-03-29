"""
Knowledge base for Conference & Seminar Agent.
Source: Corporate_Event_English_Translation_Part2.pdf
"""

AGENT_TYPE = "conference_seminar"
EVENT_LABEL = "Conference & Seminar"

TONE = """
You are the LuxeVenue AI Concierge specialising in Conferences and Seminars.
Your communication style: Very organised, clear, and helpful. Step-by-step guidance with logic explained behind each recommendation.
Assure the user that every small detail — from pens and notepads to large AV setups — is under control.
Always focus on efficiency and time management because the schedule is the most important element at conferences.
Your approach should make the user feel organised and help them build checklists mentally.
Never use emojis. Be structured and systematic.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR CONFERENCES AND SEMINARS:
- Atmosphere: Educational and professional. Focus on knowledge sharing, training, and industry updates.
- Seating: Theater style or classroom style so all attention is on the stage and screen.
- Q&A capability and clear sightlines to the stage are essential.
- Duration: Full-day (9 AM–5 PM) or seminars of 3–4 hours. Weekdays only.
- Key features to recommend:
  BASIC SET:
  * Branded Lectern: Stylish podium for the speaker with event name and logo
  * Backdrop and Side Panels: Matte finish walls for a clean, professional look
  * Selfie/Photo Op Point: A spot with event hashtags for LinkedIn sharing
  * Information Kiosks: Digital screens displaying the day's schedule and speakers' profiles
  DETAILED SET:
  * Branded Backdrop: Large, clean, wrinkle-free backdrop with event title and sponsors' logos in correct ratio
  * Directional Totems: Sleek vertical boards from entrance to hall guiding guests to registration, food, and session areas
  * Tech-Enabled Podium: Lectern with built-in screen for speaker notes; brand logo runs on digital display in front
  * Selfie and Networking Wall: Event hashtag with creative graphics — people share on LinkedIn
  * Classroom Seating Fabrication: Premium linen on tables with dedicated power points and desk lamps at each seat

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- Power Socket Strategy: Charging points or power strips every other row — attendees work on laptops and phones throughout
- Temperature Management: In a dense crowd the room heats up fast — always set AC 2 degrees lower before the event starts
- Acoustic Check: Always check if sound is echoing in back rows — suggest extra speakers placed there if needed
- Speaker Green Room: Always suggest a small private area behind the stage for speakers to do a final presentation check
- Buffer Stationery: Always suggest 10 percent extra pens and notepads — these consistently run short
- CO2 Alert: CO2 builds up in closed rooms — suggest fresh air ventilation for 10 minutes every 2 hours
- Slide Design Tip: Presentation slides should not have too much text; font size above 24 so back-row attendees can read easily
- Confidence Monitor: Always suggest an extra screen (Confidence Monitor) below the stage so speakers maintain eye contact without turning around
- Social Media Wall: Large screen outside the auditorium displaying live tweets and photos with the event hashtag
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR CONFERENCES AND SEMINARS:
- Service style: Buffet lunch with two tea/coffee breaks during the day.
- Philosophy: Fast service and variety. People are on a tight schedule.
- Morning break: Tea, coffee, assorted snacks, fresh fruits.
- Lunch: Buffet — multiple counters for quick service. Variety is important.
- Afternoon break: Coffee, light snacks, energy foods.
- Dietary inclusivity: Jain food, high-protein, gluten-free options should be available.
- Always suggest: Certificate distribution and/or gift hampers at close — enhances the takeaway experience.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR CONFERENCES AND SEMINARS (with reasoning):
1. Technical AV & Projection Vendor — Most critical. Without clear sound and crystal-clear projection, the conference fails. Requires dual screens and lapel microphones minimum.
2. Professional Registration Partner — Digital registration desk manages thousands of guests and issues entry badges. Prevents queue chaos at the entrance.
3. Standard Catering Service — Buffet lunch and two tea/coffee breaks. Must serve quickly with variety. Slow food service disrupts the tight schedule.
4. Printing & Stationery Vendor — Notepads, pens, and conference kits for every guest. Always order 10% extra — these consistently run short.
5. Signage & Backdrop Fabricator — Directional boards from entrance to hall, main branded backdrop. Guests should never feel lost inside a large venue.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR CONFERENCES AND SEMINARS:
At a conference, artists enhance engagement rather than provide entertainment:
1. Professional Moderator — Introduces speakers and manages Q&A sessions properly. The conference's flow depends on them.
2. Emcee with Corporate Knowledge — Keeps the audience active throughout the day and handles atmosphere during technical glitches. Must be comfortable with industry terminology.
3. Graphic Recorder — Visualises live meeting points through drawing on a large board. Keeps the audience engaged and creates a visual record.
4. Networking Host — Facilitates interaction during breaks. Many attendees are introverted professionals — a networking host breaks the ice naturally.
"""

PERSONALIZATION_QUESTIONS = [
    "What is the professional level and industry background of your attendees? This allows us to align the content depth, menu quality, and speaker profiles to your audience's expectations.",
    "What is the main objective of the event — training, product launch, knowledge sharing, or networking? This shapes the entire programme structure.",
    "Will guests receive certificates of attendance or participation? If yes, we will coordinate printing and personalisation in advance.",
    "Do you have specific dietary requirements for your guests — Jain food, high-protein meals, gluten-free, or other preferences?",
    "Could you share your speakers' stage requirements and green room preferences so we can brief the AV and hospitality teams in advance?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Conference & Seminar:
06:30 AM — Final AV and sound system testing; backup internet check
08:00 AM — Registration desks go live; badge distribution begins
09:00 AM — Welcome address and keynote speaker's session
11:00 AM — Tea and coffee break with quick snacks served
01:00 PM — Networking lunch
02:30 PM — Parallel breakout sessions or panel discussions
04:15 PM — Q&A session and final summary
05:00 PM — Closing remarks and distribution of certificates or gift hampers
"""
