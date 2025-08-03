def score(word):
    """
    Computes the Scrabble score for a given word.

    The score is calculated by summing the point values assigned to each letter,
    based on the standard English-language Scrabble scoring system.

    Letter values:
        - 1 point: A, E, I, O, U, L, N, R, S, T
        - 2 points: D, G
        - 3 points: B, C, M, P
        - 4 points: F, H, V, W, Y
        - 5 points: K
        - 8 points: J, X
        - 10 points: Q, Z

    Args:
        word (str): The input word to evaluate.

    Returns:
        int: The total score of the word.
    """
    # Map each letter to its score
    letter_scores = {
        **dict.fromkeys("AEIOULNRST", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10)
    }

    # Convert each letter to uppercase, look up its value, and sum the results
    return sum(letter_scores.get(char.upper(), 0) for char in word)
