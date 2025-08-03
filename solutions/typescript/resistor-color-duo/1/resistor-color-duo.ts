/**
 * Decodes the first two color bands of a resistor into a numerical value.
 * 
 * Each resistor band color corresponds to a digit from 0 to 9:
 * black: 0, brown: 1, red: 2, orange: 3, yellow: 4,
 * green: 5, blue: 6, violet: 7, grey: 8, white: 9.
 * 
 * The function ignores any colors beyond the first two.
 * 
 * @param colors - An array of color names representing the bands on a resistor.
 * @returns A two-digit number formed by the first two color codes.
 * 
 * @example
 * decodedValue(['brown', 'green']); // returns 15
 * decodedValue(['yellow', 'violet', 'red']); // returns 47
 */
export function decodedValue(colors: string[]): number {
  // Map of color names to their corresponding digit values
  const colorCodes: { [key: string]: number } = {
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

  // Extract the first two colors and map them to their digit values
  const firstTwoDigits: number[] = colors
    .slice(0, 2) // Take only the first two colors
    .map((color: string) => colorCodes[color]); // Convert each color to its digit

  // Join the digits and convert to a number
  return parseInt(firstTwoDigits.join(''));
}
