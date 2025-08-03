import re

class PhoneNumber:
    """
    A class to represent and validate a North American phone number (NANP format).

    Attributes:
        number (str): The cleaned, validated 10-digit phone number.
        area_code (str): The 3-digit area code of the phone number.

    Methods:
        pretty(): Returns the number formatted as (NXX)-NXX-XXXX.
        __str__(): Returns the same as pretty(), useful for print().
    """

    def __init__(self, number: str):
        """
        Initialize a PhoneNumber object, cleaning and validating input.

        Args:
            number (str): The raw input string containing the phone number.

        Raises:
            ValueError: If the number contains letters, invalid punctuation, incorrect length,
                        invalid country code, or invalid area/exchange codes.
        """

        # Check for alphabetic characters
        if re.search(r'[a-zA-Z]', number):
            raise ValueError("letters not permitted")

        # Check for invalid punctuation (anything not digit or standard symbols)
        if re.search(r'[^\d\s\+\-\.\(\)]', number):
            raise ValueError("punctuations not permitted")

        # Remove all non-digit characters
        digits = re.sub(r'\D', '', number)

        # Handle number length and possible country code
        if len(digits) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(digits) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(digits) == 11:
            if digits[0] != '1':
                raise ValueError("11 digits must start with 1")
            digits = digits[1:]

        # Validate area code
        if digits[0] in {'0', '1'}:
            raise ValueError("area code cannot start with zero" if digits[0] == '0' else "area code cannot start with one")

        # Validate exchange code
        if digits[3] in {'0', '1'}:
            raise ValueError("exchange code cannot start with zero" if digits[3] == '0' else "exchange code cannot start with one")

        # Save cleaned number and area code
        self.number = digits
        self.area_code = digits[:3]

    def pretty(self) -> str:
        """
        Return the formatted phone number in (NXX)-NXX-XXXX format.

        Returns:
            str: A user-friendly formatted phone number.
        """
        return f"({self.number[:3]})-{self.number[3:6]}-{self.number[6:]}"

    def __str__(self) -> str:
        """
        Return the string representation of the PhoneNumber instance.

        Returns:
            str: Same output as pretty(), useful when printing.
        """
        return self.pretty()
