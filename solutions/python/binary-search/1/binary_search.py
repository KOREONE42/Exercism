def find(search_list, value):
    """
    Perform a binary search to find the index of `value` in `search_list`.

    Parameters:
    - search_list (list): A sorted list of elements to search.
    - value: The value to search for in the list.

    Returns:
    - int: The index of `value` in `search_list` if found.

    Raises:
    - ValueError: If `value` is not present in `search_list`.
    """
    # Initialize the search boundaries
    low = 0
    high = len(search_list) - 1

    # Continue searching while there is a valid range
    while low <= high:
        # Find the middle index
        mid = (low + high) // 2
        mid_val = search_list[mid]

        # Check if the middle element is the target
        if mid_val == value:
            return mid
        # If the target is greater, discard the left half
        elif mid_val < value:
            low = mid + 1
        # If the target is smaller, discard the right half
        else:
            high = mid - 1

    # If value is not found in the list, raise an exception
    raise ValueError("value not in array")
