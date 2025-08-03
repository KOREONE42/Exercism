def sum_of_multiples(limit, multiples):
    """
    Calculate the total energy points awarded to a player based on the 
    unique multiples of magical item base values found during a game level.

    Parameters:
    limit (int): The level number the player completed. Only multiples less than this number are considered.
    multiples (list of int): A list of base values of magical items found. These must be unique and sorted.

    Returns:
    int: The sum of all unique multiples of the given base values that are less than the level number.
    
    Example:
    >>> sum_of_multiples(20, [3, 5])
    78
    """
    
    unique_multiples = set()  # Use a set to store unique multiples without duplicates

    for base in multiples:
        if base == 0:
            continue  # Skip zero to avoid division by zero or infinite loops
        
        # Add all multiples of the current base that are less than the limit
        for multiple in range(base, limit, base):
            unique_multiples.add(multiple)
    
    # Return the sum of all unique multiples found
    return sum(unique_multiples)
