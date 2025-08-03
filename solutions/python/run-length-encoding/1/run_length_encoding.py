import re

def encode(string):
    """
    Perform run-length encoding on the input string.

    Consecutive identical characters are replaced with the count followed by the character.
    Single characters are not prefixed by a count.

    Parameters:
    string (str): The input string to encode.

    Returns:
    str: The run-length encoded string.
    """
    if not string:
        return ""

    encoded = []
    i = 0

    while i < len(string):
        count = 1  # Start count at 1 for the current character

        # Count how many times the current character repeats consecutively
        while i + 1 < len(string) and string[i] == string[i + 1]:
            count += 1
            i += 1

        # Append the count (if more than 1) and the character to the result
        if count == 1:
            encoded.append(string[i])
        else:
            encoded.append(f"{count}{string[i]}")

        i += 1  # Move to the next character

    return ''.join(encoded)


def decode(string):
    """
    Decode a run-length encoded string back to its original form.

    Interprets sequences of numbers followed by characters as repetitions of the character.

    Parameters:
    string (str): The run-length encoded string to decode.

    Returns:
    str: The decoded original string.
    """
    decoded = []

    # Use regular expression to find all occurrences of optional digits followed by a character
    for count, char in re.findall(r'(\d*)([A-Za-z\s])', string):
        # Convert count to integer (default to 1 if empty) and repeat the character
        decoded.append(char * (int(count) if count else 1))

    return ''.join(decoded)
