
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 0

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    bake_time = EXPECTED_BAKE_TIME - elapsed_bake_time
    return bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the time to prep the layers of lasagna.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int: - the total time per layer which is number of layers times 2.

    This function returns the total amount of time to prep the number of layers of lasagna.
    """
    return (number_of_layers*2)

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the time already spent
    baking and calculates the total elapsed minutes spetn cooking the lasagna.
    """
    return(preparation_time_in_minutes(number_of_layers) + elapsed_bake_time)

