def translate(text):
    def translate_word(word):
        vowels = 'aeiou'
        # Rule 1: Words beginning with vowel sounds
        if word.startswith(('xr', 'yt')) or word[0] in vowels:
            return word + 'ay'

        # Rule 2 and 3: Consonant clusters including 'qu'
        i = 0
        while i < len(word):
            # Special handling for 'qu'
            if word[i:i+2] == 'qu':
                i += 2
                continue
            # Treat 'y' as a vowel only if no vowel has been found yet
            if word[i] in vowels or (word[i] == 'y' and i != 0):
                break
            i += 1
        return word[i:] + word[:i] + 'ay'

    return ' '.join(translate_word(word) for word in text.split())
