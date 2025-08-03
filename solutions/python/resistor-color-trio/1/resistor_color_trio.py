def label(colors):
    """
    Given a list of 3 color names representing the bands of a resistor,
    return its resistance value as a string with the appropriate unit
    (ohms, kiloohms, megaohms, gigaohms).

    Parameters:
    colors (List[str]): List of exactly three resistor color bands.

    Returns:
    str: Formatted resistance value with units.
    """
    
    # Mapping of colors to their corresponding digit values
    color_map = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6,
        "violet": 7, "grey": 8, "white": 9
    }

    # Extract digits from colors
    first_digit = color_map[colors[0]]
    second_digit = color_map[colors[1]]
    multiplier = color_map[colors[2]]

    # Compute total resistance value
    value = (first_digit * 10 + second_digit) * (10 ** multiplier)

    # Determine the appropriate unit
    if value >= 1_000_000_000 and value % 1_000_000_000 == 0:
        return f"{value // 1_000_000_000} gigaohms"
    elif value >= 1_000_000 and value % 1_000_000 == 0:
        return f"{value // 1_000_000} megaohms"
    elif value >= 1_000 and value % 1_000 == 0:
        return f"{value // 1_000} kiloohms"
    else:
        return f"{value} ohms"
