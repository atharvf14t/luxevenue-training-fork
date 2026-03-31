"""
Knowledge base for Leadership Summit Agent.
Source: Corporate_Event_English_Translation.pdf
"""

AGENT_TYPE = "leadership_summit"
EVENT_LABEL = "Leadership Summit"

TONE = """
You are the LuxeVenue AI Concierge specialising in Leadership Summits.
Your communication style: Visionary, intelligent, and inspiring.
Don't just offer options — suggest strategies. Position the client's brand as a thought leader.
You understand future trends, executive psychology, and the power of well-designed experiences.
Always highlight networking and collaboration opportunities. Guide the client on how to enhance event impact.
Confident, forward-thinking, and articulate. Make the client feel that their summit will define the industry.
Never use emojis. Be inspiring but precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR LEADERSHIP SUMMITS:
- Atmosphere: High-profile, intellectual, and inspiring. Major industry figures, CEOs, and visionaries gather to discuss the future.
- Scale: Medium to large. Main stage for keynote speeches, breakout rooms for focused discussions.
- Purpose: Thought leadership and premium networking.
- Decor designed for comfort and face-to-face conversation.
- Duration: 1 to 2 days. Tuesday to Thursday. Registration 8:30–9:00 AM. Main sessions end by 5 PM. Networking cocktail dinner after.
- Key features to recommend:
  BASIC SET:
  * Immersive Entry: Digital tunnels or art installations that immediately immerse guests in the event theme
  * Themed Lounges: Separate networking zones with modern furniture, brand colors, and charging stations
  * Dynamic Stage Design: Stage that changes with light cues and digital backgrounds per session mood
  * Sustainable Decor: Eco-friendly materials and live plants — trending preference in corporate circles
  DETAILED SET:
  * Digital Immersive Tunnel: Sensors greet each guest by name on screen as they walk through, or display milestones
  * Tech-Forward Stage: Minimalist stage with holographic displays or curved LED screens — speakers' presentations appear 3D
  * Networking Lounges: Cozy, stylish seating with high-speed internet and multiple charging stations
  * Kinetic Art Installations: Moving art pieces at venue center representing the summit theme (growth, innovation)
  * Branding Monoliths: Tall sleek backlit pillars that serve as both branding and directional signage

INSIDER KNOWLEDGE (not on Google — use to demonstrate thought leadership):
- Speaker Buffer: Always add 10-minute buffer between sessions — prominent leaders frequently overrun
- Privacy Pods: Place small soundproof pods at the venue so leaders can take urgent calls without leaving the event
- Cognitive Scheduling: Heaviest strategic sessions in the morning. Post-lunch sessions must be interactive workshops — people remain active
- Social Media Command Center: Suggest a dedicated team live-sharing leaders' key quotes on LinkedIn and X in real-time
- The 90-Minute Rule: No single session longer than 90 minutes — leaders have short attention spans and need cognitive breaks
- Silent Networking Zone: Reserve one corner completely quiet — no calls, no conversation. Leaders can decompress.
- Graphic Recording: Suggest a digital artist live-drawing key points of each session — visible on a screen in real-time
- Post-Event Strategy: Within 24 hours of summit ending, each attendee should receive a digital folder with session summaries and networking contacts
- Speaker Management: Two competing CEOs should never be placed on the same panel without prior consent
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR LEADERSHIP SUMMITS:
- Philosophy: Gourmet and light. Touch of global cuisine. Reflects the international profile of attendees.
- Networking lunch concept: An industry expert or topic leader hosts each table. The table itself becomes a micro-conversation forum.
- Service style: Plated for formal sessions. Stations and light bites during networking periods.
- Morning: Organic juices, wellness options (coconut water, green smoothies), premium coffee bar
- Breaks: Light protein-rich snacks, fresh fruit, dark chocolate — brain fuel
- Networking cocktail dinner: Open bar with premium spirits, global fusion appetizers, plated main course
- Dietary inclusivity: Always ask about dietary restrictions early — a mix of global attendees means diverse requirements
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR LEADERSHIP SUMMITS (with reasoning):
1. Premium AV & Tech Vendor — Seamless live streaming is essential. The summit reaches a global audience. Zero latency, professional-grade audio, multi-camera setup.
2. Experience Designer — Transforms the hall into an immersive, branded environment. The venue must reflect the client's story and vision for the future.
3. High-End Hospitality & Catering — Gourmet and light with a touch of global cuisine. The quality of food and service reflects the brand's positioning.
4. VIP Transport & Personal Assistants — Luxury cars and dedicated personal assistants for prominent speakers and VVIP guests.
5. Digital Engagement Partner — Manages the event app, real-time polling, live Q&A, and audience engagement. Ensures the summit feels interactive and modern.
"""

ARTIST_KNOWLEDGE = """
RECOMMENDED ARTISTS FOR LEADERSHIP SUMMITS (with reasoning):
1. Keynote Speakers — The summit's biggest draw. Global leaders, industry veterans, or visionary thinkers. Their presence defines the event's credibility.
2. Motivational Speakers or Authors — Share new perspectives and challenge the audience to think differently. Ideal for mid-summit inspiration.
3. Stand-up Comedian (Corporate Style) — To lighten the atmosphere during the evening dinner. Must be clean, intelligent, C-suite appropriate humour.
4. Live Jazz or Fusion Band — Sophisticated background during the cocktail networking hour. Reinforces the premium, international feel of the summit.
"""

PERSONALIZATION_QUESTIONS = [
    "Could you share your top 10 VIP attendees — their names, organisations, and key professional interests? We will design personalised touchpoints to make their experience memorable.",
    "What is the overarching theme of this summit? The theme should be woven into every element — from the immersive entry experience to the stage design to the networking materials.",
    "What is your organisation's 3-year vision that you would like this summit to communicate? We can help script the narrative arc of the event to land that message powerfully.",
    "Could you share the complete list of keynote speakers and their session topics? This helps us design the stage transitions and cognitive flow across the day.",
    "Are there any dietary preferences, wellness requirements, or cultural considerations for your key attendees? (For example, morning yoga sessions, specific organic juice preferences, or halal requirements.)",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Leadership Summit:
06:00 AM — Technical dry run and teleprompter check for all speakers
08:00 AM — High-tech registration with facial recognition or QR code entry
09:00 AM — Powerful opening film and keynote address
11:30 AM — Fireside chats (informal, in-depth conversation between two prominent leaders)
01:00 PM — Networking lunch with industry expert host at each table
02:30 PM — Interactive breakout sessions for brainstorming
04:30 PM — Closing keynote and future vision announcement
06:00 PM — Cocktail networking dinner with live jazz or fusion music
"""