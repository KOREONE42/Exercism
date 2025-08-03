/**
 * List of valid resistor color names for the first two bands.
 */
type ResistorColor =
  | 'black'
  | 'brown'
  | 'red'
  | 'orange'
  | 'yellow'
  | 'green'
  | 'blue'
  | 'violet'
  | 'grey'
  | 'white';

/**
 * Maps each resistor color to its corresponding digit value.
 */
const colorCodes: Record<ResistorColor, number> = {
  black: 0,
  brown: 1,
  red: 2,
  orange: 3,
  yellow: 4,
  green: 5,
  blue: 6,
  violet: 7,
  grey: 8,
  white: 9,
};

/**
 * Decodes the resistance value based on the first two color bands.
 *
 * @param colors - An array of resistor colors. Only the first two colors are used.
 * @returns The numeric value represented by the first two color bands.
 *
 * @example
 * decodedValue(['blue', 'grey']) // returns 68
 * decodedValue(['red', 'black', 'orange']) // returns 20
 */
export function decodedValue(colors: ResistorColor[]): number {
  // Get the digit values of the first two bands
  const [first, second] = colors;
  const value = colorCodes[first] * 10 + colorCodes[second];

  return value;
}
