"""
Knowledge base for Product Launch Agent.
Source: Corporate_Event_English_Translated.pdf
"""

AGENT_TYPE = "product_launch"
EVENT_LABEL = "Product Launch"

TONE = """
You are the LuxeVenue AI Concierge specialising in Product Launches.
Your communication style: Futuristic, high-energy, and visionary. Speak like an expert strategist who deeply understands technology and branding.
Generate excitement and guide the client on new digital trends and creative concepts that will make their launch unforgettable.
Always focus on innovation, impact, and wow factor. Suggest ideas that can make the event go viral.
Never use emojis. Be bold and precise.
"""

VENUE_KNOWLEDGE = """
VENUE REQUIREMENTS FOR PRODUCT LAUNCHES:
- Atmosphere: Futuristic, high-tech, and premium. Purpose: generate excitement and build brand authority. Colors: deep black, gold, and white — makes the product look expensive and special.
- Experience zones: Guests can see the product up close and understand its features through 3D walkthroughs or VR.
- Duration: 2 to 3 hours total. The main product reveal segment is only 15 to 20 minutes. Timing: 11 AM for media/journalists (gives full day for news coverage); 7 PM for a grand launch gala.
- Key features to recommend:
  BASIC SET:
  * High-End AV and Curved LED Wall: Large seamless LED wall for product videos and dramatic reveal moments
  * Experience Zone: Premium display stands and interactive booths where guests can touch and feel the product
  * Hydraulic Lift or Smoke Screen Reveal: Dramatic product reveal mechanism on stage
  * Futuristic Lab Look: Glow-in-the-dark graphics and minimalist furniture giving the hall a gallery or lab aesthetic
  DETAILED SET:
  * Anamorphic 3D Video Wall: Seamless LED wall with anamorphic 3D videos that make the product appear to come out of the screen
  * Matterport 3D and VR Zone: Separate area where guests experience the product in a virtual world before the physical reveal
  * Transparent OLED Display Boxes: Product placed inside boxes made of transparent OLED screens — digital features run on the screen while the physical product is visible through it
  * 3D Table Projection Mapping: Projection from ceiling onto each guest's round table — the product's story plays in 3D light and shadow directly on the table surface (premium wow factor)
  * Kinetic LED Ceiling Architecture: Thousands of small LED balls on motorized strings that form a 3D shape of the product in the air during the reveal moment
  * Hybrid VR and Physical Unboxing: VR headsets placed at each VIP seat — guests experience the product virtually before the physical reveal, stage set in North-East direction per Vastu
  * Silent Sensory Launch: Completely dark ballroom, noise-cancelling headphones for every guest, binaural 3D audio — 100% attention on the product

STAGE AND ROOM DESIGN:
- Stage orientation: North-East direction (Vastu — most auspicious for new endeavors and growth)
- Temperature: Reduce room temperature by 2 degrees during the product reveal — cooler environment increases focus and excitement level
- Social media command center: A dedicated team at the venue for live social media updates immediately after the reveal
- 3D walkthrough screen lighting: Must not reflect from ambient lights — clarity and contrast are critical for immersion
- Always have a backup plan: If there is a technical glitch or mechanical delay during the reveal, a fallback sequence must be ready

INSIDER KNOWLEDGE (not on Google — demonstrate expertise):
- The 2-Degree Temperature Drop: Lower the room temperature by 2 degrees right before the reveal — it heightens focus and amplifies excitement
- North-East Vastu Orientation: Placing the stage and reveal mechanism in the North-East direction is considered the most auspicious for new beginnings — suggest this to clients who value Vastu
- Social Media Command Center: A dedicated team stationed at the venue posts live updates the moment the reveal happens — every second of delay costs viral momentum
- Always Have a Backup Plan: Hydraulic lifts and smoke machines have mechanical failure rates — always brief the tech team on the fallback reveal sequence
- Silent Sensory Logic: Complete darkness + binaural audio eliminates every distraction — the product receives 100% of every guest's attention, creating the most immersive reveal possible
"""

MENU_KNOWLEDGE = """
MENU GUIDANCE FOR PRODUCT LAUNCHES:
- Philosophy: Food must match the brand's premium image. It should not distract from the product experience.
- Service style: Live counters and quick snacks — keeps guests mobile and allows them to move between experience zones freely.
- Morning launch (media): Networking high-tea served after the experience zone opens (around 1:30 PM).
- Evening gala: Light gourmet dinner after the reveal and keynote speech.
- VIP media kits: Prepare personalized food and beverage arrangements for key influencers and media house representatives.
- Dietary requirements should be collected in advance from all confirmed guests.
"""

VENDOR_KNOWLEDGE = """
RECOMMENDED VENDORS FOR PRODUCT LAUNCHES (with reasoning):
1. Special Reveal and Tech Vendor — Hydraulic lifts, smoke effects, and digital countdown screens. The reveal moment is the centrepiece of the entire event — it must be executed flawlessly with a tested backup plan.
2. High-End AV and LED Partner — Large curved LED walls and concert-level sound system for anamorphic 3D video and impactful audio. The product's visual and sound presentation determines the audience's first emotional response.
3. PR and Media Agency — Invites influencers and press, manages live coverage, and coordinates the social media command center. Without media amplification, the launch's reach is limited to the room.
4. Experience Zone Fabricator — Premium display stands, interactive booths, and Matterport 3D or 360-degree view systems. This is where guests form their lasting impression of the product after the reveal.
5. Gourmet Catering Service — Brand-aligned food with live counters and quick snacks. Food should enhance the premium atmosphere, not distract from the product experience.
  For high-tech launches, also consider:
  - 3D Projection Mapping Experts (animation studio + high-lumens projector riggers)
  - Immersive VR and 3D Content Developers (VR headset rental + Matterport content)
  - Kinetic Rigging and Lighting Programmers (specialized engineers for ceiling installations)
  - Transparent OLED Display Suppliers (hardware + UI/UX programming)
  - Silent Sensory Audio Engineers (binaural 3D sound mix + RF headphone hardware)
  - International Level Showcaller (technical director who gives live cues to all vendors simultaneously)
"""

ARTIST_KNOWLEDGE = """
ARTIST GUIDANCE FOR PRODUCT LAUNCHES:
1. Tech-Themed Performers — LED light dancers, holographic artists, or laser show performers. They fill the launch moment with energy and create the visual drama that makes the reveal feel like an event.
2. Tech Influencer or Celebrity Guest — Unveils the product on stage for the first time and shares their live experience. Their social media reach amplifies the launch beyond the room instantly.
3. Sharp Corporate Emcee — Speaks the brand's language, controls the reveal countdown, and keeps audience excitement at peak level throughout the event.
4. Modern Jazz or Electronic Band — Plays upbeat background music that matches the futuristic and innovative theme — heard during networking and the experience zone segment.
"""

PERSONALIZATION_QUESTIONS = [
    "What is the product's core philosophy and its biggest USP (unique selling point)? The entire event — stage design, AV content, emcee script, and experience zone — should revolve around this single idea.",
    "Who are the key influencers and media houses attending? We will prepare personalised media kits for each, and brief the PR team on their areas of interest so coverage is targeted and impactful.",
    "What is the brand's legacy and 5-year vision? This shapes the event's theme, the brand story video, and the overall narrative so everything feels coherent and forward-looking.",
    "Does your team follow any numerology or Vastu principles? If so, the exact launch minute, stage orientation (North-East), and entry direction can all be planned accordingly in advance.",
    "What reveal format excites you most — a classic stage reveal with hydraulic lift and smoke effects, a Hybrid VR unboxing experience, the Silent Sensory launch, or the 3D Table Projection concept? Each guest can also receive a personalised miniature model or digital souvenir of the product.",
]

OPERATIONAL_TIMELINE = """
OPERATIONAL TIMELINE — Product Launch:
08:00 AM — Final technical rehearsal of stage reveal mechanism and LED wall
11:00 AM — Welcome for media and influencers with red carpet photo-op
11:45 AM — High-definition 3D brand story video screening; countdown begins
12:00 PM — Main Product Reveal moment with optimal light and sound
12:20 PM — Keynote speech and live product demonstration on stage
01:00 PM — Experience zone opens; guests touch and feel the product
01:30 PM — Networking high-tea and Q&A session with media
03:00 PM — Gift distribution and digital feedback collection; event wrap-up
"""
