"""Query the Artist table or return proxy data if DB is sparse."""
from core.database import get_pool

# Proxy data mirrors tools.ts in Next.js — used as fallback
PROXY_ARTISTS = [
    {
        "name": "DJ Aqeel",
        "type": "DJ / Music Director",
        "city": "Mumbai",
        "description": "Bollywood's legendary DJ with 20+ years. Iconic at India's biggest weddings & corporate galas.",
        "priceMin": 500000,
        "priceMax": 1500000,
    },
    {
        "name": "Anchor Anupriya Kapoor",
        "type": "Professional Emcee",
        "city": "Mumbai",
        "description": "India's top bilingual emcee for luxury weddings & corporate events. Known for warmth and wit.",
        "priceMin": 75000,
        "priceMax": 200000,
    },
    {
        "name": "Kailash Kher & Kailasa",
        "type": "Live Artist / Singer",
        "city": "Mumbai",
        "description": "Sufi-rock legend. Electrifying live performances that bring profound emotion to events.",
        "priceMin": 3000000,
        "priceMax": 8000000,
    },
    {
        "name": "Shankar Mahadevan Live Band",
        "type": "Live Band",
        "city": "Mumbai",
        "description": "Grammy-winning composer with his full live ensemble. Bollywood, Sufi & classical fusion.",
        "priceMin": 5000000,
        "priceMax": 15000000,
    },
    {
        "name": "Rahul Subramanian",
        "type": "Stand-up Comedian",
        "city": "Mumbai",
        "description": "Sharp observational comedy in English & Hindi. Crowd favourite at corporate parties.",
        "priceMin": 300000,
        "priceMax": 800000,
    },
]

# Corporate-specific proxy artists for relevant agent types
CORPORATE_PROXY_ARTISTS = [
    {
        "name": "Anand Mahindra Jazz Quartet",
        "type": "Jazz Band",
        "city": "Mumbai",
        "description": "Premium jazz ensemble for corporate networking dinners. Four-piece band with saxophone, piano, bass, and drums. Sophisticated background music for elite boardroom events.",
        "priceMin": 150000,
        "priceMax": 400000,
    },
    {
        "name": "Aakash Mehta",
        "type": "Corporate Stand-up Comedian",
        "city": "Mumbai",
        "description": "India's leading corporate comedian. Clean, intelligent humour tailored for C-suite audiences. Performs at leadership summits and award nights.",
        "priceMin": 200000,
        "priceMax": 600000,
    },
    {
        "name": "Suhail Doshi (Mentalist)",
        "type": "Mentalist / Illusionist",
        "city": "Mumbai",
        "description": "India's premier corporate mentalist. Mind-reading and logic-based illusions. Perfect ice-breaker for strategy meets and power dinners.",
        "priceMin": 100000,
        "priceMax": 350000,
    },
    {
        "name": "Violin Maestro — Balabhaskar Style",
        "type": "Instrumental Soloist",
        "city": "Mumbai",
        "description": "Classical violin soloist for executive networking. Elegant background music for boardroom arrivals and formal lunches.",
        "priceMin": 50000,
        "priceMax": 150000,
    },
    {
        "name": "String Quartet India",
        "type": "String Quartet",
        "city": "Delhi",
        "description": "Formal chamber music ensemble for AGMs and board meetings. Four-piece group with violin, viola, and cello. Repertoire includes classical and light contemporary.",
        "priceMin": 120000,
        "priceMax": 300000,
    },
    {
        "name": "Anchor Anupriya Kapoor",
        "type": "Professional Emcee",
        "city": "Mumbai",
        "description": "India's top bilingual emcee for corporate events. Known for composure and legal event scripting for AGMs and leadership summits.",
        "priceMin": 75000,
        "priceMax": 200000,
    },
]


async def get_artists_for_event(agent_type: str) -> list[dict]:
    pool = await get_pool()

    # Try DB first
    try:
        rows = await pool.fetch(
            'SELECT id, name, description, city, state, "artistType", "priceRangeMin", "priceRangeMax", "googleUrl" FROM "Artist" LIMIT 8'
        )
        if rows:
            return [
                {
                    "name": r["name"],
                    "type": r["artistType"],
                    "city": r["city"],
                    "description": r["description"],
                    "priceMin": r["priceRangeMin"],
                    "priceMax": r["priceRangeMax"],
                }
                for r in rows
            ]
    except Exception:
        pass

    # Fallback: use corporate proxy artists for all corporate event types
    return CORPORATE_PROXY_ARTISTS
