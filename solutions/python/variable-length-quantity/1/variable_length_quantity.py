def encode(numbers):
    """
    Encodes a list of 32-bit unsigned integers using Variable Length Quantity (VLQ).

    VLQ encoding uses 7 bits per byte to store the integer value.
    All bytes except the last have their most significant bit (MSB) set to 1.
    The last byte has its MSB set to 0.

    Args:
        numbers (list[int]): List of integers to encode.

    Returns:
        list[int]: VLQ-encoded byte stream.
    """
    encoded_bytes = []

    for number in numbers:
        # Special case for 0
        if number == 0:
            encoded_bytes.append(0x00)
            continue

        bytes_ = []
        while number > 0:
            # Take the lowest 7 bits
            bytes_.insert(0, number & 0x7F)
            number >>= 7

        # Set the MSB of all bytes except the last
        for i in range(len(bytes_) - 1):
            bytes_[i] |= 0x80

        encoded_bytes.extend(bytes_)

    return encoded_bytes


def decode(bytes_):
    """
    Decodes a list of VLQ-encoded bytes into integers.

    It reconstructs integers from 7-bit chunks.
    The continuation bit (MSB) determines if the current byte ends the sequence.
    If a sequence ends unexpectedly (without an MSB=0 byte), it raises a ValueError.

    Args:
        bytes_ (list[int]): List of VLQ-encoded bytes.

    Returns:
        list[int]: Decoded list of integers.

    Raises:
        ValueError: If byte sequence is incomplete.
    """
    numbers = []
    current = 0
    ongoing = False

    for byte in bytes_:
        ongoing = True
        # Append 7 bits to current value
        current = (current << 7) | (byte & 0x7F)

        # MSB 0 means end of this value
        if byte & 0x80 == 0:
            numbers.append(current)
            current = 0
            ongoing = False

    # If sequence ends mid-number, raise error
    if ongoing:
        raise ValueError("incomplete sequence")

    return numbers
