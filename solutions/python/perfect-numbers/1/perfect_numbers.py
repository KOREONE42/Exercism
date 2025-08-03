def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # Check for a positive integer
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    # Calculate the aliquot sum
    aliquot_sum = sum(factor for factor in range(1, number) if number % factor == 0)
    
    # Determine the classification
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"