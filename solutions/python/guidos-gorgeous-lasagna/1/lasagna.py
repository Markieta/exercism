EXPECTED_BAKE_TIME = 40  # in minutes
PREPARATION_TIME = 2     # in minutes per layer


def bake_time_remaining(elapsed_bake_time: int) -> int:
    """Calculate the bake time remaining."""

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time based on the number of layers."""

    return PREPARATION_TIME * number_of_layers


def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time."""

    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
