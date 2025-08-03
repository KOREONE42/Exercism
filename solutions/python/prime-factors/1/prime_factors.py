def factors(value):
    """
    Compute the prime factors of a given natural number.

    Args:
        value (int): The natural number to factorize.

    Returns:
        List[int]: A list of prime factors, possibly with repetitions.
    """
    result = []           # List to store the prime factors
    divisor = 2           # Start with the smallest prime number

    # Try dividing by each number up to the square root of value
    while divisor * divisor <= value:
        # While the current divisor divides the value evenly
        while value % divisor == 0:
            result.append(divisor)  # Store the divisor
            value //= divisor       # Divide the value
        divisor += 1                # Move to the next possible divisor

    # If there's any value left > 1, it's also a prime factor
    if value > 1:
        result.append(value)

    return result
