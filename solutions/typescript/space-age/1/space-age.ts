const EARTH_YEAR_SECONDS = 31557600;

const ORBITAL_PERIODS: Record<string, number> = {
  mercury: 0.2408467,
  venus:   0.61519726,
  earth:   1.0,
  mars:    1.8808158,
  jupiter: 11.862615,
  saturn:  29.447498,
  uranus:  84.016846,
  neptune: 164.79132
};

export function age(planet: unknown, seconds: unknown): unknown {
  if (typeof planet !== 'string' || typeof seconds !== 'number') {
    throw new Error('Invalid input: expected a planet name and number of seconds');
  }

  const key = planet.toLowerCase();
  const period = ORBITAL_PERIODS[key];
  if (period === undefined) {
    throw new Error(`Unknown planet: ${planet}`);
  }

  const years = seconds / (EARTH_YEAR_SECONDS * period);
  return Number(years.toFixed(2));
}
