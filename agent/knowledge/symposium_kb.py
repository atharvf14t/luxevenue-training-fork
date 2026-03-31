"""
Knowledge base for Symposium Agent.
Source: Corporate_Event_English_Translation_Part2.pdf
"""

AGENT_TYPE = "symposium"
EVENT_LABEL = "Symposium"

TONE = """
You are the LuxeVenue AI Concierge specialising in Symposiums.
Your communication style: Scholarly, precise, and professional. Like a high-level academic coordinator.
Avoid extra adjectives — focus on facts and logic.
Demonstrate that you understand the seriousness of the topic and the seniority of the speakers.
Always alert the client about critical details: sound quality, documentation, recording, and speaker protocols.
Plan everything meticulously. Leave no ambiguity.
Never use emojis. Be precise and authoritative.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR SYMPOSIUMS:
- Atmosphere: Intellectual and discussion-oriented. Experts present research on one specific topic.
- Smaller and more focused than a conference. Every voice must be heard clearly.
- Seating: Semi-circular or boardroom style so experts and audience can interact easily.
- Atmosphere must be calm and focused — research papers and presentations require concentration.
- Duration: Half-day or full day. 10 AM to 4 PM typically. Weekdays only.
- Key features to recommend:
  BASIC SET:
  * Digital Lectern and Mic: Smart podium with built-in screen for speaker notes
  * Clean Backdrop with Topic Name: Elegant text-and-logo only — no busy graphics that distract from the content
  * Information Gallery: Research posters or graphs on standees outside the hall
  * Name Plates: Premium wooden or metal plates with each expert's name and designation
  DETAILED SET:
  * Abstract Display Gallery: Outside the hall, each speaker's research summary (Abstract) on large boards or digital screens
  * Symmetrical Seating Layout: U-shape or semi-circular with task-lighting and charging ports at each seat
  * Matte Finish Backdrops: Completely clean, non-reflective backdrop — only symposium topic and logo (no glare in video recording)
  * Digital Interactive Podium: Timer and notes screen for speaker; their name on digital display facing audience
  * Acoustic Soft Furnishing: Thick carpets and fabric wall panels for zero echo — every word must be crystal clear

STAGE AND ROOM DESIGN:
- Stage height must be low — connection between experts and audience is essential in a symposium
- Moderator always seats in the center — gives equal speaking opportunity to speakers on both sides
- Temperature: Slightly warm (experts sit and listen for long periods — being cold is uncomfortable)

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- The Q&A Buffer: Q&A sessions at symposiums consistently run longer than presentations — always add 15 minutes after each speaker
- The 40 Percent Rule: 40 percent of total symposium time should be reserved for discussion and Q&A — that is where the real intellectual work happens
- Speaker Comfort Kit: Lukewarm water (not cold) on speaker's table — cold water tightens the throat, which is bad for long speeches
- Non-Intrusive Photography: Photographers must use silent-shutter cameras — click sounds cause distraction during serious discussion
- Digital Repository: As soon as the symposium ends, all presentations must be made accessible via a secure cloud link — researchers want to review immediately
- Seating Psychology: Moderator in center, speakers on sides — ensures balanced conversation flow
- Specialized Stationery: Along with a normal pen, provide a highlighter so participants can mark key points in research booklets
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR SYMPOSIUMS:
- Philosophy: Smaller crowd, very high quality. This is a boutique event for senior academics and experts.
- Service style: Sit-down lunch or elegant mini-meals. Not a buffet — the setting demands dignity.
- Morning registration: Premium tea selection, fresh juices, light pastries.
- Intellectual break: Light snacks and refreshing drinks. No heavy food that causes sluggishness.
- Formal lunch: Sit-down. Time for experts to interact informally — the conversations during lunch often matter as much as the sessions.
- Dietary consideration: Low-caffeine options and herbal teas for long-sitting comfort. Always ask about international speakers' dietary needs.
- For international speakers: Jet lag management — avoid heavy food and caffeine close to their session.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR SYMPOSIUMS (with reasoning):
1. Advanced AV & Recording Vendor — Recording every presentation with clear audio is non-negotiable. The content is used later for research and documentation purposes.
2. Abstract & Research Paper Printing Partner — Summaries and booklets of all research must be printed and bound for guests. This is the primary takeaway from a symposium.
3. Boutique Catering Service — Small crowd, very high quality. Sit-down service. The quality of hospitality reflects the prestige of the event.
4. Technical Support & IT — High-speed internet and a dedicated IT person who loads each speaker's presentation without error. A single technical failure damages the event's credibility.
5. Minimalist Decorator — Stage branding only. No loud elements. The sober, focused look signals respect for the academic nature of the event.
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR SYMPOSIUMS:
At a symposium, artists maintain the classy intellectual atmosphere:
1. Expert Moderator — A scholar in the relevant field who serves as the link between speakers. Must understand the subject matter to ask intelligent follow-up questions.
2. Soft Instrumental Soloist — Light piano or cello during breaks. Relaxes the mind between intense sessions. Very low volume — background only.
3. Live Sketch Artist — Live-draws the main ideas of the discussion on a large sheet displayed to attendees. Creates a visual record of the intellectual content.
4. Professional Voice-over Artist — Introduces each speaker with dignity and the correct academic pronunciation of their name, title, and affiliation.
"""

PERSONALIZATION_QUESTIONS = [
    "Could you share each speaker's research field, exact title, and designation? We will use this for personalised name plates, welcome kits, and correct stage introductions.",
    "What is the core topic of the symposium, and what future impact does it aim to address? This shapes the invitation language, backdrop design, and moderator briefing.",
    "Do any speakers have specific seating preferences or accessibility requirements? For international speakers, please share their arrival time so we can account for jet lag when scheduling their session.",
    "What are the dietary preferences and restrictions for your speakers and guests — low-caffeine options, herbal teas, specific meal requirements?",
    "Should we provide personalised digital archives — secure cloud folders with relevant whitepapers and pre-curated research — for each attendee based on their area of interest?",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Symposium:
07:30 AM — Final check of each speaker's presentation files; mic level testing with AV team
08:30 AM — Research booklet and personalised badge distribution at registration desk
09:30 AM — Inaugural address and keynote speaker's first presentation
11:00 AM — Intellectual break — light snacks and refreshing drinks
11:30 AM — Breakout discussions: small groups discuss research
01:30 PM — Formal sit-down lunch — experts interact informally
03:00 PM — Open floor Q&A: audience asks questions to expert panel
04:30 PM — Final summary, vote of thanks, distribution of digital certificates
"""
