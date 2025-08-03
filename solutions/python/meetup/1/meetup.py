from datetime import date
import calendar

# Custom exception for when the meetup day is not available.
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.
    
    message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def meetup(year, month, week, day_of_week):
    # Mapping day names to Python's weekday numbers (Monday is 0, Sunday is 6)
    weekday_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    
    if day_of_week not in weekday_mapping:
        raise MeetupDayException("Invalid day of week.")
    
    target_weekday = weekday_mapping[day_of_week]
    # Get number of days in the month
    days_in_month = calendar.monthrange(year, month)[1]
    
    # For "teenth": examine the days 13th to 19th
    if week == "teenth":
        for day in range(13, 20):
            d = date(year, month, day)
            if d.weekday() == target_weekday:
                return d
        # This block should never be reached given the problem guarantees,
        # but we include it for completeness.
        raise MeetupDayException("That day does not exist.")
    
    # Gather all dates in the month that match the target weekday.
    matching_days = [
        date(year, month, day)
        for day in range(1, days_in_month + 1)
        if date(year, month, day).weekday() == target_weekday
    ]
    
    if week == "first":
        if len(matching_days) >= 1:
            return matching_days[0]
    elif week == "second":
        if len(matching_days) >= 2:
            return matching_days[1]
    elif week == "third":
        if len(matching_days) >= 3:
            return matching_days[2]
    elif week == "fourth":
        if len(matching_days) >= 4:
            return matching_days[3]
    elif week == "fifth":
        if len(matching_days) >= 5:
            return matching_days[4]
        else:
            raise MeetupDayException("That day does not exist.")
    elif week == "last":
        return matching_days[-1]
    
    # If the provided week string does not match any of the above cases:
    raise MeetupDayException("Invalid week descriptor.")
