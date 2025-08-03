def is_isogram(string):
    normalized = string.lower()
    seen = set()

    for char in normalized:
        if char in (' ', '-'):
            continue
        if char in seen:
            return False
        seen.add(char)

    return True
