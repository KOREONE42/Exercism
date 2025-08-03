def prime(number):
    """
    Returns the nth prime number.

    Parameters:
    number (int): The position of the prime number to find (1-based index).

    Returns:
    int: The nth prime number.

    Raises:
    ValueError: If number is less than 1 (since there is no 0th or negative prime).
    """
    
    if number < 1:
        raise ValueError('there is no zeroth prime')

    def is_prime(n):
        """
        Determines whether a given number is prime.

        Parameters:
        n (int): The number to check.

        Returns:
        bool: True if n is prime, False otherwise.
        """
        if n < 2:
            return False
        # Only test divisors up to the square root of n for efficiency
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    count = 0       # Number of primes found so far
    candidate = 1   # Current number being tested for primality

    # Continue searching until we find the nth prime
    while count < number:
        candidate += 1
        if is_prime(candidate):
            count += 1

    return candidate
