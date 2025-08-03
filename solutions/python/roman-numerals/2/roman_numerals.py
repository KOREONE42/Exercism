def roman(number):
    """
    Convert an integer to a Roman numeral (1 to 3999).

    Args:
        number (int): The number to convert. Must be in the range 1–3999.

    Returns:
        str: A string representing the Roman numeral equivalent of the input number.

    Example:
        >>> roman(104)
        'CIV'
        >>> roman(3999)
        'MMMCMXCIX'
    """
    
    # Roman numeral mappings in descending order.
    # Includes standard and subtractive notation (like IV for 4, CM for 900, etc.)
    roman_numerals = [
        (1000, 'M'), (900, 'CM'),
        (500, 'D'),  (400, 'CD'),
        (100, 'C'),  (90, 'XC'),
        (50, 'L'),   (40, 'XL'),
        (10, 'X'),   (9, 'IX'),
        (5, 'V'),    (4, 'IV'),
        (1, 'I')
    ]

    result = ""  # Initialize the Roman numeral result as an empty string

    # Loop through the numeral mapping
    for value, symbol in roman_numerals:
        count = number // value  # Determine how many times the symbol fits into the number
        result += symbol * count  # Append the symbol 'count' times
        number -= value * count   # Reduce the number by the total value added

        # Early exit if number reaches zero (optional but efficient)
        if number == 0:
            break

    return result
