// Define an array of colors corresponding to their resistance values
export const COLORS: string[] = [
  'black',   // 0
  'brown',   // 1
  'red',     // 2
  'orange',  // 3
  'yellow',  // 4
  'green',   // 5
  'blue',    // 6
  'violet',  // 7
  'grey',    // 8
  'white'    // 9
];

// Function to return the numerical value of a specified color
export const colorCode = (color: string): number => {
  const index = COLORS.indexOf(color);
  
  // If the color is not found, throw an error
  if (index === -1) {
    throw new Error('Color not found');
  }
  
  return index; // Return the index which corresponds to the numeric value
};