def distance(strand_a, strand_b):
    """
    Calculate the Hamming distance between two DNA strands.

    The Hamming distance is the number of positions at which the corresponding
    symbols in two strings of equal length are different. This function will
    raise a ValueError if the two strands are not of equal length.

    Parameters:
    strand_a (str): The first DNA strand.
    strand_b (str): The second DNA strand.

    Returns:
    int: The Hamming distance between the two strands.

    Raises:
    ValueError: If the strands are not of equal length.
    """
    
    # Check if the strands are of equal length
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    
    # Initialize a counter for the Hamming distance
    hamming_distance = 0

    # Iterate through both strands and compare corresponding characters
    for a, b in zip(strand_a, strand_b):
        # Increment the counter if characters at the same position are different
        if a != b:
            hamming_distance += 1
    
    # Return the calculated Hamming distance
    return hamming_distance
