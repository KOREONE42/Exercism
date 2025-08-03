from collections import Counter

# Define all scoring categories as constants
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

def score(dice, category):
    """
    Calculate the score for a given roll of five dice based on the specified category.

    Args:
        dice (list of int): A list of five integers (1 through 6) representing the dice roll.
        category (str): A string indicating which scoring category to use.

    Returns:
        int: The score for the roll based on the chosen category.
    """
    counts = Counter(dice)  # Get frequency of each die face (e.g., {3: 2, 5: 3})

    if category == YACHT:
        # Yacht: All five dice must be the same
        return 50 if len(counts) == 1 else 0

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        # Scoring for numbered categories (e.g., ONES = 1 × number of 1s)
        target = {
            ONES: 1,
            TWOS: 2,
            THREES: 3,
            FOURS: 4,
            FIVES: 5,
            SIXES: 6
        }[category]
        return dice.count(target) * target

    if category == FULL_HOUSE:
        # Full House: 3 of one number and 2 of another (e.g., [2,2,4,4,4])
        values = sorted(counts.values())
        return sum(dice) if values == [2, 3] else 0

    if category == FOUR_OF_A_KIND:
        # Four of a Kind: At least four dice with the same number
        for num, count in counts.items():
            if count >= 4:
                return num * 4
        return 0

    if category == LITTLE_STRAIGHT:
        # Little Straight: 1-2-3-4-5
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    if category == BIG_STRAIGHT:
        # Big Straight: 2-3-4-5-6
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    if category == CHOICE:
        # Choice: Sum of all dice, no restrictions
        return sum(dice)

    return 0  # Fallback in case of an unrecognized category
