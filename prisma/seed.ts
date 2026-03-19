import 'dotenv/config';
import { PrismaClient } from '@prisma/client';
import { PrismaPg } from '@prisma/adapter-pg';
import venuesData from './data/venues.json';

const adapter = new PrismaPg({ connectionString: process.env.DATABASE_URL! });
const prisma = new PrismaClient({ adapter });


const artists = [
  {
    name: 'Anchor Anupriya Kapoor',
    description: 'Bilingual emcee specialising in grand Indian weddings and corporate galas. Known for her warmth, humour, and ability to connect with diverse audiences across Hindi and English.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'emcee',
    priceRangeMin: 75000,
    priceRangeMax: 200000,
    googleUrl: 'https://www.google.com/search?q=Anupriya+Kapoor+Anchor+India',
  },
  {
    name: 'Rahul Subramanian',
    description: 'Stand-up comedian turned corporate entertainer. Razor-sharp observational comedy in English and Hindi. A crowd favourite at corporate parties and award nights.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'stand_up_comedian',
    priceRangeMin: 300000,
    priceRangeMax: 800000,
    googleUrl: 'https://www.google.com/search?q=Rahul+Subramanian+comedian',
  },
  {
    name: 'DJ Aqeel',
    description: 'Bollywood\'s legendary DJ with 20+ years of experience. Known for high-energy sets blending Bollywood hits, retro classics, and remixes. A staple at India\'s biggest parties.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'dj',
    priceRangeMin: 500000,
    priceRangeMax: 1500000,
    googleUrl: 'https://www.google.com/search?q=DJ+Aqeel+Bollywood',
  },
  {
    name: 'DJ NYK',
    description: 'One of India\'s top EDM and commercial DJs. Resident at major nightclubs and festivals. Crafts bespoke sets combining EDM, Bollywood, and international chart toppers.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'dj',
    priceRangeMin: 200000,
    priceRangeMax: 600000,
    googleUrl: 'https://www.google.com/search?q=DJ+NYK+India',
  },
  {
    name: 'Shankar Mahadevan Live Band',
    description: 'Grammy-winning composer Shankar Mahadevan with his live band. An unforgettable evening of Bollywood, sufi, and classical fusion. Premium entertainment for elite events.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'live_band',
    priceRangeMin: 5000000,
    priceRangeMax: 15000000,
    googleUrl: 'https://www.google.com/search?q=Shankar+Mahadevan+live+concert',
  },
  {
    name: 'Kailash Kher',
    description: 'Sufi-rock singer known for soulful anthems like Teri Deewani and Allah Ke Bande. His electrifying live performances bring profound emotion and energy to weddings and events.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'bollywood_celebrity',
    priceRangeMin: 3000000,
    priceRangeMax: 8000000,
    googleUrl: 'https://www.google.com/search?q=Kailash+Kher+live+performance',
  },
  {
    name: 'Neha Kakkar Live',
    description: 'India\'s most-streamed female singer with chart-toppers across a decade. Her high-energy live shows are a guaranteed hit at weddings, sangeets, and corporate parties.',
    city: 'Delhi',
    state: 'Delhi',
    artistType: 'bollywood_celebrity',
    priceRangeMin: 8000000,
    priceRangeMax: 25000000,
    googleUrl: 'https://www.google.com/search?q=Neha+Kakkar+live+concert',
  },
  {
    name: 'Strings of Shrutti — Classical Violin Ensemble',
    description: 'A duo of trained violinists performing Bollywood melodies, Western classical, and Hindi film compositions. Elegant ambient entertainment for cocktail hours and gala dinners.',
    city: 'Bengaluru',
    state: 'Karnataka',
    artistType: 'violinist',
    priceRangeMin: 80000,
    priceRangeMax: 200000,
    googleUrl: 'https://www.google.com/search?q=violin+ensemble+event+Bengaluru',
  },
  {
    name: 'Devang Patel — Saxophone & Jazz',
    description: 'Classically trained saxophonist with 15+ years of live performance experience. Jazz standards, Bollywood on sax, and custom compositions for sophisticated evening events.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'saxophonist',
    priceRangeMin: 60000,
    priceRangeMax: 150000,
    googleUrl: 'https://www.google.com/search?q=saxophone+player+events+Mumbai',
  },
  {
    name: 'Kalbeliya Folk Dance Troupe Jaipur',
    description: 'Authentic Rajasthani Kalbeliya serpent dancers from Jaipur. UNESCO-recognised folk art performed in traditional costume. Adds regal Rajputana flavour to any event.',
    city: 'Jaipur',
    state: 'Rajasthan',
    artistType: 'folk_dancer',
    priceRangeMin: 50000,
    priceRangeMax: 150000,
    googleUrl: 'https://www.google.com/search?q=Kalbeliya+dance+troupe+Jaipur',
  },
  {
    name: 'Bhangra Blaze — Punjabi Dance Troupe',
    description: 'High-octane Bhangra and Giddha group from Chandigarh. Trained in traditional Punjabi folk and fusion styles. Guaranteed to electrify sangeets and baraat processions.',
    city: 'Chandigarh',
    state: 'Punjab',
    artistType: 'folk_dancer',
    priceRangeMin: 80000,
    priceRangeMax: 200000,
    googleUrl: 'https://www.google.com/search?q=Bhangra+troupe+Chandigarh+events',
  },
  {
    name: 'Groovecraft — Bollywood Dance Troupe',
    description: 'Mumbai-based Bollywood and contemporary dance group performing to the latest hits. Slick choreography, dazzling costumes, and audience interaction for weddings and gala nights.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'bollywood_dancer',
    priceRangeMin: 100000,
    priceRangeMax: 300000,
    googleUrl: 'https://www.google.com/search?q=Bollywood+dance+troupe+Mumbai+events',
  },
  {
    name: 'Samba Seduction — International Dance Show',
    description: 'Trained Brazilian Samba and Belly dance performers. Vibrant international act ideal for fusion weddings, destination events, and cocktail soirées seeking a global flair.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'international_dancer',
    priceRangeMin: 150000,
    priceRangeMax: 400000,
    googleUrl: 'https://www.google.com/search?q=international+dance+show+events+India',
  },
  {
    name: 'Suresh Mudra — Live Sand Art',
    description: 'Acclaimed sand artist creating real-time animated stories on an illuminated table. Mesmerising storytelling medium for opening ceremonies, corporate milestones, and themed events.',
    city: 'Hyderabad',
    state: 'Telangana',
    artistType: 'sand_artist',
    priceRangeMin: 75000,
    priceRangeMax: 200000,
    googleUrl: 'https://www.google.com/search?q=sand+art+live+performance+India+events',
  },
  {
    name: 'Arpit Bala — Stand-up Comedy',
    description: 'Hindi stand-up comedian known for relatable content about family and relationships. Perfect for sangeet nights and corporate parties wanting clean, crowd-friendly humour.',
    city: 'Delhi',
    state: 'Delhi',
    artistType: 'stand_up_comedian',
    priceRangeMin: 150000,
    priceRangeMax: 400000,
    googleUrl: 'https://www.google.com/search?q=Arpit+Bala+comedian',
  },
  {
    name: 'The Dhol Foundation India',
    description: 'Energetic dhol players and Punjabi boliyan performers specialising in baraat entries and sangeet entertainment. Creates an unforgettable atmosphere with traditional percussion.',
    city: 'Amritsar',
    state: 'Punjab',
    artistType: 'dhol_artist',
    priceRangeMin: 40000,
    priceRangeMax: 120000,
    googleUrl: 'https://www.google.com/search?q=dhol+players+wedding+India',
  },
  {
    name: 'Samarth — Mentalist & Illusionist',
    description: 'India\'s leading corporate mentalist with mind-bending illusions and psychological demonstrations. A stunning after-dinner act that leaves audiences speechless at luxury events.',
    city: 'Mumbai',
    state: 'Maharashtra',
    artistType: 'illusionist',
    priceRangeMin: 200000,
    priceRangeMax: 600000,
    googleUrl: 'https://www.google.com/search?q=mentalist+illusionist+corporate+events+India',
  },
  {
    name: 'Drum Circle India — Percussion Experience',
    description: 'Interactive percussion workshops and drum circle experiences facilitated by professional percussionists. A unique team-building and celebration activity for 50–500 participants.',
    city: 'Bengaluru',
    state: 'Karnataka',
    artistType: 'percussion_artist',
    priceRangeMin: 100000,
    priceRangeMax: 300000,
    googleUrl: 'https://www.google.com/search?q=drum+circle+team+building+India+events',
  },
];

const vendors = [
  {
    name: 'Shaadi Décor by Isha',
    description: 'Award-winning decorator specialising in luxury floral and fabric installations for Indian weddings. Known for elaborate mandap designs and enchanting entrance decorations.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'decorator',
    priceRangeMin: 500000,
    priceRangeMax: 3000000,
    googleUrl: 'https://www.google.com/search?q=luxury+wedding+decorator+Mumbai',
  },
  {
    name: 'Decorwale Events',
    description: 'Delhi NCR\'s most sought-after event decorator. From intimate mehendi setups to 1,000-pax grand receptions. Specialises in floral carpets, LED art, and custom installations.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'decorator',
    priceRangeMin: 400000,
    priceRangeMax: 2500000,
    googleUrl: 'https://www.google.com/search?q=Decorwale+Events+Delhi',
  },
  {
    name: 'StageSet Fabricators Mumbai',
    description: 'Premium fabricator specialising in large-scale stage design, truss structures, LED walls, and fibre installations. Trusted by India\'s top event companies for production-grade builds.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'fabricator',
    priceRangeMin: 800000,
    priceRangeMax: 5000000,
    googleUrl: 'https://www.google.com/search?q=stage+fabricator+event+production+Mumbai',
  },
  {
    name: 'Wizcraft International',
    description: 'India\'s premier full-service event production and entertainment company. Handles complete event production including AV, staging, artist management, and creative concepts for premium events.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'av_production',
    priceRangeMin: 2000000,
    priceRangeMax: 20000000,
    googleUrl: 'https://www.google.com/search?q=Wizcraft+International+events',
  },
  {
    name: 'Encompass Events',
    description: 'Award-winning event management agency handling India\'s largest corporate events, product launches, and luxury weddings. Full-service planning from concept to execution.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'wedding_planner',
    priceRangeMin: 1500000,
    priceRangeMax: 15000000,
    googleUrl: 'https://www.google.com/search?q=Encompass+Events+Delhi',
  },
  {
    name: 'WeddingNama Planning',
    description: 'Boutique luxury wedding planning studio in Delhi. Handles destination weddings across Rajasthan, Goa, and Dubai. Known for curated experiences and meticulous attention to detail.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'wedding_planner',
    priceRangeMin: 1000000,
    priceRangeMax: 8000000,
    googleUrl: 'https://www.google.com/search?q=WeddingNama+wedding+planning+Delhi',
  },
  {
    name: 'Joseph Radhik Photography',
    description: 'India\'s most celebrated wedding photographer. Featured in Vogue, Harper\'s Bazaar. Captures weddings with a cinematic editorial eye. Books up 18 months in advance.',
    city: 'Chennai',
    state: 'Tamil Nadu',
    vendorType: 'photographer',
    priceRangeMin: 800000,
    priceRangeMax: 3000000,
    googleUrl: 'https://www.google.com/search?q=Joseph+Radhik+wedding+photographer',
  },
  {
    name: 'The Wedding Filmer',
    description: 'India\'s leading wedding cinematography studio. Their films have 100M+ YouTube views. Creates extraordinary wedding films that feel like a Bollywood production.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'photographer',
    priceRangeMin: 600000,
    priceRangeMax: 2500000,
    googleUrl: 'https://www.google.com/search?q=The+Wedding+Filmer+India',
  },
  {
    name: 'SFX India — Cold Pyro & Entry Effects',
    description: 'Specialists in cold pyrotechnics, confetti cannons, CO2 jets, and bride/groom entry effects. Serves luxury weddings across India with trained technicians and safety protocols.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'sfx_provider',
    priceRangeMin: 100000,
    priceRangeMax: 800000,
    googleUrl: 'https://www.google.com/search?q=SFX+cold+pyro+wedding+effects+India',
  },
  {
    name: 'Molecular Bar India',
    description: 'India\'s pioneering molecular mixology bar service. Liquid nitrogen cocktails, smoking drinks, and edible garnishes. A sensational F&B experience for luxury event guests.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'molecular_bar',
    priceRangeMin: 200000,
    priceRangeMax: 800000,
    googleUrl: 'https://www.google.com/search?q=molecular+bar+cocktails+events+India',
  },
  {
    name: 'Rathi Furniture Rentals',
    description: 'Delhi\'s largest event furniture rental company. Extensive inventory of luxury banquet chairs, Chivari chairs, vintage sofas, and custom high-tables for all event types.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'furniture_rental',
    priceRangeMin: 100000,
    priceRangeMax: 600000,
    googleUrl: 'https://www.google.com/search?q=event+furniture+rental+Delhi',
  },
  {
    name: 'Greentech Genset & Lighting',
    description: 'Reliable generator and lighting equipment supplier for events. Silent DG sets, distribution boards, and full power backup solutions for uninterrupted event operations.',
    city: 'Gurugram',
    state: 'Haryana',
    vendorType: 'genset_lighting',
    priceRangeMin: 80000,
    priceRangeMax: 400000,
    googleUrl: 'https://www.google.com/search?q=generator+rental+events+Gurgaon',
  },
  {
    name: 'MapleMaps Travel — Event Logistics',
    description: 'Full-service travel and logistics partner for destination weddings and corporate offsites. Handles group air bookings, hotel blocks, ground transport, and guest travel management.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'travel_agent',
    priceRangeMin: 200000,
    priceRangeMax: 2000000,
    googleUrl: 'https://www.google.com/search?q=destination+wedding+travel+agent+India',
  },
  {
    name: 'Royal Valet & Security Services',
    description: 'Professional valet parking and event security for luxury events. Trained personnel in formal attire, real-time car tracking, and discreet security protocols for high-profile guests.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'valet_security',
    priceRangeMin: 80000,
    priceRangeMax: 300000,
    googleUrl: 'https://www.google.com/search?q=valet+parking+event+security+Delhi',
  },
  {
    name: 'Pixelmapp — Projection Mapping India',
    description: 'Pioneers in architectural projection mapping in India. Creates breathtaking visual narratives on building facades, stages, and props for a truly immersive event experience.',
    city: 'Hyderabad',
    state: 'Telangana',
    vendorType: 'projection_mapping',
    priceRangeMin: 500000,
    priceRangeMax: 3000000,
    googleUrl: 'https://www.google.com/search?q=projection+mapping+events+India',
  },
  {
    name: 'LuxePacks — Gifting & Packaging',
    description: 'Curated luxury gifting solutions for corporate events and weddings. Custom hampers, branded packaging, and experiential gift boxes sourced from premium artisans across India.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'luxury_gifting',
    priceRangeMin: 200000,
    priceRangeMax: 1500000,
    googleUrl: 'https://www.google.com/search?q=luxury+corporate+gifting+events+India',
  },
  {
    name: 'GuestPro — Hospitality & RSVP Management',
    description: 'End-to-end guest management for luxury events. Physical RSVP teams, guest tracking systems, welcome desks, and shadow service for the bridal couple.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'hospitality',
    priceRangeMin: 150000,
    priceRangeMax: 800000,
    googleUrl: 'https://www.google.com/search?q=event+guest+management+hospitality+India',
  },
  {
    name: 'AutoLux — Luxury Car Rentals',
    description: 'Premium fleet of Mercedes, BMW, Range Rover, and vintage cars for bridal entries and VIP transfers. Professionally uniformed chauffeurs across all major Indian cities.',
    city: 'Mumbai',
    state: 'Maharashtra',
    vendorType: 'rental_car',
    priceRangeMin: 50000,
    priceRangeMax: 400000,
    googleUrl: 'https://www.google.com/search?q=luxury+car+rental+wedding+India',
  },
  {
    name: 'Presto AV — Audio Visual Production',
    description: 'Pan-India AV production house. LED walls, line array sound systems, intelligent lighting, and live streaming. Trusted for large-scale corporate conferences and award ceremonies.',
    city: 'New Delhi',
    state: 'Delhi',
    vendorType: 'av_production',
    priceRangeMin: 300000,
    priceRangeMax: 3000000,
    googleUrl: 'https://www.google.com/search?q=AV+production+house+event+Delhi',
  },
  {
    name: 'Ashiyana Tent & Décor',
    description: 'Established tent and décor contractor across Rajasthan. Provides traditional shamianas, contemporary tensile structures, and full furniture packages for outdoor wedding venues.',
    city: 'Jaipur',
    state: 'Rajasthan',
    vendorType: 'decorator',
    priceRangeMin: 300000,
    priceRangeMax: 1500000,
    googleUrl: 'https://www.google.com/search?q=tent+decor+contractor+Jaipur+wedding',
  },
];

async function main() {
  console.log('🌱 Seeding database...');

  // Clear existing data
  await prisma.vendor.deleteMany();
  await prisma.artist.deleteMany();
  await prisma.venue.deleteMany();

  // Seed venues
  console.log(`  → Seeding ${venuesData.length} venues...`);
  await prisma.venue.createMany({ data: venuesData, skipDuplicates: true });

  // Seed artists
  console.log(`  → Seeding ${artists.length} artists...`);
  await prisma.artist.createMany({ data: artists });

  // Seed vendors
  console.log(`  → Seeding ${vendors.length} vendors...`);
  await prisma.vendor.createMany({ data: vendors });

  console.log('✅ Seed complete!');
  console.log(`   Venues: ${venuesData.length}`);
  console.log(`   Artists: ${artists.length}`);
  console.log(`   Vendors: ${vendors.length}`);
}

main()
  .catch((e) => {
    console.error('❌ Seed failed:', e);
    process.exit(1);
  })
  .finally(async () => {
    await prisma.$disconnect();
  });
