import math

def triplets_with_sum(number):
    """
    Generate all Pythagorean triplets (a, b, c) such that:
      - a < b < c (natural numbers)
      - a^2 + b^2 = c^2 (Pythagorean condition)
      - a + b + c = number (sum constraint)
    
    This uses Euclid's formula for better performance on large inputs.
    
    Args:
        number (int): Desired total sum of the triplet.
    
    Returns:
        list of lists: All valid triplets [a, b, c] that satisfy the constraints.
    """
    triplets = []
    limit = int(math.sqrt(number // 2)) + 1

    for m in range(2, limit):
        for n in range(1, m):
            if (m - n) % 2 == 1 and math.gcd(m, n) == 1:  # Ensure primitive triplet
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                total = a + b + c

                if number % total == 0:
                    k = number // total
                    triplet = sorted([k * a, k * b, k * c])
                    triplets.append(triplet)

    return triplets
