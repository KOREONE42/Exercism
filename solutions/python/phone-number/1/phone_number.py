import re

class PhoneNumber:
    """
    A class to represent and validate a North American phone number (NANP format).

    Attributes:
        number (str): The cleaned, validated 10-digit phone number.
        area_code (str): The 3-digit area code extracted from the phone number.

    Methods:
        pretty(): Returns the phone number in the format (NXX)-NXX-XXXX.
    """

    def __init__(self, number):
        """
        Initializes and validates a PhoneNumber object.

        Args:
            number (str): The raw input string representing a phone number.

        Raises:
            ValueError: If the number contains letters or unacceptable punctuation.
            ValueError: If the number has too few or too many digits.
            ValueError: If the number has an invalid country code, area code, or exchange code.
        """

        # Raise error if input contains any letters
        if re.search(r'[a-zA-Z]', number):
            raise ValueError("letters not permitted")

        # Raise error if input contains punctuation other than standard phone symbols
        if re.search(r'[^\d\+\-\.\(\) ]', number):
            raise ValueError("punctuations not permitted")

        # Strip all non-digit characters
        digits = re.sub(r'\D', '', number)

        # Check digit count and handle country code
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        elif len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        elif len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]  # Strip leading country code

        # Validate area code (first digit must be 2–9)
        if digits[0] == '0':
            raise ValueError("area code cannot start with zero")
        if digits[0] == '1':
            raise ValueError("area code cannot start with one")

        # Validate exchange code (4th digit, index 3, must be 2–9)
        if digits[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if digits[3] == '1':
            raise ValueError("exchange code cannot start with one")

        # Store valid number and area code
        self.number = digits
        self.area_code = digits[:3]

    def pretty(self):
        """
        Returns the formatted phone number in (NXX)-NXX-XXXX style.

        Returns:
            str: The phone number in a user-friendly display format.
        """
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"
