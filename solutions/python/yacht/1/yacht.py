# Score categories
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

from collections import Counter

def score(dice, category):
    """
    Calculate the score of a given roll of five dice according to the selected category.

    Parameters:
    - dice (list of int): A list of 5 integers, each from 1 to 6, representing the dice roll.
    - category (str): The scoring category to evaluate the roll against.

    Returns:
    - int: The score for the roll based on the selected category.
    """
    counts = Counter(dice)  # Count the occurrences of each die value

    if category == YACHT:
        # All five dice must be the same
        return 50 if len(counts) == 1 else 0

    elif category == ONES:
        return dice.count(1) * 1
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6

    elif category == FULL_HOUSE:
        # Full house requires one triplet and one pair (e.g., 3 of one number, 2 of another)
        if sorted(counts.values()) == [2, 3]:
            return sum(dice)
        return 0

    elif category == FOUR_OF_A_KIND:
        # Four or more of the same value; score is 4 times that value
        for num, cnt in counts.items():
            if cnt >= 4:
                return num * 4
        return 0

    elif category == LITTLE_STRAIGHT:
        # Exact sequence 1-2-3-4-5, regardless of order
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0

    elif category == BIG_STRAIGHT:
        # Exact sequence 2-3-4-5-6, regardless of order
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0

    elif category == CHOICE:
        # Sum of all dice, no constraints
        return sum(dice)

    return 0  # Default return for unrecognized categories
