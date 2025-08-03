# Define relationship constants used for comparison results
SUBLIST = 0       # list_one is a sublist of list_two
SUPERLIST = 1     # list_one is a superlist of list_two
EQUAL = 2         # list_one is equal to list_two
UNEQUAL = 3       # list_one and list_two are not equal or sub/super lists

def is_sublist(small, big):
    """
    Check if 'small' list is a contiguous sublist of 'big' list.

    Parameters:
    small (list): The potential sublist.
    big (list): The list in which to search for the sublist.

    Returns:
    bool: True if 'small' is a contiguous sublist of 'big', False otherwise.
    """
    if not small:
        return True  # An empty list is always considered a sublist
    len_small = len(small)
    for i in range(len(big) - len_small + 1):
        if big[i:i+len_small] == small:
            return True
    return False

def sublist(list_one, list_two):
    """
    Determine the relationship between two lists: equal, sublist, superlist, or unequal.

    Parameters:
    list_one (list): The first list to compare.
    list_two (list): The second list to compare.

    Returns:
    int: One of the constants SUBLIST, SUPERLIST, EQUAL, or UNEQUAL representing the relationship.
    """
    if list_one == list_two:
        return EQUAL
    elif is_sublist(list_one, list_two):
        return SUBLIST
    elif is_sublist(list_two, list_one):
        return SUPERLIST
    else:
        return UNEQUAL
