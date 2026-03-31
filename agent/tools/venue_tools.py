"""Query the Venue table (same Postgres DB used by Prisma in Next.js)."""
from core.database import get_pool


async def search_venues(
    city: str,
    guest_count: int = 100,
    venue_style: str | None = None,
    limit: int = 8,
) -> list[dict]:
    pool = await get_pool()

    if venue_style and venue_style != "any":
        query = """
            SELECT id, name, city, state, capacity, rooms,
                   "pricePerDayMin", "pricePerDayMax", "venueStyle", "googleUrl"
            FROM "Venue"
            WHERE city ILIKE $1
              AND capacity >= $2
              AND "venueStyle" = $3
            ORDER BY "pricePerDayMin" ASC
            LIMIT $4
        """
        rows = await pool.fetch(query, f"%{city}%", guest_count, venue_style, limit)

        if not rows:
            # Fallback: drop style filter
            rows = await _search_without_style(pool, city, guest_count, limit)
    else:
        rows = await _search_without_style(pool, city, guest_count, limit)

    return [dict(r) for r in rows]


async def _search_without_style(pool, city: str, guest_count: int, limit: int) -> list:
    query = """
        SELECT id, name, city, state, capacity, rooms,
               "pricePerDayMin", "pricePerDayMax", "venueStyle", "googleUrl"
        FROM "Venue"
        WHERE city ILIKE $1
          AND capacity >= $2
        ORDER BY "pricePerDayMin" ASC
        LIMIT $3
    """
    return await pool.fetch(query, f"%{city}%", guest_count, limit)
