def transform(legacy_data):
    """
    Transforms a legacy letter score format into a new format.

    Legacy format:
        A dictionary where keys are point values (ints) and values are 
        lists of uppercase letters that share that score.
    
    New format:
        A dictionary where each lowercase letter is a key and the 
        corresponding score is the value (one-to-one mapping).

    Example:
        Input:
            {
                1: ["A", "E"],
                2: ["D", "G"]
            }
        Output:
            {
                "a": 1,
                "e": 1,
                "d": 2,
                "g": 2
            }

    Args:
        legacy_data (dict): Legacy mapping of points to uppercase letters.

    Returns:
        dict: New mapping of lowercase letters to their point values.
    """
    new_data = {}  # Initialize the new dictionary

    # Loop over each point value and its associated letters
    for score, letters in legacy_data.items():
        for letter in letters:
            # Convert each letter to lowercase and assign its score
            new_data[letter.lower()] = score

    return new_data
