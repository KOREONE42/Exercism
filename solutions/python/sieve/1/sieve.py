def primes(limit):
    """
    Use the Sieve of Eratosthenes to find all prime numbers up to and including the given limit.

    A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    This function marks non-prime numbers (multiples of each prime) in a boolean list and returns
    all numbers that remain marked as prime.

    Parameters:
        limit (int): The upper bound of the range to search for prime numbers (inclusive).

    Returns:
        List[int]: A list of all prime numbers less than or equal to the limit.
    """
    # No primes below 2
    if limit < 2:
        return []

    # Initialize a list of boolean values, where index represents the number
    # True means "assumed prime" initially
    is_prime = [True] * (limit + 1)

    # 0 and 1 are not prime numbers
    is_prime[0:2] = [False, False]

    # Iterate from 2 to sqrt(limit), as any composite number has at least one factor ≤ sqrt(limit)
    for number in range(2, int(limit ** 0.5) + 1):
        if is_prime[number]:
            # Mark all multiples of the current number as not prime
            # Start from number^2 because smaller multiples were already marked
            for multiple in range(number * number, limit + 1, number):
                is_prime[multiple] = False

    # Extract and return the list of numbers still marked as prime
    return [i for i, prime in enumerate(is_prime) if prime]
