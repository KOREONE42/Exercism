/**
 * Determines whether the given year is a leap year in the Gregorian calendar.
 *
 * Rules:
 * - Every year divisible by 4 is a leap year,
 *   except years divisible by 100 are not leap years,
 *   unless they are also divisible by 400.
 *
 * @param year - The year to check
 * @returns True if leap year, false otherwise
 */
export function isLeap(year: number): boolean {
  // Years divisible by 400 are leap years
  if (year % 400 === 0) {
    return true;
  }
  // Years divisible by 100 (but not 400) are not leap years
  if (year % 100 === 0) {
    return false;
  }
  // Years divisible by 4 (but not 100) are leap years
  if (year % 4 === 0) {
    return true;
  }
  // All other years are not leap years
  return false;
}