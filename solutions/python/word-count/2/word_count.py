import re
from collections import Counter

def count_words(sentence):
    """
    Analyze a subtitle sentence and count how many times each word appears.

    Rules:
    - Words consist of letters, digits, and optional apostrophes used in contractions.
    - Words are case-insensitive (e.g., "You" and "you" are considered the same).
    - All punctuation and whitespace are treated as separators, 
      except apostrophes within words (e.g., "don't", "it's").
    - Numbers (e.g., "123") are treated as words.

    Parameters:
        sentence (str): A subtitle line containing ASCII characters.

    Returns:
        dict: A dictionary where keys are words and values are their frequency counts.
    """
    # Normalize to lowercase to make word matching case-insensitive
    sentence = sentence.lower()

    # Regex breakdown:
    # [a-zA-Z0-9]+        → Matches a sequence of letters or digits (the base word)
    # (?:'[a-zA-Z0-9]+)?  → Optionally allows a contraction (e.g., 's, 're)
    # Combined, this matches words like "hello", "you're", and "123"
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?", sentence)

    # Count how often each word appears
    word_counts = Counter(words)

    # Return result as a regular dictionary
    return dict(word_counts)
