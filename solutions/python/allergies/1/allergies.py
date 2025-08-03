class Allergies:
    # List of known allergens and their corresponding scores.
    # The order here is important if you wish to maintain the same sequence.
    all_allergens = [
        ("eggs", 1),
        ("peanuts", 2),
        ("shellfish", 4),
        ("strawberries", 8),
        ("tomatoes", 16),
        ("chocolate", 32),
        ("pollen", 64),
        ("cats", 128)
    ]
    
    def __init__(self, score):
        # Only consider the lower eight bits by taking modulo 256.
        self.score = score % 256
    
    def allergic_to(self, item):
        """
        Returns True if the person is allergic to the given item,
        False otherwise.
        """
        for allergen, val in Allergies.all_allergens:
            if allergen == item:
                return (self.score & val) != 0
        # If the item is not in the known allergens list, we return False.
        return False
        
    @property
    def lst(self):
        """
        Returns a list of allergens (names) to which the person is allergic.
        """
        return [allergen for allergen, val in Allergies.all_allergens if (self.score & val)]
