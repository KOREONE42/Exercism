from datetime import datetime, timedelta

def add(moment: datetime) -> datetime:
    """
    Calculate the date and time that occurs exactly one gigasecond (1,000,000,000 seconds)
    after the given starting moment.

    A gigasecond is 10^9 seconds, or 1,000,000,000 seconds.
    This function adds that duration to the input datetime and returns the resulting datetime.

    Args:
        moment (datetime): A datetime object representing the starting point in time.

    Returns:
        datetime: A new datetime object exactly one gigasecond later.
    """
    gigasecond = timedelta(seconds=1_000_000_000)  # Define the gigasecond interval
    new_moment = moment + gigasecond               # Add interval to original datetime
    return new_moment
