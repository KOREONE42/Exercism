export function decodedResistorValue(colors: string[]): string {
  const colorMap: Record<string, number> = {
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
  }

  // Only consider the first three colors
  const [first, second, third] = colors
  const firstDigit = colorMap[first]
  const secondDigit = colorMap[second]
  const multiplier = Math.pow(10, colorMap[third])

  const rawValue = (firstDigit * 10 + secondDigit) * multiplier

  // Formatting logic
  if (rawValue >= 1_000_000_000) {
    return `${rawValue / 1_000_000_000} gigaohms`
  } else if (rawValue >= 1_000_000) {
    return `${rawValue / 1_000_000} megaohms`
  } else if (rawValue >= 1_000) {
    return `${rawValue / 1_000} kiloohms`
  } else {
    return `${rawValue} ohms`
  }
}
