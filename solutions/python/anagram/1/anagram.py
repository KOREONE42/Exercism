def find_anagrams(word, candidates):
    """
    This function finds and returns a list of words from the candidates that are anagrams of the target word.
    
    An anagram is a word formed by rearranging the letters of the target word. The function 
    ensures that the candidate word is not the same as the target word and considers case-insensitivity
    when determining if two words are anagrams.

    Args:
        word (str): The target word to check for anagrams.
        candidates (list of str): A list of candidate words to check against the target word.

    Returns:
        list: A list of words from the candidates that are anagrams of the target word.
    """
    
    # Normalize the target word to lowercase for comparison
    target_lower = word.lower()
    
    # List to store valid anagrams
    anagrams = []
    
    # Iterate through each candidate word
    for candidate in candidates:
        # If the candidate word is an anagram of the target word (not identical and characters match)
        if candidate.lower() != target_lower and sorted(candidate.lower()) == sorted(target_lower):
            anagrams.append(candidate)
    
    return anagrams
