def recite(start_verse, end_verse):
    """
    Recite verses from the cumulative song 'I Know an Old Lady Who Swallowed a Fly'.

    The song adds a new animal in each verse and builds upon the previous ones, forming a chain.
    The final verse (with the horse) ends the song abruptly without the typical repetition.

    Parameters:
        start_verse (int): The 1-based index of the first verse to return.
        end_verse (int): The 1-based index of the last verse to return.

    Returns:
        list[str]: A list of song lines from the specified range of verses, 
                   including blank lines between verses but not after the last verse.
    """
    # Ordered list of animals swallowed in each verse
    animals = [
        "fly", "spider", "bird", "cat",
        "dog", "goat", "cow", "horse"
    ]

    # Optional comment for each animal's verse
    comments = {
        "fly": "",
        "spider": "It wriggled and jiggled and tickled inside her.",
        "bird": "How absurd to swallow a bird!",
        "cat": "Imagine that, to swallow a cat!",
        "dog": "What a hog, to swallow a dog!",
        "goat": "Just opened her throat and swallowed a goat!",
        "cow": "I don't know how she swallowed a cow!",
        "horse": "She's dead, of course!"
    }

    # Reasoning chains that explain why she swallowed each animal
    chain = {
        "spider": "She swallowed the spider to catch the fly.",
        "bird": "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "cat": "She swallowed the cat to catch the bird.",
        "dog": "She swallowed the dog to catch the cat.",
        "goat": "She swallowed the goat to catch the dog.",
        "cow": "She swallowed the cow to catch the goat.",
    }

    output = []

    for i in range(start_verse - 1, end_verse):
        current_animal = animals[i]
        verse_lines = [f"I know an old lady who swallowed a {current_animal}."]

        # Add the special comment for the animal, if it exists
        comment = comments[current_animal]
        if comment:
            verse_lines.append(comment)

        # Special case: horse ends the song immediately
        if current_animal == "horse":
            output.extend(verse_lines)
            continue

        # Add cumulative swallowing chain in reverse order
        for j in range(i, -1, -1):
            animal = animals[j]
            if animal in chain:
                verse_lines.append(chain[animal])
            if animal == "fly":
                verse_lines.append("I don't know why she swallowed the fly. Perhaps she'll die.")
                break

        # Append verse to final output
        output.extend(verse_lines)

        # Add a blank line between verses, but not after the last one
        if i < end_verse - 1:
            output.append("")

    return output
