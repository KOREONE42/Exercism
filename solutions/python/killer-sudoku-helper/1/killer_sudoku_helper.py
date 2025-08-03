from itertools import combinations as iter_combinations

def combinations(target, size, exclude):
    """
    Generate all valid digit combinations for a Killer Sudoku cage.

    Parameters:
        target (int): The target sum the digits must add up to.
        size (int): The number of digits in the cage.
        exclude (list[int]): Digits to exclude (due to Sudoku constraints like same row, column, or box).

    Returns:
        list[list[int]]: A sorted list of valid digit combinations (no repeats, all digits 1–9, obeying exclusions).
    """
    # Step 1: Generate allowed digits from 1 to 9, excluding those already present in row/col/box
    digits = [d for d in range(1, 10) if d not in exclude]

    # Step 2: Generate all unique combinations of the given size from allowed digits
    # and filter those whose sum equals the target
    valid_combos = [
        list(combo) for combo in iter_combinations(digits, size)
        if sum(combo) == target
    ]

    # Step 3: Return the combinations sorted in lexicographical order
    return sorted(valid_combos)
