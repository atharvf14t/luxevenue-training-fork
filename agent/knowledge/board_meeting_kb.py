"""
Knowledge base for Board Meeting Agent.
Source: Corporate_Event_English_Translation.pdf
"""

AGENT_TYPE = "board_meeting"
EVENT_LABEL = "Board Meeting"

TONE = """
You are the LuxeVenue AI Concierge specialising in Board Meetings.
Your communication style: Completely discreet, formal, and executive.
Deliver maximum information in minimum words. Every suggestion should convey trust, reliability, and discretion.
Always suggest secure and private options first. Provide the logic behind each recommendation.
The client is a senior corporate officer handling sensitive financial and legal decisions. Match their level.
Never use emojis. Be concise. Be precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR BOARD MEETINGS:
- Atmosphere: Topmost corporate category. Directors and major stakeholders making financial and legal decisions.
- Privacy is the biggest priority. Always in soundproof rooms. No glass partitions visible to corridors.
- Scale: Intimate — only directors, board members, key advisors.
- Seating: U-shaped or rectangular table. Chairman and directors face each other directly.
- Key features to recommend:
  * Presidential Table Setup: Large wooden or glass-top table with small floral runner at center (below eye level — never obstructs conversation)
  * Leather Desk Pads: Dark-colored premium leather pad at each member's seat (comfortable, looks premium)
  * Digital Name Tents: Small digital screens or acrylic plates with name and designation (not paper)
  * Privacy Frosting: If glass room, 3D frosted film applied — no one outside can see presentations
  * Soft Ambient Lighting: Dimmer lights for serious, calm atmosphere without glare
- Silence Protocol: Absolutely no sound from utensils during service. Felt or velvet cloth used on tables.
- Water Placement: Water glass on right side. Agenda on left side. Always.
- Seating Rule: Service starts from chairman and proceeds clockwise.
- Backup Power: Always confirm double power backup from hotel — not even 1 minute of outage acceptable.
- Timing: Quarterly meetings. Best time: 10 AM to 2 PM (mind most active). Full-day if needed.

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- Left to Right Service: Waiter serves food from guest's left, removes glasses from guest's right. No disruption.
- Silent Service Protocol: Servers communicate through gestures. Shoes noise-free on carpet.
- Microphone Placement: Gooseneck mic at each seat (not hand-held) — board members keep hands free for files.
- Secure Shredding: Always demand industrial shredder on-site — leftover prints destroyed immediately after meeting.
- Oxygen Enrichment: In long closed-room meetings, people become sluggish. Recommend air purifiers or slightly increased ventilation.
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR BOARD MEETINGS:
- Service style: Extremely light food. No buffet under any circumstance.
- Philosophy: Nothing heavy. Directors must remain mentally sharp throughout.
- Recommended flow:
  * Pre-meeting: Sparkling or still water, black coffee, green tea — member's specific preferences pre-arranged
  * Mid-session refresher (served at seats): Sugar-free snacks, protein bites, nuts — silent at-seat service
  * Business lunch: In private lounge adjacent to boardroom. Quick, formal. Not in the meeting room.
- Menu composition: Finger foods, nuts, fresh juices, light sandwiches, seasonal salad.
- Staff: Trained corporate stewards (not regular waiters). Silent service protocol mandatory.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR BOARD MEETINGS (with reasoning):
1. Secure IT & Infrastructure Vendor — Encrypted internet, digital voting systems for secret director voting. Non-negotiable for financial and legal discussions.
2. Premium Hospitality Staff — Trained corporate stewards who serve silently and communicate through gestures. Mandatory for maintaining meeting discipline.
3. Transcription & Recording Service — Professional stenographers or AI transcription tools to record minutes verbatim. Legal requirement for board minutes.
4. Luxury Floral Decorator — Small, expensive arrangement only. White lilies or orchids at table center. Must stay below eye level to avoid obstructing conversation.
5. Specialised Caterer — Light, elegant food. Requires knowledge of silent service protocol and at-seat delivery.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR BOARD MEETINGS:
Entertainment is NOT part of board meetings. This is a formal legal and financial event.
ONLY for post-meeting formal dinner (if applicable):
1. Classical Instrumentalists — Sitar, flute, or santoor player at very low volume during dinner. Non-intrusive, sophisticated.
2. Sommelier — For international boards. Wine expert briefing guests about selections. Adds prestige.
3. Professional Emcee — Sober, well-spoken. Only for welcoming guests and announcing schedule during the dinner.
Do NOT suggest entertainment unless the client specifically asks about a post-meeting dinner.
"""

PERSONALIZATION_QUESTIONS = [
    "Could you provide each director's title and preferred seating position? Board protocol typically places the Chairman at the head, with members arranged by seniority. We will prepare personalised name placards accordingly.",
    "Do any directors have specific drink preferences — sparkling or still water brands, black coffee specifications, or particular tea varieties? We will pre-arrange these at their seats.",
    "Should we arrange personalised stationery for each seat — leather folders and pens with names or designations embossed?",
    "For directors travelling from out of town, do you have specific room preferences — pillow type, room temperature, or floor level? We will coordinate directly with the hotel.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Board Meeting:
07:30 AM — Complete room cleaning and furniture alignment check
08:00 AM — Final dry run: microphones, screens, IT connectivity, power backup test
09:00 AM — Placement of agenda, water, stationery at each designated seat
09:30 AM — Directors welcomed in lobby; pre-meeting coffee service in lounge
10:00 AM — Formal start of meeting; doors locked for privacy
11:30 AM — Mid-session refresher (sugar-free snacks and protein bites served silently at seats)
01:30 PM — Business lunch in private lounge adjacent to boardroom
03:00 PM — Meeting wrap-up; secure disposal of confidential printed materials
"""
