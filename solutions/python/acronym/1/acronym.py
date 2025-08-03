import re

def abbreviate(words):
    """
    Convert a phrase into its acronym.

    :param words: str - the input phrase.
    :return: str - acronym formed by the capitalized initials.
    """
    # Replace hyphens with spaces to treat them like word separators
    words = words.replace('-', ' ')

    # Remove all characters except letters, digits, and whitespace
    words = re.sub(r"[^A-Za-z0-9\s]", "", words)

    # Build the acronym by taking the first character of each word and capitalizing it
    acronym = ''.join(word[0].upper() for word in words.split() if word)

    return acronym
