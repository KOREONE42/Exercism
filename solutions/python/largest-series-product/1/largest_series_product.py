def largest_product(series, size):
    # Validate span is not negative.
    if size < 0:
        raise ValueError("span must not be negative")
    
    # Validate that all characters in series are digits.
    if any(ch not in "0123456789" for ch in series):
        raise ValueError("digits input must only contain digits")
    
    # For cases when size is greater than the length of the series.
    if size > len(series):
        raise ValueError("span must be smaller than string length")
    
    # When span is 0, the product of no numbers is defined as 1.
    if size == 0:
        return 1

    max_product = 0
    # Iterate through all substrings (series) of the given size.
    for i in range(len(series) - size + 1):
        substring = series[i:i+size]
        product = 1
        # Calculate the product of the digits in the substring.
        for ch in substring:
            product *= int(ch)
        if product > max_product:
            max_product = product
    return max_product
