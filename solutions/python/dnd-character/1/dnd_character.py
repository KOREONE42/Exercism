import random
import math

def modifier(value):
    """
    Calculate the ability modifier for a given ability score.

    In Dungeons & Dragons, the modifier is calculated as:
    (score - 10) // 2, rounding down.

    Args:
        value (int): The ability score.

    Returns:
        int: The corresponding modifier.
    """
    return math.floor((value - 10) / 2)

class Character:
    """
    A class representing a randomly generated Dungeons & Dragons character.

    Each character has six ability scores:
    - Strength
    - Dexterity
    - Constitution
    - Intelligence
    - Wisdom
    - Charisma

    These scores are determined by rolling four 6-sided dice,
    discarding the lowest roll, and summing the remaining three.

    Hitpoints are calculated as 10 + constitution modifier.
    """

    def __init__(self):
        """
        Initialize a new Character with randomized abilities and hitpoints.
        """
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        """
        Generate a single ability score by rolling four 6-sided dice,
        discarding the lowest value, and summing the rest.

        Returns:
            int: The resulting ability score (range 3 to 18).
        """
        rolls = [random.randint(1, 6) for _ in range(4)]  # Roll 4d6
        rolls.sort()
        return sum(rolls[1:])  # Drop the lowest roll and sum the top three
