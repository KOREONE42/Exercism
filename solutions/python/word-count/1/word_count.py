import re
from collections import Counter

def count_words(sentence):
    """
    Counts the frequency of each word in a given subtitle sentence.

    A word is defined as a sequence of letters, numbers, or contractions
    (e.g., "don't", "you're"). Words are case-insensitive and are separated
    by any punctuation or whitespace, except for apostrophes used in contractions.

    Parameters:
        sentence (str): The subtitle text to analyze.

    Returns:
        dict: A dictionary mapping each word to the number of times it appears.
    """
    # Convert the sentence to lowercase to ensure case-insensitive matching
    sentence = sentence.lower()

    # Use regex to find words:
    # - [a-zA-Z0-9]+ matches letters or numbers
    # - (?:'[a-zA-Z0-9]+)? allows for optional contractions like don't, it's
    # - This ignores all other punctuation and whitespace (e.g., commas, underscores)
    words = re.findall(r"[a-zA-Z0-9]+(?:'[a-zA-Z0-9]+)?", sentence)

    # Count the occurrences of each word
    return dict(Counter(words))
