def is_pangram(sentence):
    # Normalize to lowercase
    sentence = sentence.lower()
    # Create a set of all letters in the sentence
    letters = set(char for char in sentence if char.isalpha())
    # Check if the set has all 26 letters
    return len(letters) == 26

# Example usage for demonstration
test_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Hello world!",
    "Pack my box with five dozen liquor jugs.",
    "Sphinx of black quartz, judge my vow.",
    "Not a pangram at all"
]

results = {s: is_pangram(s) for s in test_sentences}
results
