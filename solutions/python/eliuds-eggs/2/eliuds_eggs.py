def egg_count(display_value):
    """
    Count the number of eggs in the coop based on the binary representation of the display value.

    Each '1' bit in the binary representation indicates a nest with an egg.
    This function manually computes the number of 1s without using built-in bit counting methods.

    Parameters:
    display_value (int): The decimal number shown on the coop's display.

    Returns:
    int: The number of eggs (1s) in the binary representation of the input.
    """
    count = 0
    while display_value > 0:
        # Divide the number by 2 and get the remainder
        display_value, remainder = divmod(display_value, 2)
        # If remainder is 1, it means there's an egg in that position
        if remainder == 1:
            count += 1
    return count
