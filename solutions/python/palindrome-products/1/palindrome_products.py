def largest(min_factor, max_factor):
    """
    Find the largest palindromic product of two factors within the given range.

    :param min_factor: Minimum factor to consider (inclusive).
    :param max_factor: Maximum factor to consider (inclusive).
    :return: Tuple of (largest palindrome, list of factor pairs).
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindrome = None  # To store the largest palindrome found
    result = []        # To store all factor pairs producing that palindrome

    # Loop from larger numbers first to find the largest palindrome earlier
    for a in range(max_factor, min_factor - 1, -1):
        for b in range(a, min_factor - 1, -1):
            product = a * b

            # Optimization: stop checking if product is already smaller than current max
            if palindrome is not None and product < palindrome:
                break

            # Check if the product is a palindrome
            if str(product) == str(product)[::-1]:
                if product > (palindrome or 0):
                    palindrome = product
                    result = [(b, a)]  # Start new result list
                elif product == palindrome:
                    result.append((b, a))  # Add another valid pair

    return palindrome, result


def smallest(min_factor, max_factor):
    """
    Find the smallest palindromic product of two factors within the given range.

    :param min_factor: Minimum factor to consider (inclusive).
    :param max_factor: Maximum factor to consider (inclusive).
    :return: Tuple of (smallest palindrome, list of factor pairs).
    """
    if min_factor > max_factor:
        raise ValueError("min must be <= max")

    palindrome = None  # To store the smallest palindrome found
    result = []        # To store all factor pairs producing that palindrome

    # Loop from smaller numbers first to find the smallest palindrome earlier
    for a in range(min_factor, max_factor + 1):
        for b in range(a, max_factor + 1):
            product = a * b

            # Optimization: stop checking if product is already larger than current min
            if palindrome is not None and product > palindrome:
                break

            # Check if the product is a palindrome
            if str(product) == str(product)[::-1]:
                if palindrome is None or product < palindrome:
                    palindrome = product
                    result = [(a, b)]  # Start new result list
                elif product == palindrome:
                    result.append((a, b))  # Add another valid pair

    return palindrome, result
