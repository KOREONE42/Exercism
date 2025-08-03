def slices(series, length):
    """
    Generate all contiguous substrings of the given length from the input string.

    Parameters:
    series (str): The input string of digits from which substrings are to be generated.
    length (int): The length of each substring.

    Returns:
    list: A list containing the contiguous substrings of the specified length.

    Raises:
    ValueError: If any of the following conditions are met:
        - The series is empty.
        - The length is zero.
        - The length is negative.
        - The length is greater than the series length.
    """
    
    # Check if the input series is empty
    if not series:
        raise ValueError("series cannot be empty")
    
    # Check if the length is zero and raise an error with a specific message
    if length == 0:
        raise ValueError("slice length cannot be zero")
    
    # Check if the length is negative and raise an error with a specific message
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    
    # Check if the requested slice length is greater than the length of the series
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")
    
    # Generate and return the contiguous substrings of the given length
    return [series[i:i+length] for i in range(len(series) - length + 1)]
