import string

# Prepare the Atbash cipher mapping: a <-> z, b <-> y, ..., z <-> a
alphabet = string.ascii_lowercase
cipher_map = str.maketrans(alphabet, alphabet[::-1])

def encode(plain_text):
    """
    Encode a plaintext string using the Atbash cipher.

    - Converts all letters to lowercase.
    - Ignores punctuation.
    - Keeps numbers unchanged.
    - Groups output in chunks of 5 characters.

    Args:
        plain_text (str): The text to encode.

    Returns:
        str: The encoded ciphertext.
    """
    # Remove all non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in plain_text if char.isalnum())

    # Apply the Atbash cipher for letters; keep digits unchanged
    ciphered = ''.join(char.translate(cipher_map) if char.isalpha() else char for char in cleaned)

    # Group the result into chunks of 5 characters
    grouped = ' '.join(ciphered[i:i+5] for i in range(0, len(ciphered), 5))
    return grouped

def decode(ciphered_text):
    """
    Decode an Atbash ciphered string back to plaintext.

    - Removes spaces from grouped ciphertext.
    - Applies the same Atbash cipher (symmetric).
    - Keeps numbers unchanged.

    Args:
        ciphered_text (str): The encoded text to decode.

    Returns:
        str: The original decoded text.
    """
    # Remove spaces and convert to lowercase
    cleaned = ''.join(char.lower() for char in ciphered_text if char.isalnum())

    # Apply Atbash cipher (reversible)
    deciphered = ''.join(char.translate(cipher_map) if char.isalpha() else char for char in cleaned)
    return deciphered
