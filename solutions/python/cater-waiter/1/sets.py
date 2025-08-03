"""Functions for compiling dishes and ingredients for a catering company."""

from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients`."""
    return (dish_name, set(dish_ingredients))


def check_drinks(drink_name, drink_ingredients):
    """Append "Cocktail" or "Mocktail" to `drink_name` based on `drink_ingredients`."""
    if set(drink_ingredients) & ALCOHOLS:
        return f"{drink_name} Cocktail"
    else:
        return f"{drink_name} Mocktail"


def categorize_dish(dish_name, dish_ingredients):
    """Categorize `dish_name` based on `dish_ingredients`."""
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
    """Compare `dish` ingredients to `SPECIAL_INGREDIENTS`."""
    name, ingredients = dish
    return (name, set(ingredients) & SPECIAL_INGREDIENTS)


def compile_ingredients(dishes):
    """Create a master list of ingredients."""
    return set().union(*dishes)


def separate_appetizers(dishes, appetizers):
    """Remove appetizer dishes from the full dish list."""
    return list(set(dishes) - set(appetizers))


def singleton_ingredients(dishes, intersection):
    """Return ingredients that appear only in one dish."""
    all_ingredients = set().union(*dishes)
    return all_ingredients - intersection
