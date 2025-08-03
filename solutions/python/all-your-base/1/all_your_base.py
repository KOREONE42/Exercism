def rebase(input_base, digits, output_base):
    # Input validation
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if any(d < 0 or d >= input_base for d in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if not digits:
        return [0]

    # Strip leading zeros
    while digits and digits[0] == 0:
        digits = digits[1:]
    if not digits:
        return [0]

    # Convert from input_base to decimal
    decimal_value = 0
    for d in digits:
        decimal_value = decimal_value * input_base + d

    # Convert from decimal to output_base
    output_digits = []
    if decimal_value == 0:
        return [0]
    while decimal_value > 0:
        output_digits.append(decimal_value % output_base)
        decimal_value //= output_base

    return output_digits[::-1]
