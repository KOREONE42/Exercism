def maximum_value(maximum_weight, items):
    """
    Calculates the maximum total value that can be carried in a knapsack
    given a list of items with individual weights and values, using the
    0/1 Knapsack dynamic programming approach.

    Parameters:
        maximum_weight (int): Maximum weight capacity of the knapsack.
        items (List[Dict[str, int]]): A list of items, where each item is a dictionary
                                      with 'weight' and 'value' as keys.

    Returns:
        int: The maximum value that can be carried in the knapsack without exceeding its capacity.
    """
    # Initialize a DP array where dp[w] stores the max value for weight w
    dp = [0] * (maximum_weight + 1)

    # Iterate through all items
    for item in items:
        weight = item["weight"]
        value = item["value"]

        # Traverse dp array in reverse to prevent reusing the same item
        for w in range(maximum_weight, weight - 1, -1):
            # Update dp[w] to the max value of including or excluding the current item
            dp[w] = max(dp[w], dp[w - weight] + value)

    # The maximum value for the full knapsack capacity is stored in dp[maximum_weight]
    return dp[maximum_weight]
