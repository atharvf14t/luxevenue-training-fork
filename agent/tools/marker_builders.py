"""
Build the exact marker strings consumed by the Next.js frontend (MessageBubble.tsx).
Schema must match tools.ts in the Next.js codebase.
"""
import json
from typing import Any


def build_venue_cards_marker(venues: list[dict], guest_count: int) -> str:
    payload = {
        "venues": [
            {
                "name": v["name"],
                "city": v["city"],
                "state": v["state"],
                "capacity": v["capacity"],
                "rooms": v["rooms"],
                "priceMin": v["pricePerDayMin"],
                "priceMax": v["pricePerDayMax"],
                "style": v["venueStyle"],
                "url": v["googleUrl"],
                "totalMin": guest_count * v["pricePerDayMin"],
                "totalMax": guest_count * v["pricePerDayMax"],
            }
            for v in venues
        ],
        "guestCount": guest_count,
    }
    return f"[VENUE_CARDS: {json.dumps(payload)}]"


def build_menu_cards_marker(
    venue_name: str,
    city: str,
    guest_count: int,
    price_min: int,
    price_max: int,
) -> str:
    payload = {
        "venueName": venue_name,
        "city": city,
        "guestCount": guest_count,
        "priceMin": price_min,
        "priceMax": price_max,
    }
    return f"[MENU_CARDS: {json.dumps(payload)}]"


def build_artist_cards_marker(category: str, artists: list[dict]) -> str:
    payload = {"category": category, "artists": artists}
    return f"[ARTIST_CARDS: {json.dumps(payload)}]"


def build_vendor_cards_marker(category: str, vendors: list[dict]) -> str:
    payload = {"category": category, "vendors": vendors}
    return f"[VENDOR_CARDS: {json.dumps(payload)}]"


def build_chips_marker(options: list[str]) -> str:
    return f"[CHIPS: {' | '.join(options)}]"


def build_booking_total_marker(items: list[dict[str, Any]], total: int) -> str:
    payload = {"items": items, "total": total}
    return f"[BOOKING_TOTAL: {json.dumps(payload)}]"
