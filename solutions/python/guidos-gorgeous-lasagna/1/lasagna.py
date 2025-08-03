"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# Define the 'EXPECTED_BAKE_TIME' constant.
EXPECTED_BAKE_TIME = 40  # Assuming the expected bake time is 40 minutes.

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    remaining_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return remaining_time

def preparation_time_in_minutes(layers):
    """Calculate the preparation time in minutes.

    :param layers: int - number of layers in the lasagna.
    :return: int - preparation time (in minutes) based on the number of layers.

    Function that takes the number of layers in the lasagna and returns the total
    preparation time. Assuming each layer takes 2 minutes to prepare.
    """
    PREPARATION_TIME_PER_LAYER = 2  # Each layer takes 2 minutes to prepare
    return layers * PREPARATION_TIME_PER_LAYER

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Calculate the total elapsed time.

    :param layers: int - number of layers in the lasagna.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - total elapsed time (in minutes) including preparation and bake time.

    Function that takes the number of layers and the elapsed baking time as arguments
    and returns the total time spent on preparing and baking the lasagna.
    """
    prep_time = preparation_time_in_minutes(layers)
    total_elapsed_time = prep_time + elapsed_bake_time
    return total_elapsed_time