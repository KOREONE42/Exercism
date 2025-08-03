def rows(letter):
    """
    Generate a diamond-shaped pattern of uppercase letters centered around the given letter.

    Args:
        letter (str): A single uppercase letter between 'A' and 'Z'.

    Returns:
        List[str]: A list of strings, each representing a row in the diamond.

    Raises:
        ValueError: If the input is not a single uppercase letter from A to Z.
    """
    if not ('A' <= letter <= 'Z'):
        raise ValueError("Input must be a capital letter from A to Z.")

    index = ord(letter) - ord('A')  # Get the 0-based index of the input letter
    size = 2 * index + 1            # Total number of rows (and columns)
    diamond = []

    # Construct the top half including the middle row
    for i in range(index + 1):
        current_letter = chr(ord('A') + i)
        outer_spaces = ' ' * (index - i)  # Leading and trailing spaces

        if i == 0:
            # First row has only 'A' with spaces on each side
            row = outer_spaces + current_letter + outer_spaces
        else:
            inner_spaces = ' ' * (2 * i - 1)  # Spaces between the two letters
            row = outer_spaces + current_letter + inner_spaces + current_letter + outer_spaces

        diamond.append(row)

    # Construct the bottom half by reversing the top half (excluding the middle row)
    for i in range(index - 1, -1, -1):
        diamond.append(diamond[i])

    return diamond
