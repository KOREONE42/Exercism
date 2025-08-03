def resistor_label(colors):
    """
    Convert resistor color bands into a readable resistance label with tolerance.

    Supports 1, 4, and 5-band resistors.

    :param colors: list - list of color band strings.
    :return: str - formatted resistor value with tolerance.
    """
    color_digit = {
        "black": 0, "brown": 1, "red": 2, "orange": 3,
        "yellow": 4, "green": 5, "blue": 6,
        "violet": 7, "grey": 8, "white": 9
    }

    tolerance_map = {
        "grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%",
        "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"
    }

    if len(colors) == 1 and colors[0] == "black":
        return "0 ohms"

    if len(colors) == 4:
        a, b, m, t = colors
        value = int(f"{color_digit[a]}{color_digit[b]}")
        multiplier = 10 ** color_digit[m]
        tolerance = tolerance_map[t]

    elif len(colors) == 5:
        a, b, c, m, t = colors
        value = int(f"{color_digit[a]}{color_digit[b]}{color_digit[c]}")
        multiplier = 10 ** color_digit[m]
        tolerance = tolerance_map[t]
    else:
        raise ValueError("Invalid number of color bands. Must be 1, 4, or 5.")

    total = value * multiplier

    # Format with decimal precision when needed
    if total >= 1_000_000:
        result = total / 1_000_000
        label = f"{result:.2f}".rstrip('0').rstrip('.') + " megaohms"
    elif total >= 1_000:
        result = total / 1_000
        label = f"{result:.2f}".rstrip('0').rstrip('.') + " kiloohms"
    else:
        label = f"{total} ohms"

    return f"{label} {tolerance}"
