def score(word):
    """
    Calculate the Scrabble score of a given word.

    Each letter in Scrabble has a point value. This function adds up the values
    of the letters in the input word based on standard English Scrabble rules.

    Args:
        word (str): The input word to score.

    Returns:
        int: The total Scrabble score of the word.
    """
    # Define point values for groups of letters
    letter_values = {
        1: "AEIOULNRST",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: "K",
        8: "JX",
        10: "QZ"
    }

    # Create a lookup dictionary to map each letter to its value
    lookup = {}
    for value, letters in letter_values.items():
        for letter in letters:
            lookup[letter] = value

    # Sum the score for each letter in the word (case-insensitive)
    return sum(lookup.get(char.upper(), 0) for char in word)
