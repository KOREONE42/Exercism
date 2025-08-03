import re
from itertools import permutations

def solve(puzzle):
    # Remove spaces and normalize equals
    expr = puzzle.replace(' ', '')
    # Support both = and ==
    if '==' in expr:
        left, _, right = expr.partition('==')
    else:
        left, _, right = expr.partition('=')

    # Split addends and result
    terms = left.split('+')
    words = terms + [right]

    # Collect unique letters
    unique_letters = sorted({ch for word in words for ch in word})
    if len(unique_letters) > 10:
        return None  # Impossible if more than 10 letters

    # Leading letters cannot be '0'
    leading = {word[0] for word in words if len(word) > 1}

    # Try all digit assignments
    digits = '0123456789'
    for perm in permutations(digits, len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        # Skip if any leading letter is assigned '0'
        if any(mapping[ch] == '0' for ch in leading):
            continue

        # Convert words to numbers
        values = []
        for word in words:
            num = int(''.join(mapping[ch] for ch in word))
            values.append(num)

        # Check sum of addends equals result
        if sum(values[:-1]) == values[-1]:
            # Convert mapping to int values and return
            return {ch: int(d) for ch, d in mapping.items()}

    return None  # No solution found