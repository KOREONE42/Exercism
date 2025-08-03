def two_fer(name=None):
    """
    Generate a message for giving away a cookie in a 'two-fer' deal.

    If a name is provided and not just whitespace, the message will include the name.
    Otherwise, it defaults to using "you".

    Parameters:
    name (str, optional): The name of the person receiving the extra cookie.

    Returns:
    str: A string in the format "One for <name>, one for me."
    """
    # Check if a valid name is provided; strip whitespace to avoid empty or blank strings
    recipient = name.strip() if name and name.strip() else "you"
    
    # Return the formatted message
    return f"One for {recipient}, one for me."
