export interface LiquorCalcInput {
  guestsDrinking: number;
  eventType: 'social' | 'corporate' | 'wedding';
  drinkType: 'spirits' | 'beer' | 'both';
}

export interface LiquorCalcResult {
  spirits?: number;
  beer?: number;
  totalBottles: number;
  summary: string;
}

export function calculateLiquor(input: LiquorCalcInput): LiquorCalcResult {
  const { guestsDrinking, eventType, drinkType } = input;

  let spirits: number | undefined;
  let beer: number | undefined;

  if (drinkType === 'spirits' || drinkType === 'both') {
    const spiritRatio = eventType === 'corporate' ? 4 : 3;
    spirits = Math.ceil(guestsDrinking / spiritRatio);
  }

  if (drinkType === 'beer' || drinkType === 'both') {
    const beerRatio = eventType === 'corporate' ? 2.5 : 3.5;
    beer = Math.ceil(guestsDrinking * beerRatio);
  }

  const totalBottles = (spirits ?? 0) + (beer ?? 0);

  const lines: string[] = [];
  if (spirits !== undefined) lines.push(`**Spirits:** ${spirits} bottles (1 per ${eventType === 'corporate' ? 4 : 3} guests)`);
  if (beer !== undefined) lines.push(`**Beer:** ${beer} bottles/cans (~${eventType === 'corporate' ? '2–3' : '3–4'} per guest)`);
  lines.push(`\n*Through LuxeVenue, you can purchase these at **10% off**. Want me to send you our liquor menu?*`);

  return {
    spirits,
    beer,
    totalBottles,
    summary: lines.join('\n'),
  };
}
