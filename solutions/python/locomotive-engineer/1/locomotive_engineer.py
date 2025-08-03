def get_list_of_wagons(*wagons):
    """Return a list of wagons.

    :param wagons: arbitrary number of wagons.
    :return: list - list of wagons.
    """
    return list(wagons)


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    - Move first two wagons to the end of the list.
    - Insert missing wagons after the locomotive (ID 1).

    :param each_wagons_id: list - the list of wagons.
    :param missing_wagons: list - the list of missing wagons.
    :return: list - updated list of wagons.
    """
    # Move first two wagons to the end
    first_two, rest = each_wagons_id[:2], each_wagons_id[2:]
    adjusted_wagons = rest + first_two

    # Find the index of the locomotive (ID 1)
    loco_index = adjusted_wagons.index(1)

    # Insert missing wagons after the locomotive
    return (
        adjusted_wagons[:loco_index + 1]
        + missing_wagons
        + adjusted_wagons[loco_index + 1:]
    )


def add_missing_stops(route, **stops):
    """Add missing stops to route dict.

    :param route: dict - the dict of routing information.
    :param stops: keyword arguments - variable number of stops.
    :return: dict - updated route dictionary.
    """
    route["stops"] = list(stops.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    :param route: dict - the route information.
    :param more_route_information: dict - extra route information.
    :return: dict - extended route information.
    """
    return {**route, **more_route_information}


def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Transpose a 3x3 grid of wagons to align by column color.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    return [list(row) for row in zip(*wagons_rows)]
