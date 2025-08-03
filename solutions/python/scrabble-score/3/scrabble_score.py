def score(word):
    """
    Calculate the Scrabble score for a given word using standard letter values.

    Scoring Rules:
        A, E, I, O, U, L, N, R, S, T  -> 1 point
        D, G                          -> 2 points
        B, C, M, P                    -> 3 points
        F, H, V, W, Y                 -> 4 points
        K                             -> 5 points
        J, X                          -> 8 points
        Q, Z                          -> 10 points

    Parameters:
        word (str): The word to be scored. Case-insensitive.

    Returns:
        int: The total Scrabble score of the word. Non-letter characters are ignored.
    """
    letter_scores = {
        **dict.fromkeys("AEIOULNRST", 1),
        **dict.fromkeys("DG", 2),
        **dict.fromkeys("BCMP", 3),
        **dict.fromkeys("FHVWY", 4),
        **dict.fromkeys("K", 5),
        **dict.fromkeys("JX", 8),
        **dict.fromkeys("QZ", 10)
    }

    return sum(letter_scores.get(char.upper(), 0) for char in word if char.isalpha())
