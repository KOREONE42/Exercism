def primes(limit):
    """
    Returns a list of all prime numbers less than or equal to the given limit
    using the Sieve of Eratosthenes algorithm.

    The Sieve of Eratosthenes works by iteratively marking the multiples of each
    prime number starting from 2. All unmarked numbers that remain are primes.

    Parameters:
        limit (int): The upper bound of the range to search for primes (inclusive).

    Returns:
        List[int]: A list of prime numbers less than or equal to `limit`.
    """
    # Edge case: no primes exist below 2
    if limit < 2:
        return []

    # Initialize a list where the index represents the number, and the value
    # represents whether it's currently assumed to be a prime (True = prime)
    is_prime = [True] * (limit + 1)
    is_prime[0] = False  # 0 is not prime
    is_prime[1] = False  # 1 is not prime

    # Start checking from 2 up to the square root of the limit
    for current in range(2, int(limit ** 0.5) + 1):
        if is_prime[current]:
            # Mark all multiples of `current` as not prime, starting from current^2
            for multiple in range(current * current, limit + 1, current):
                is_prime[multiple] = False

    # Collect and return all numbers still marked as prime
    primes_list = [number for number, prime in enumerate(is_prime) if prime]
    return primes_list
