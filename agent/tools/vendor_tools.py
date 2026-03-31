"""Query the Vendor table or return proxy data if DB is sparse."""
from core.database import get_pool

PROXY_VENDORS = [
    {
        "name": "Shaadi Décor by Isha",
        "type": "Premium Decorator",
        "city": "Mumbai",
        "description": "Award-winning luxury floral & fabric decorator. Known for elaborate designs and signature floral installations.",
        "priceMin": 500000,
        "priceMax": 3000000,
    },
    {
        "name": "Wizcraft International",
        "type": "AV Production House",
        "city": "Mumbai",
        "description": "India's premier event production company. Complete AV, staging, LED walls, artist management.",
        "priceMin": 2000000,
        "priceMax": 20000000,
    },
    {
        "name": "Royal Valet & Security",
        "type": "Valet & Security Services",
        "city": "New Delhi",
        "description": "Professional valet parking & event security. Formal attire, real-time car tracking & discreet security.",
        "priceMin": 80000,
        "priceMax": 300000,
    },
]

CORPORATE_PROXY_VENDORS = [
    {
        "name": "Wizcraft International",
        "type": "AV Production House",
        "city": "Mumbai",
        "description": "India's premier corporate AV production. LED walls, noise-cancellation mics, 4K video conferencing, and seamless live streaming for corporate events.",
        "priceMin": 2000000,
        "priceMax": 20000000,
    },
    {
        "name": "ClearTrail Secure IT",
        "type": "Secure IT & Infrastructure",
        "city": "Bangalore",
        "description": "Corporate cybersecurity and IT infrastructure for events. Encrypted 1 Gbps private networks, digital voting systems, and bug-sweeping services for boardrooms.",
        "priceMin": 150000,
        "priceMax": 800000,
    },
    {
        "name": "LuxeMotion Executive Transport",
        "type": "Luxury Transport Service",
        "city": "Mumbai",
        "description": "Premium executive ground transport. NDA-signed chauffeurs, Mercedes and BMW fleet, airport-to-venue VVIP transfers for corporate events.",
        "priceMin": 50000,
        "priceMax": 300000,
    },
    {
        "name": "Elite Corporate Catering Co.",
        "type": "Premium Catering Service",
        "city": "Mumbai",
        "description": "White-glove corporate catering. Pre-plated service, silent staff protocol, and curated menus for boardrooms and strategy meets.",
        "priceMin": 500000,
        "priceMax": 3000000,
    },
    {
        "name": "SentryShield Security",
        "type": "Professional Security",
        "city": "Delhi",
        "description": "Discreet plainclothes security for high-profile corporate events. Covers VVIP protection, crowd management for AGMs, and access control.",
        "priceMin": 100000,
        "priceMax": 500000,
    },
    {
        "name": "TranscribeNow India",
        "type": "Transcription & Recording Service",
        "city": "Bangalore",
        "description": "Professional stenographers and AI-powered meeting transcription. Specialised in board meetings and AGMs. Produces verbatim minutes within 24 hours.",
        "priceMin": 25000,
        "priceMax": 100000,
    },
    {
        "name": "GreenLeaf Corporate Florals",
        "type": "Luxury Floral Decorator",
        "city": "Mumbai",
        "description": "Premium minimalist floral arrangements for boardrooms. White lilies, orchids, and air-purifying plants. Low-profile centerpieces that stay below eye level.",
        "priceMin": 50000,
        "priceMax": 250000,
    },
    {
        "name": "DigEngage Events",
        "type": "Digital Engagement Partner",
        "city": "Mumbai",
        "description": "Event app development, real-time polling, Q&A management, and live audience engagement tools for leadership summits and AGMs.",
        "priceMin": 200000,
        "priceMax": 800000,
    },
    {
        "name": "FabriCraft Fabrication",
        "type": "Fabrication & Signage Vendor",
        "city": "Delhi",
        "description": "Large-scale fabrication for AGMs and conferences. Stage structures, grand entrance arches, registration bays, directional signage, and branding totems.",
        "priceMin": 500000,
        "priceMax": 5000000,
    },
]


async def get_vendors_for_event(agent_type: str) -> list[dict]:
    pool = await get_pool()

    try:
        rows = await pool.fetch(
            'SELECT id, name, description, city, state, "vendorType", "priceRangeMin", "priceRangeMax", "googleUrl" FROM "Vendor" LIMIT 8'
        )
        if rows:
            return [
                {
                    "name": r["name"],
                    "type": r["vendorType"],
                    "city": r["city"],
                    "description": r["description"],
                    "priceMin": r["priceRangeMin"],
                    "priceMax": r["priceRangeMax"],
                }
                for r in rows
            ]
    except Exception:
        pass

    return CORPORATE_PROXY_VENDORS
