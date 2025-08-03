def recite(start, take=1):
    """
    Generate verses of the song 'Ten Green Bottles'.

    Args:
        start (int): The starting number of green bottles (max 10).
        take (int): How many verses to generate.

    Returns:
        List[str]: A list of lines representing the requested verses.
    """
    # Map of numbers to words for 0 through 10
    number_words = {
        0: "no",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }

    verses = []

    # Generate verses in countdown order
    for idx, num in enumerate(range(start, start - take, -1)):
        next_num = num - 1

        # Convert numbers to their corresponding words
        current_word = number_words[num]
        next_word = number_words.get(next_num, str(next_num))

        # Format current and next lines with correct pluralization
        current_bottles = f"{current_word} green bottle{'s' if num != 1 else ''}"
        if next_num == 0:
            next_bottles = "no green bottles"
        else:
            next_bottles = f"{next_word.lower()} green bottle{'s' if next_num != 1 else ''}"

        # Build the verse
        verses.append(f"{current_bottles} hanging on the wall,")
        verses.append(f"{current_bottles} hanging on the wall,")
        verses.append("And if one green bottle should accidentally fall,")
        verses.append(f"There'll be {next_bottles} hanging on the wall.")

        # Add a blank line between verses (but not after the last one)
        if idx < take - 1:
            verses.append("")

    return verses
