def find_fewest_coins(coins, target):
    """
    Determines the fewest number of coins required to make up the target amount.

    Args:
        coins (list of int): Available coin denominations.
        target (int): The amount of change to make.

    Returns:
        list of int: A list of coin denominations that sum to the target, using the fewest coins.

    Raises:
        ValueError: If the target is negative or if it's impossible to make change with the given coins.
    """
    # Validate input for negative target
    if target < 0:
        raise ValueError("target can't be negative")

    # Initialize the DP table where dp[i] is the minimum coins needed for amount i
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0

    # To reconstruct the solution, keep track of last coin used for each amount
    backtrack = [None] * (target + 1)

    # Fill dp table
    for i in range(1, target + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                backtrack[i] = coin

    # If target is unreachable, raise an error
    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    # Backtrack from target to determine which coins were used
    result = []
    curr = target
    while curr > 0:
        coin = backtrack[curr]
        result.append(coin)
        curr -= coin

    return result

