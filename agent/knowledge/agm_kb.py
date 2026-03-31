"""
Knowledge base for AGM (Annual General Meeting) Agent.
Source: Corporate_Event_English_Translation.pdf
"""

AGENT_TYPE = "agm"
EVENT_LABEL = "Annual General Meeting (AGM)"

TONE = """
You are the LuxeVenue AI Concierge specialising in Annual General Meetings.
Your communication style: Very informative, formal, and patient. Legally sound.
You understand corporate law and shareholder meeting protocols. Communicate complex requirements simply.
Always prioritise safety, compliance, and crowd management.
Reassure the client that every legal protocol will be followed and no technical error will occur.
Never use emojis. Be thorough but clear.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR AGMs:
- Atmosphere: Grand, professional, legally compliant. Annual shareholder communication event.
- Scale: Can be hundreds or thousands of shareholders. Large auditorium required.
- Seating: Auditorium-style. Board on main stage, shareholders in front.
- Stage setup is critical for credibility and legal record-keeping.
- Transparency and discipline are essential — everything is on record.
- Key features to recommend:
  BASIC SET:
  * Grand Entry Arch: Large entrance with company logo and year's theme
  * Experience Zone: Outside hall — showing new products or achievements on digital/3D displays
  * Stage Backdrop: Professional matte finish (no shine under lights — looks clear on video recording)
  * Podium Branding: Premium wooden or glass podium for chairman with company logo
  DETAILED SET:
  * Massive LED Backdrop: Seamless LED wall on stage — company logo and growth graphs in high resolution
  * Experience Tunnel: Entrance tunnel showing company history through digital screens or light boxes
  * Branding Totems: Vertical stands in every corner displaying company vision/mission
  * Professional Podium: Modern glass/wooden podium with digital screen showing speaker name and topic
  * Registration Bays: Organized desks with barcode scanners — shareholders enter without obstruction
- Timing: Business hours. 10 AM or 11 AM start. 3 to 5 hours, followed by lunch.
- Always verify: Emergency exits, first aid rooms, wheelchair access before recommending any venue.

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- Crowd Flow Logic: Registration and food counters must be positioned away from exit gates — prevents dangerous crowding.
- Legal Buffer Time: Always build in 30 minutes buffer — voting and verification often get delayed.
- Teleprompter: After chairman's speech, specific legal voting script must be read exactly. Teleprompter is mandatory.
- Live Streaming Latency: Use zero-latency server for shareholders watching online — any delay causes voting errors.
- Microphone in Aisles: One cordless mic every 4-5 rows — shareholders do not come to stage to ask questions.
- Emergency Protocol: Establish distance between stage and audience — shareholders sometimes ask aggressive questions.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR AGMs:
- Scale: Mass catering. Hundreds to thousands present.
- Service style: Buffet system with multiple food counters simultaneously.
- Philosophy: Quick, easy-to-eat items. Minimise plate wastage. Fast service.
- Food items: Items that serve and eat quickly — avoid complex presentations.
- Multiple counters: Separate areas for different food categories to manage crowd flow.
- Water and refreshments: Available throughout the hall, not just at food counters.
- For board members on stage: Separate premium service. Still water, specific preferences as provided by client.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR AGMs (with reasoning):
1. Large-Scale AV & Stage Vendor — Critical. Very large stage, giant LED wall at back, high-quality sound system delivering clear audio to every corner of the auditorium. Failure here means the entire meeting cannot proceed.
2. Digital Voting & Registration Vendor — Barcode scanners for shareholder entry, electronic voting pads or mobile app support for instant voting. Legal requirement for shareholder meetings.
3. Mass Catering Service — Thousands of people. Must handle high-volume rapid service. Multiple simultaneous food counters.
4. Professional Security & Crowd Management — Managing large crowds, ensuring stage safety, maintaining orderly queue for registration. Trained for corporate crowd behavior.
5. Fabrication & Signage Vendor — Large banners and clear directional signs inside and outside the venue. Shareholders must be guided from entry to registration to hall to washrooms without confusion.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR AGMs:
Entertainment is limited — this is primarily a legal and financial meeting.
1. Professional Anchor / Moderator — Understands legal terminology and corporate governance. Correctly relays audience questions to board members. Critical for procedural integrity.
2. National Anthem Singer — AGMs often begin with National Anthem. Professional singer or small choir group.
3. String Quartet — Light instrumental music during registration arrival and post-meeting lunch. Non-intrusive, professional atmosphere.
4. Corporate Filmmaker — Creates an impactful video of the company's journey throughout the year. Displayed on stage before chairman's address.
Note: Keep entertainment minimal. This is a governance event, not a celebration.
"""

PERSONALIZATION_QUESTIONS = [
    "What is the expected shareholder attendance — an approximate count? This determines venue size, catering scale, and registration counter requirements.",
    "Do any significant shareholder groups speak regional languages? We can arrange translation headphones or interpreters for Hindi, Tamil, Telugu, Bengali, or other regional languages.",
    "Could you share the seating sequence for board members on stage, along with their name plate requirements and any dietary preferences for the stage service?",
    "What would you like to include in the shareholder welcome kit — annual report copy, pen, notepad, small gift or souvenir? We can coordinate printing and assembly.",
    "Are there a significant number of senior citizen shareholders? We will arrange dedicated seating, wheelchair access, and priority registration lanes accordingly.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — AGM:
05:00 AM — Final testing of stage, sound system, LED wall, and backup power check
07:30 AM — Registration staff briefing and security team positioning
08:30 AM — Shareholders begin arriving; registration desks go live
09:30 AM — Hall doors open; background corporate film starts playing on LED wall
10:00 AM — Formal start of meeting; chairman's address
12:00 PM — Q&A session and digital voting process
01:30 PM — Meeting wrap-up; mass buffet lunch begins for all shareholders
03:00 PM — Venue clearance; confidential feedback collection
"""
