def rotate(text, key):
    """
    Applies a Caesar cipher (rotational cipher) to the input text using the specified key.

    Parameters:
    - text (str): The input string to encrypt or decrypt.
    - key (int): The rotation key (0 to 26). A key of 0 or 26 leaves the text unchanged.

    Returns:
    - str: The result of applying the Caesar cipher to the input text.
    """
    result = []

    for char in text:
        if char.isupper():
            # Rotate uppercase letters within 'A'-'Z'
            base = ord('A')
            rotated = chr((ord(char) - base + key) % 26 + base)
            result.append(rotated)
        elif char.islower():
            # Rotate lowercase letters within 'a'-'z'
            base = ord('a')
            rotated = chr((ord(char) - base + key) % 26 + base)
            result.append(rotated)
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)

    return ''.join(result)
