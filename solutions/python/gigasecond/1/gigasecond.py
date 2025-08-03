from datetime import timedelta

# Define a constant for one gigasecond (1,000,000,000 seconds)
GIGASECOND = 1_000_000_000

def add(moment):
    """
    Return the moment that is exactly one gigasecond (1,000,000,000 seconds)
    after the given datetime.

    Args:
        moment (datetime.datetime): The starting date and time.

    Returns:
        datetime.datetime: The date and time one gigasecond later.
    """
    # Add a timedelta of one gigasecond to the input moment
    return moment + timedelta(seconds=GIGASECOND)
