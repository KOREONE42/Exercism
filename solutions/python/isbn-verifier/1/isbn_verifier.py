def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace('-', '')
    
    # Check length
    if len(isbn) != 10:
        return False

    # Check characters: first 9 must be digits, last can be digit or 'X'
    if not all(c.isdigit() for c in isbn[:9]):
        return False
    if not (isbn[9].isdigit() or isbn[9] == 'X'):
        return False

    # Convert characters to numeric values
    total = 0
    for i, char in enumerate(isbn):
        if char == 'X':
            value = 10
        else:
            value = int(char)
        weight = 10 - i
        total += value * weight

    # Check validity
    return total % 11 == 0
