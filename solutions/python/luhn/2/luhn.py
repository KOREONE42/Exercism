class Luhn:
    """
    Luhn algorithm validator for numerical identifiers such as credit card numbers.

    This class validates whether a given string of digits (optionally containing spaces)
    is valid according to the Luhn checksum formula.
    """

    def __init__(self, card_num: str):
        """
        Initializes the Luhn validator with a card number.

        Parameters:
        card_num (str): The identifier to validate. May include spaces.
        """
        self.card_num = card_num.replace(" ", "")  # Remove all spaces

    def valid(self) -> bool:
        """
        Validates the stored number using the Luhn algorithm.

        Returns:
        bool: True if the number is valid per the Luhn check, False otherwise.
        """
        # The number must be at least two digits and consist of only numeric characters
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        # Convert to a list of integers and reverse it for easier position handling
        digits = [int(char) for char in reversed(self.card_num)]

        # Apply Luhn transformation: double every second digit, subtract 9 if result > 9
        for i in range(1, len(digits), 2):
            doubled = digits[i] * 2
            digits[i] = doubled - 9 if doubled > 9 else doubled

        # Valid if the total sum is divisible by 10
        return sum(digits) % 10 == 0
