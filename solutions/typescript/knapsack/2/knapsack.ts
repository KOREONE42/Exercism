/**
 * Represents an item with a given weight and value.
 */
export type Item = {
  /** Weight of the item (must be non-negative). */
  weight: number
  /** Value of the item (must be non-negative). */
  value: number
}

/**
 * Computes the maximum total value of items that can be carried
 * in a knapsack with a given weight capacity using the 0/1 knapsack DP algorithm.
 *
 * @param params.maximumWeight - Maximum weight capacity of the knapsack (non-negative integer).
 * @param params.items - Array of available items, each with a weight and a value.
 * @returns The maximum achievable value without exceeding the weight capacity.
 *
 * @example
 * ```ts
 * const items = [
 *   { weight: 5, value: 10 },
 *   { weight: 4, value: 40 },
 *   { weight: 6, value: 30 },
 *   { weight: 4, value: 50 },
 * ]
 * const max = maximumValue({ maximumWeight: 10, items })
 * // max === 90
 * ```
 */
export function maximumValue({
  maximumWeight,
  items,
}: {
  maximumWeight: number
  items: Item[]
}): number {
  // Edge cases: no capacity or no items
  if (maximumWeight <= 0 || items.length === 0) return 0

  // dp[w] stores the max value achievable with weight limit w
  const dp: number[] = Array(maximumWeight + 1).fill(0)

  // Iterate over each item once
  for (const { weight, value } of items) {
    if (weight > maximumWeight || weight < 0 || value < 0) {
      // Skip items that cannot be added or invalid
      continue
    }
    // Traverse capacities in reverse to avoid reuse of the same item
    for (let w = maximumWeight; w >= weight; w--) {
      dp[w] = Math.max(dp[w], dp[w - weight] + value)
    }
  }

  // The answer for capacity exactly maximumWeight is the best for <= that limit
  return dp[maximumWeight]
}
