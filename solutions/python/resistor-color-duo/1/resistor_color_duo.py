def value(colors):
    """
    Given a list of resistor color bands, return the resistance value represented by the first two colors.

    Parameters:
    colors (list): A list of color names as strings. Only the first two are considered.

    Returns:
    int: A two-digit number formed by the mapped values of the first two color bands.
    """
    
    # Mapping of resistor color codes to digit values
    color_map = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9
    }

    # Convert the first two color names to their corresponding digit values
    first_two_digits = [color_map[color] for color in colors[:2]]

    # Concatenate the two digits into a number and return it as an integer
    return int(f"{first_two_digits[0]}{first_two_digits[1]}")
