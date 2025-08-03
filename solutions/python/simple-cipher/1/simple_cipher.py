import random
import string

class Cipher:
    def __init__(self, key=None):
        """
        Initializes the cipher with a key.
        
        If a key is provided, it must consist of only lowercase letters.
        If no key is provided, a random key of 100 lowercase letters is generated.
        """
        if key:
            # Verify that the provided key contains only lowercase alphabetical letters.
            if not key.isalpha() or not key.islower():
                raise ValueError("Key must contain only lowercase letters")
            self.key = key
        else:
            # Generate a random key of length 100 using lowercase letters.
            self.key = ''.join(random.choice(string.ascii_lowercase) for _ in range(100))
    
    def encode(self, text):
        """
        Encodes the given text using the substitution cipher.

        Each letter in the plaintext is shifted by an amount corresponding to the letter in the key.
        For example, if the key letter is 'd' (which represents a shift of 3 since a=0, b=1, c=2, d=3),
        then plaintext letter 'i' (index 8) becomes 'l' (index (8+3) % 26 = 11).
        Characters in the text that are not lowercase alphabet letters are preserved.
        """
        encoded = []
        # Process each letter in the text
        for i, letter in enumerate(text):
            if letter.isalpha() and letter.islower():
                # Convert plaintext letter to index 0-25.
                p = ord(letter) - ord('a')
                # Use the corresponding letter in the key (repeating if necessary)
                key_letter = self.key[i % len(self.key)]
                k = ord(key_letter) - ord('a')
                # Compute the new letter index using a circular shift of 26 letters.
                e = (p + k) % 26
                encoded_letter = chr(e + ord('a'))
                encoded.append(encoded_letter)
            else:
                # Leave non-lowercase letters (and non-alphabetical characters) unchanged.
                encoded.append(letter)
        return ''.join(encoded)
    
    def decode(self, text):
        """
        Decodes the given text using the substitution cipher.

        Each letter in the ciphertext is shifted back by the shift amount derived from the corresponding
        letter in the key (again, with the key repeating as needed).
        Characters that are not lowercase alphabet letters are preserved.
        """
        decoded = []
        for i, letter in enumerate(text):
            if letter.isalpha() and letter.islower():
                c = ord(letter) - ord('a')
                key_letter = self.key[i % len(self.key)]
                k = ord(key_letter) - ord('a')
                # Reverse the shift, ensuring the result stays in the 0-25 range.
                p = (c - k) % 26
                decoded_letter = chr(p + ord('a'))
                decoded.append(decoded_letter)
            else:
                decoded.append(letter)
        return ''.join(decoded)
