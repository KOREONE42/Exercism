def flatten(iterable):
    """
    Flattens a nested iterable (list) of any depth and removes any `None` values.
    
    Args:
    iterable (list): The input nested list which may contain other lists or values.
    
    Returns:
    list: A new list that contains all the non-None elements from the input, flattened into one list.
    """
    
    result = []  # Initialize an empty list to store the flattened values.
    
    # Loop through each item in the iterable (which could be a list or a non-list element)
    for item in iterable:
        # If the item is a list, recursively flatten it and extend the result list.
        if isinstance(item, list):
            result.extend(flatten(item))
        # If the item is not None, append it to the result list.
        elif item is not None:
            result.append(item)
    
    return result  # Return the fully flattened list.
