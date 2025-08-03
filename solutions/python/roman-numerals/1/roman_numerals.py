def roman(number):
    """
    Convert an integer to a Roman numeral.

    Parameters:
    number (int): The integer to convert. Must be between 1 and 3999.

    Returns:
    str: The Roman numeral representation of the input number.

    Example:
    >>> roman(1996)
    'MCMXCVI'
    """
    
    # List of tuples mapping integer values to Roman numerals, ordered from highest to lowest.
    # Includes special subtractive cases like 900 ("CM"), 4 ("IV"), etc.
    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    result = ""  # Initialize the result string to build the Roman numeral

    # Loop through each (value, symbol) pair
    for value, numeral in roman_numerals:
        # While the current number is greater than or equal to the value,
        # subtract the value and append the Roman numeral to the result
        while number >= value:
            result += numeral
            number -= value
    
    return result
