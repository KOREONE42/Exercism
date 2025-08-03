"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS
)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicate ingredients from a dish.

    :param dish_name: str - name of the dish.
    :param dish_ingredients: list - ingredients used in the dish.
    :return: tuple - (dish_name, set of unique ingredients).
    """
    # Convert ingredient list to a set to remove duplicates
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Classify a drink as either 'Mocktail' or 'Cocktail'.

    :param drink_name: str - name of the drink.
    :param drink_ingredients: list - ingredients in the drink.
    :return: str - drink_name followed by "Mocktail" or "Cocktail".
    """
    # If any ingredient is in the ALCOHOLS set, it is a Cocktail
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    # Otherwise, it's a Mocktail
    return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize a dish into VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE.

    :param dish_name: str - name of the dish.
    :param dish_ingredients: set - unique ingredients in the dish.
    :return: str - formatted as 'dish_name: CATEGORY'.
    """
    # Check ingredient subset against each dietary category
    if dish_ingredients.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_ingredients.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_ingredients.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_ingredients.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


def tag_special_ingredients(dish):
    """Identify special or allergenic ingredients in a dish.

    :param dish: tuple - (dish name, list/set of ingredients).
    :return: tuple - (dish name, set of special ingredients).
    """
    name, ingredients = dish
    # Identify overlap with SPECIAL_INGREDIENTS set
    return (name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """Compile a master list of ingredients from multiple dishes.

    :param dishes: list - of ingredient sets (one set per dish).
    :return: set - all unique ingredients across all dishes.
    """
    # Use set union to combine all ingredient sets
    return set().union(*dishes)


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from the main dish list.

    :param dishes: list - all dish names (may include duplicates).
    :param appetizers: list - appetizer names (may include duplicates).
    :return: list - dishes excluding appetizers.
    """
    # Remove appetizer dishes by using set difference
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """Identify ingredients that appear in only one dish.

    :param dishes: list - list of ingredient sets (one per dish).
    :param intersection: set - ingredients common to multiple dishes.
    :return: set - ingredients unique to a single dish.
    """
    # Combine all ingredients and subtract those in multiple dishes
    all_ingredients = set().union(*dishes)
    return all_ingredients - intersection
