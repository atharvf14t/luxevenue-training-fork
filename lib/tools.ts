import { prisma } from './prisma';
import { calculateLiquor } from './liquor-calc';

export interface ToolResult {
  content: string;
}

// Format venue results as markdown numbered list
function formatVenues(venues: {
  name: string;
  city: string;
  state: string;
  rooms: number;
  pricePerDay: number;
  venueStyle: string;
  googleUrl: string;
  capacity: number;
  description: string;
}[]): string {
  if (venues.length === 0) return 'No venues found matching your criteria. Try broadening your search.';
  return venues
    .map(
      (v, i) =>
        `${i + 1}. **${v.name}**, ${v.city} — Capacity: ${v.capacity} pax, ${v.rooms} rooms, Est. ₹${(v.pricePerDay / 100000).toFixed(1)}L/day | Style: ${v.venueStyle}\n   ${v.description}\n   [View Venue →](${v.googleUrl})`
    )
    .join('\n\n');
}

function formatArtists(artists: {
  name: string;
  city: string;
  state: string;
  artistType: string;
  priceRangeMin: number;
  priceRangeMax: number;
  googleUrl: string;
  description: string;
}[]): string {
  if (artists.length === 0) return 'No artists found matching your criteria.';
  return artists
    .map(
      (a, i) =>
        `${i + 1}. **${a.name}** (${a.artistType.replace(/_/g, ' ')}) — ${a.city}, ${a.state} | Budget: ₹${(a.priceRangeMin / 100000).toFixed(1)}L – ₹${(a.priceRangeMax / 100000).toFixed(1)}L\n   ${a.description}\n   [View Profile →](${a.googleUrl})`
    )
    .join('\n\n');
}

function formatVendors(vendors: {
  name: string;
  city: string;
  state: string;
  vendorType: string;
  priceRangeMin: number;
  priceRangeMax: number;
  googleUrl: string;
  description: string;
}[]): string {
  if (vendors.length === 0) return 'No vendors found matching your criteria.';
  return vendors
    .map(
      (v, i) =>
        `${i + 1}. **${v.name}** (${v.vendorType.replace(/_/g, ' ')}) — ${v.city}, ${v.state} | Budget: ₹${(v.priceRangeMin / 100000).toFixed(1)}L – ₹${(v.priceRangeMax / 100000).toFixed(1)}L\n   ${v.description}\n   [View Profile →](${v.googleUrl})`
    )
    .join('\n\n');
}

export async function handleToolCall(
  toolName: string,
  args: Record<string, unknown>
): Promise<string> {
  switch (toolName) {
    case 'search_venues': {
      const { city, event_type, capacity, venue_type, budget_range } = args as {
        city: string;
        event_type: string;
        capacity?: number;
        venue_type?: string;
        budget_range?: string;
      };

      const where: Record<string, unknown> = {};
      if (city) where.city = { contains: city, mode: 'insensitive' };
      if (venue_type && venue_type !== 'any') where.venueStyle = venue_type;
      if (capacity) where.capacity = { gte: capacity };

      const venues = await prisma.venue.findMany({
        where,
        take: 5,
        orderBy: { pricePerDay: 'asc' },
      });

      return formatVenues(venues);
    }

    case 'search_artists': {
      const { category, budget_min, budget_max, gender } = args as {
        category: string;
        budget_min?: number;
        budget_max?: number;
        gender?: string;
      };

      const where: Record<string, unknown> = {};
      if (category) where.artistType = { contains: category.replace(/ /g, '_'), mode: 'insensitive' };
      if (budget_min) where.priceRangeMin = { gte: budget_min };
      if (budget_max) where.priceRangeMax = { lte: budget_max };

      const artists = await prisma.artist.findMany({
        where,
        take: 5,
        orderBy: { priceRangeMin: 'asc' },
      });

      return formatArtists(artists);
    }

    case 'search_vendors': {
      const { service_type, city } = args as {
        service_type: string;
        city?: string;
      };

      const where: Record<string, unknown> = {};
      if (service_type) where.vendorType = { contains: service_type.replace(/ /g, '_'), mode: 'insensitive' };
      if (city) where.city = { contains: city, mode: 'insensitive' };

      const vendors = await prisma.vendor.findMany({
        where,
        take: 5,
        orderBy: { priceRangeMin: 'asc' },
      });

      return formatVendors(vendors);
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
      const { total_budget, guest_count, event_type, services_needed } = args as {
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

      // Return a marker that the frontend will intercept
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

// Tool definitions for Azure OpenAI function calling
export const TOOL_DEFINITIONS = [
  {
    type: 'function' as const,
    function: {
      name: 'search_venues',
      description: 'Search for event venues in our database. Returns up to 5 results.',
      parameters: {
        type: 'object',
        properties: {
          city: { type: 'string', description: 'City to search in' },
          capacity: { type: 'number', description: 'Minimum guest capacity needed' },
          venue_type: {
            type: 'string',
            enum: ['5-star', 'heritage', 'resort', 'outdoor', 'banquet', 'any'],
          },
          budget_range: { type: 'string', description: 'Budget range e.g. "5-10L"' },
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
      name: 'search_artists',
      description: 'Search for artists/entertainment by category and budget',
      parameters: {
        type: 'object',
        properties: {
          category: { type: 'string', description: 'Artist category e.g. dj, emcee, live band' },
          budget_min: { type: 'number', description: 'Minimum budget in INR' },
          budget_max: { type: 'number', description: 'Maximum budget in INR' },
          gender: { type: 'string', enum: ['male', 'female', 'any'] },
        },
        required: ['category'],
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'search_vendors',
      description: 'Search for vendors by service type and city',
      parameters: {
        type: 'object',
        properties: {
          service_type: { type: 'string', description: 'Type of service e.g. decorator, photographer' },
          city: { type: 'string' },
        },
        required: ['service_type'],
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
