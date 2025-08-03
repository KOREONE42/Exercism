/**
 * List of supported planets in lowercase form.
 */
export type Planet =
  | 'mercury'
  | 'venus'
  | 'earth'
  | 'mars'
  | 'jupiter'
  | 'saturn'
  | 'uranus'
  | 'neptune';

/**
 * Number of seconds in one Earth year (365.25 days).
 */
export const EARTH_YEAR_SECONDS = 31557600;

/**
 * Orbital periods relative to an Earth year for each planet.
 */
export const ORBITAL_PERIODS: Record<Planet, number> = {
  mercury: 0.2408467,
  venus:   0.61519726,
  earth:   1.0,
  mars:    1.8808158,
  jupiter: 11.862615,
  saturn:  29.447498,
  uranus:  84.016846,
  neptune: 164.79132
};

/**
 * Calculates age in years on a given planet based on seconds lived.
 * Rounds to two decimal places.
 *
 * @param planet - One of the supported planet names (in lowercase).
 * @param seconds - Age in seconds.
 * @returns Age in planet years, rounded to two decimals.
 * @throws {Error} If an unsupported planet name is provided.
 */
export function age(
  planet: Planet,
  seconds: number
): number {
  const period = ORBITAL_PERIODS[planet];
  if (period === undefined) {
    throw new Error(`Unknown planet: ${planet}`);
  }

  const orbitalSeconds = EARTH_YEAR_SECONDS * period;
  const rawYears = seconds / orbitalSeconds;
  return Math.round(rawYears * 100) / 100;
}
