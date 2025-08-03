def recite(start_verse, end_verse):
    """
    Generate the lyrics of the cumulative song 'I Know an Old Lady Who Swallowed a Fly'
    from start_verse to end_verse (1-indexed).

    Each verse adds a new animal and repeats the previous ones in reverse order,
    ending with a refrain. The last verse for the horse ends the song abruptly.

    Parameters:
    - start_verse (int): The starting verse number (1-based).
    - end_verse (int): The ending verse number (1-based).

    Returns:
    - list[str]: A list of strings representing the song lyrics, including blank lines between verses.
    """
    
    # List of animals swallowed in order
    animals = [
        "fly",
        "spider",
        "bird",
        "cat",
        "dog",
        "goat",
        "cow",
        "horse"
    ]

    # Unique comment for each animal, when applicable
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

    # Cumulative chain lines explaining why each animal was swallowed
    chain = {
        "bird": "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.",
        "cat": "She swallowed the cat to catch the bird.",
        "dog": "She swallowed the dog to catch the cat.",
        "goat": "She swallowed the goat to catch the dog.",
        "cow": "She swallowed the cow to catch the goat.",
        "spider": "She swallowed the spider to catch the fly.",
    }

    result = []  # Final list of lines for the full song or section

    for i in range(start_verse - 1, end_verse):
        animal = animals[i]
        verse = [f"I know an old lady who swallowed a {animal}."]

        # Add the animal-specific comment if one exists
        if comments[animal]:
            verse.append(comments[animal])

        # If it's the last verse (horse), end without the usual refrain
        if animal == "horse":
            result.extend(verse)
            continue

        # Build cumulative lines, walking back from current animal to the fly
        for j in range(i, -1, -1):
            curr_animal = animals[j]
            if curr_animal in chain:
                verse.append(chain[curr_animal])
            if curr_animal == "fly":
                verse.append("I don't know why she swallowed the fly. Perhaps she'll die.")
                break

        # Add verse to result
        result.extend(verse)

        # Add a blank line after each verse except the last
        if i != end_verse - 1:
            result.append("")

    return result
