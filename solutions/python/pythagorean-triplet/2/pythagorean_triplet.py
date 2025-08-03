import math

def triplets_with_sum(number):
    """
    Find all Pythagorean triplets (a, b, c) such that:
      - a < b < c (natural numbers)
      - a^2 + b^2 = c^2
      - a + b + c = number

    Uses Euclid's formula for generating Pythagorean triplets:
        a = k * (m^2 - n^2)
        b = k * (2 * m * n)
        c = k * (m^2 + n^2)
        sum = k * 2 * m * (m + n)

    Args:
        number (int): The desired sum of the triplet.

    Returns:
        list of lists: All valid triplets [a, b, c] that satisfy the conditions.
    """
    triplets = set()

    # Upper limit for m based on the constraint that sum = 2 * k * m * (m + n)
    max_m = int(math.sqrt(number // 2)) + 1

    for m in range(2, max_m):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
                # Euclid's formula gives a primitive triplet
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                triplet_sum = a + b + c

                # Scale the primitive triplet if it fits into 'number'
                if number % triplet_sum == 0:
                    k = number // triplet_sum
                    scaled_triplet = tuple(sorted([k * a, k * b, k * c]))
                    triplets.add(scaled_triplet)

    # Convert set of tuples to list of lists
    return [list(t) for t in triplets]
