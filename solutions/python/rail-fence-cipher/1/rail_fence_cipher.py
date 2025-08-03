def encode(message, rails):
    """
    Encodes a message using the Rail Fence Cipher.

    Args:
        message (str): The input string to be encoded.
        rails (int): The number of rails to use for the zigzag pattern.

    Returns:
        str: The encoded message.
    """
    if rails == 1:
        return message

    # Initialize each rail as an empty string
    rail_matrix = ['' for _ in range(rails)]

    current_rail = 0
    direction = 1  # 1 means moving down, -1 means moving up

    for char in message:
        # Append character to the current rail
        rail_matrix[current_rail] += char
        current_rail += direction

        # Change direction if we hit the top or bottom rail
        if current_rail == 0 or current_rail == rails - 1:
            direction *= -1

    # Combine all rails to produce the final encoded message
    return ''.join(rail_matrix)


def decode(encoded_message, rails):
    """
    Decodes a message encoded with the Rail Fence Cipher.

    Args:
        encoded_message (str): The encoded string.
        rails (int): The number of rails used during encoding.

    Returns:
        str: The original decoded message.
    """
    if rails == 1:
        return encoded_message

    length = len(encoded_message)

    # Step 1: Mark the zigzag path using placeholders
    zigzag = [['' for _ in range(length)] for _ in range(rails)]
    idx = 0
    direction = 1
    for col in range(length):
        zigzag[idx][col] = '?'  # Placeholder for future characters
        idx += direction

        if idx == 0 or idx == rails - 1:
            direction *= -1

    # Step 2: Replace placeholders with actual characters from the encoded message
    msg_idx = 0
    for r in range(rails):
        for c in range(length):
            if zigzag[r][c] == '?' and msg_idx < length:
                zigzag[r][c] = encoded_message[msg_idx]
                msg_idx += 1

    # Step 3: Read characters in zigzag order to decode the message
    result = []
    idx = 0
    direction = 1
    for col in range(length):
        result.append(zigzag[idx][col])
        idx += direction

        if idx == 0 or idx == rails - 1:
            direction *= -1

    return ''.join(result)
