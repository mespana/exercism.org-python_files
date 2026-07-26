"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(actual_time):
    """Calculate the bake time remaining.

    Parameters:
        actual_time (int): The actual baking time.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME' - 'actual_time'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """    
    
    return EXPECTED_BAKE_TIME - actual_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time.
    Paramenters:
    number_of_layers(int): The number of layers add to the lasagna.
    
    Returns:
    int: The preparation time in minutes derived from 'number_of_layers' * 'PREPARATION_TIME'.
    """
    
    return number_of_layers * PREPARATION_TIME



def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed bake time in minutes.
    Parameters:
        number of layers (int): The number of layers added to the lasagna.
        elapsed_bake_time (int): The number of minutes the lasagna has spent baking in the oven already.

    Returns:
        int: The elapsed time (in minutes) derived from (preparation_time_in_minutes * 'PREPARATION_TIME') - 'elapsed_bake_time'.

    Function that takes the preparation time given the number of layers added time the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna has been baked or elapsed cooking time in minutes.
    """    
    number_of_layers = number_of_layers * PREPARATION_TIME
    return number_of_layers + elapsed_bake_time

