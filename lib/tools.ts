import { prisma } from './prisma';
import { calculateLiquor } from './liquor-calc';

export interface ToolResult {
  content: string;
}

// ─── Hardcoded proxy data ──────────────────────────────────────────────────

const PROXY_ARTISTS = [
  {
    name: 'DJ Aqeel',
    type: 'DJ / Music Director',
    city: 'Mumbai',
    description:
      "Bollywood's legendary DJ with 20+ years. Iconic at India's biggest weddings & corporate galas. Crafts bespoke sets blending Bollywood hits, retro classics & EDM.",
    priceMin: 500000,
    priceMax: 1500000,
  },
  {
    name: 'Anchor Anupriya Kapoor',
    type: 'Professional Emcee',
    city: 'Mumbai',
    description:
      "India's top bilingual emcee for luxury weddings & corporate events. Known for warmth, wit and ability to electrify any crowd in Hindi & English.",
    priceMin: 75000,
    priceMax: 200000,
  },
  {
    name: 'Kailash Kher & Kailasa',
    type: 'Live Artist / Singer',
    city: 'Mumbai',
    description:
      'Sufi-rock legend behind Teri Deewani & Allah Ke Bande. Electrifying live performances that bring profound emotion to weddings and award nights.',
    priceMin: 3000000,
    priceMax: 8000000,
  },
  {
    name: 'Shankar Mahadevan Live Band',
    type: 'Live Band',
    city: 'Mumbai',
    description:
      'Grammy-winning composer with his full live ensemble. Bollywood, Sufi & classical fusion. Premium entertainment for India\'s most elite events.',
    priceMin: 5000000,
    priceMax: 15000000,
  },
  {
    name: 'Rahul Subramanian',
    type: 'Stand-up Comedian',
    city: 'Mumbai',
    description:
      'Sharp observational comedy in English & Hindi. Crowd favourite at corporate parties, award nights & sangeet nights. Safe, intelligent humour for all audiences.',
    priceMin: 300000,
    priceMax: 800000,
  },
];

const PROXY_VENDORS = [
  {
    name: 'Shaadi Décor by Isha',
    type: 'Premium Decorator',
    city: 'Mumbai',
    description:
      'Award-winning luxury floral & fabric decorator. Known for elaborate mandap designs, enchanting entrances & signature floral installations.',
    priceMin: 500000,
    priceMax: 3000000,
  },
  {
    name: 'Joseph Radhik Photography',
    type: 'Photographer & Cinematographer',
    city: 'Chennai',
    description:
      "India's most celebrated wedding photographer. Featured in Vogue & Harper's Bazaar. Cinematic editorial eye — books 18 months in advance.",
    priceMin: 800000,
    priceMax: 3000000,
  },
  {
    name: 'Wizcraft International',
    type: 'AV Production House',
    city: 'Mumbai',
    description:
      "India's premier event production company. Complete AV, staging, LED walls, artist management & creative concepts for India's biggest events.",
    priceMin: 2000000,
    priceMax: 20000000,
  },
  {
    name: 'SFX India',
    type: 'SFX & Special Effects',
    city: 'Mumbai',
    description:
      'Specialists in cold pyro, confetti cannons, CO₂ jets & grand entry effects. Trained technicians with full safety protocols.',
    priceMin: 100000,
    priceMax: 800000,
  },
  {
    name: 'Royal Valet & Security',
    type: 'Valet & Security Services',
    city: 'New Delhi',
    description:
      'Professional valet parking & event security. Formal attire, real-time car tracking & discreet security for high-profile guests.',
    priceMin: 80000,
    priceMax: 300000,
  },
];

// ─── Tool handler ──────────────────────────────────────────────────────────

export async function handleToolCall(
  toolName: string,
  args: Record<string, unknown>
): Promise<string> {
  switch (toolName) {
    case 'search_venues': {
      const { city, event_type, capacity, venue_type } = args as {
        city: string;
        event_type: string;
        capacity?: number;
        venue_type?: string;
      };

      const where: Record<string, unknown> = {};
      if (city) where.city = { contains: city, mode: 'insensitive' };
      if (venue_type && venue_type !== 'any') where.venueStyle = venue_type;
      if (capacity) where.capacity = { gte: capacity };

      let venues = await prisma.venue.findMany({
        where,
        take: 3,
        orderBy: { pricePerDayMin: 'asc' },
      });

      const guestCount = capacity ?? 100;
      let styleUnavailableNote = '';

      // Fallback: if specific style requested but none found, retry without style filter
      if (venues.length === 0 && venue_type && venue_type !== 'any') {
        const fallbackWhere: Record<string, unknown> = {};
        if (city) fallbackWhere.city = { contains: city, mode: 'insensitive' };
        if (capacity) fallbackWhere.capacity = { gte: capacity };
        venues = await prisma.venue.findMany({
          where: fallbackWhere,
          take: 3,
          orderBy: { pricePerDayMin: 'asc' },
        });
        if (venues.length > 0) {
          styleUnavailableNote = `Note: No ${venue_type} venues are currently available in ${city}. Here are the best available options instead:\n`;
        }
      }

      if (venues.length === 0) {
        return `No venues found in ${city}${capacity ? ` for ${capacity}+ guests` : ''}. Try a nearby city or different guest count.`;
      }

      return `${styleUnavailableNote}[VENUE_CARDS: ${JSON.stringify({
        venues: venues.map((v) => ({
          name: v.name,
          city: v.city,
          state: v.state,
          capacity: v.capacity,
          rooms: v.rooms,
          priceMin: v.pricePerDayMin,
          priceMax: v.pricePerDayMax,
          style: v.venueStyle,
          url: v.googleUrl,
          totalMin: guestCount * v.pricePerDayMin,
          totalMax: guestCount * v.pricePerDayMax,
        })),
        guestCount,
      })}]`;
    }

    case 'show_artists': {
      const { category } = args as { category: string };
      return `[ARTIST_CARDS: ${JSON.stringify({ category, artists: PROXY_ARTISTS })}]`;
    }

    case 'show_vendors': {
      const { category } = args as { category: string };
      return `[VENDOR_CARDS: ${JSON.stringify({ category, vendors: PROXY_VENDORS })}]`;
    }

    case 'calculate_liquor': {
      const { guests_drinking, event_type, drink_type } = args as {
        guests_drinking: number;
        event_type: 'social' | 'corporate' | 'wedding';
        drink_type: 'spirits' | 'beer' | 'both';
      };

      const result = calculateLiquor({
        guestsDrinking: guests_drinking,
        eventType: event_type,
        drinkType: drink_type,
      });

      return result.summary;
    }

    case 'calculate_budget': {
      const { total_budget, guest_count, event_type } = args as {
        total_budget: number;
        guest_count: number;
        event_type: string;
        services_needed?: string[];
      };

      const budgetL = total_budget / 100000;
      const perHead = total_budget / guest_count;

      const breakdown: Record<string, string> = {
        venue: `₹${(budgetL * 0.35).toFixed(1)}L (35%)`,
        decor: `₹${(budgetL * 0.20).toFixed(1)}L (20%)`,
        catering: `₹${(budgetL * 0.25).toFixed(1)}L (25%)`,
        entertainment: `₹${(budgetL * 0.10).toFixed(1)}L (10%)`,
        photography: `₹${(budgetL * 0.05).toFixed(1)}L (5%)`,
        logistics_misc: `₹${(budgetL * 0.05).toFixed(1)}L (5%)`,
      };

      const lines = [
        `**Budget Breakdown for ${event_type} (${guest_count} guests, ₹${budgetL.toFixed(1)}L total)**`,
        `Per head: ₹${Math.round(perHead).toLocaleString('en-IN')}`,
        '',
        ...Object.entries(breakdown).map(([k, v]) => `- **${k.replace(/_/g, ' ')}:** ${v}`),
        '',
        '*These are indicative splits. We can adjust based on your priorities.*',
      ];

      return lines.join('\n');
    }

    case 'generate_decor_image': {
      const { area, color_theme, event_type, style } = args as {
        area: string;
        color_theme: string;
        event_type: string;
        style?: string;
      };

      return `[GENERATE_IMAGE: area="${area}" theme="${color_theme}" event="${event_type}" style="${style ?? 'elegant'}"]`;
    }

    case 'generate_digital_invite': {
      const { event_name, host_names, date, venue, theme_color } = args as {
        event_name: string;
        host_names: string;
        date: string;
        venue: string;
        theme_color?: string;
      };

      return `[GENERATE_INVITE: event="${event_name}" hosts="${host_names}" date="${date}" venue="${venue}" color="${theme_color ?? 'gold'}"]`;
    }

    case 'web_search': {
      const { query } = args as { query: string };

      if (!process.env.SERPER_API_KEY) {
        return `Web search is not configured. Based on my knowledge: searching for "${query}" — please provide your SERPER_API_KEY to enable live web search.`;
      }

      const response = await fetch('https://google.serper.dev/search', {
        method: 'POST',
        headers: {
          'X-API-KEY': process.env.SERPER_API_KEY,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ q: query, num: 5 }),
      });

      if (!response.ok) return 'Web search failed.';
      const data = await response.json() as { organic?: { title: string; link: string; snippet: string }[] };
      const results = data.organic?.slice(0, 5) ?? [];

      return results
        .map((r, i) => `${i + 1}. **${r.title}**\n   ${r.snippet}\n   [Read more →](${r.link})`)
        .join('\n\n');
    }

    default:
      return `Tool "${toolName}" is not implemented.`;
  }
}

// ─── Tool definitions for Azure OpenAI function calling ───────────────────

export const TOOL_DEFINITIONS = [
  {
    type: 'function' as const,
    function: {
      name: 'search_venues',
      description: 'Search for event venues in our database. Returns top 3 results as venue cards.',
      parameters: {
        type: 'object',
        properties: {
          city: { type: 'string', description: 'City to search in' },
          capacity: { type: 'number', description: 'Minimum guest capacity needed' },
          venue_type: {
            type: 'string',
            enum: ['luxury', 'modern', 'heritage', 'any'],
            description: 'luxury = 5-star premium hotels (Taj, Oberoi, ITC, Marriott etc.), modern = contemporary business hotels (Hyatt, Radisson, Novotel etc.), heritage = palace/historical properties',
          },
          event_type: {
            type: 'string',
            enum: ['wedding', 'corporate', 'social', 'destination-wedding'],
          },
        },
        required: ['city', 'event_type'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'show_artists',
      description: 'Show bookable artists for a given category. Returns artist cards with Book buttons.',
      parameters: {
        type: 'object',
        properties: {
          category: {
            type: 'string',
            description: 'Artist category e.g. Emcee, DJ, Live Band, Comedian',
          },
        },
        required: ['category'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'show_vendors',
      description: 'Show enquirable vendors for a given category. Returns vendor cards with Enquire buttons.',
      parameters: {
        type: 'object',
        properties: {
          category: {
            type: 'string',
            description: 'Vendor category e.g. Decorator, Photographer, AV Production',
          },
        },
        required: ['category'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'generate_decor_image',
      description: 'Generate an AI decor mood image for a specific area. Checks user quota before generating.',
      parameters: {
        type: 'object',
        properties: {
          area: { type: 'string', description: 'Area of the venue e.g. entrance, stage, table' },
          color_theme: { type: 'string', description: 'Color theme e.g. gold floral, white minimal' },
          event_type: { type: 'string', description: 'Type of event' },
          style: { type: 'string', description: 'Style e.g. royal, modern, rustic' },
        },
        required: ['area', 'color_theme', 'event_type'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'calculate_liquor',
      description: 'Calculate how many bottles of liquor are needed for an event',
      parameters: {
        type: 'object',
        properties: {
          guests_drinking: { type: 'number' },
          event_type: { type: 'string', enum: ['social', 'corporate', 'wedding'] },
          drink_type: { type: 'string', enum: ['spirits', 'beer', 'both'] },
        },
        required: ['guests_drinking', 'event_type', 'drink_type'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'calculate_budget',
      description: 'Estimate event budget breakdown by service category',
      parameters: {
        type: 'object',
        properties: {
          total_budget: { type: 'number', description: 'Total budget in INR' },
          guest_count: { type: 'number' },
          event_type: { type: 'string' },
          services_needed: { type: 'array', items: { type: 'string' } },
        },
        required: ['total_budget', 'guest_count', 'event_type'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'generate_digital_invite',
      description: 'Generate a digital invitation card',
      parameters: {
        type: 'object',
        properties: {
          event_name: { type: 'string' },
          host_names: { type: 'string' },
          date: { type: 'string' },
          venue: { type: 'string' },
          theme_color: { type: 'string' },
        },
        required: ['event_name', 'host_names', 'date', 'venue'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'web_search',
      description: 'Search web for current venue info, artist portfolios, vendor reviews',
      parameters: {
        type: 'object',
        properties: {
          query: { type: 'string' },
        },
        required: ['query'],
      },
    },
  },
];
