class Luhn:
    """
    A class to validate numerical identifiers (e.g. credit card numbers)
    using the Luhn algorithm.
    """

    def __init__(self, card_num):
        """
        Initialize the Luhn validator.

        Parameters:
        card_num (str): The input number as a string. It may include spaces.
        """
        # Remove all spaces from the input
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        """
        Check if the provided card number is valid according to the Luhn algorithm.

        Returns:
        bool: True if the number is valid, False otherwise.
        """
        # A valid number must contain only digits and be longer than 1 character
        if len(self.card_num) <= 1 or not self.card_num.isdigit():
            return False

        # Convert string to a list of integers
        digits = [int(d) for d in self.card_num]

        # Reverse the digits to simplify indexing for doubling
        digits = digits[::-1]

        # Double every second digit from the right (now every odd index due to reversal)
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            # Subtract 9 if doubling results in a number > 9
            if digits[i] > 9:
                digits[i] -= 9

        # Sum all the digits
        total = sum(digits)

        # If total modulo 10 is 0, the number is valid
        return total % 10 == 0
