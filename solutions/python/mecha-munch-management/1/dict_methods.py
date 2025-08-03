def add_item(current_cart, items_to_add):
    """
    Add items to a shopping cart. Increments the count for existing items or adds new ones with quantity 1.

    :param current_cart: dict - existing shopping cart with item quantities.
    :param items_to_add: iterable - list/tuple of items to be added.
    :return: dict - updated shopping cart.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1  # Increment count or initialize to 1
    return current_cart


def read_notes(notes):
    """
    Create a shopping cart from a list of items, assigning quantity 1 to each.

    :param notes: iterable - items listed by user.
    :return: dict - shopping cart with each item quantity set to 1.
    """
    return {item: 1 for item in notes}  # Each item added once


def update_recipes(ideas, recipe_updates):
    """
    Replace existing recipes or add new ones with a fresh set of ingredients.

    :param ideas: dict - current recipe ideas.
    :param recipe_updates: iterable - (recipe_name, ingredients_dict) updates.
    :return: dict - updated recipe dictionary.
    """
    for recipe, new_ingredients in recipe_updates:
        ideas[recipe] = new_ingredients.copy()  # Replace entire recipe with new ingredients
    return ideas


def sort_entries(cart):
    """
    Sort a shopping cart's items alphabetically by name.

    :param cart: dict - the shopping cart to sort.
    :return: dict - a new dictionary with sorted item keys.
    """
    return dict(sorted(cart.items()))  # Sort by key (item name)


def send_to_store(cart, aisle_mapping):
    """
    Merge cart quantities with aisle and refrigeration info and sort in reverse alphabetical order.

    :param cart: dict - user shopping cart.
    :param aisle_mapping: dict - maps items to [aisle, refrigeration] info.
    :return: dict - fulfillment-ready cart.
    """
    # Create a new dictionary where each item includes quantity, aisle, and refrigeration status
    fulfillment_cart = {
        item: [quantity, *aisle_mapping[item]] for item, quantity in cart.items()
    }
    return dict(sorted(fulfillment_cart.items(), reverse=True))  # Sort reverse alphabetically


def update_store_inventory(fulfillment_cart, store_inventory):
    """
    Deduct ordered items from store inventory or mark as 'Out of Stock' if quantity runs out.

    :param fulfillment_cart: dict - cart with quantities and store location info.
    :param store_inventory: dict - current inventory with available quantities.
    :return: dict - updated store inventory.
    """
    for item, (qty_ordered, aisle, refrigeration) in fulfillment_cart.items():
        available_qty = store_inventory[item][0]
        new_qty = available_qty - qty_ordered
        store_inventory[item][0] = new_qty if new_qty > 0 else 'Out of Stock'  # Decrement or mark out of stock
    return store_inventory
