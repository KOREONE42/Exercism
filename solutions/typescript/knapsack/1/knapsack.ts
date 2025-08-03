type Item = {
  weight: number
  value: number
}

export function maximumValue({
  maximumWeight,
  items,
}: {
  maximumWeight: number
  items: Item[]
}): number {
  // dp[w] will hold the maximum value achievable with weight limit w
  const dp = new Array<number>(maximumWeight + 1).fill(0)

  // Iterate through each item
  for (const item of items) {
    // Traverse weights from high to low to avoid reusing the same item
    for (let w = maximumWeight; w >= item.weight; w--) {
      const newValue = dp[w - item.weight] + item.value
      if (newValue > dp[w]) {
        dp[w] = newValue
      }
    }
  }

  // The answer is the maximum value for the full capacity
  return dp[maximumWeight]
}
