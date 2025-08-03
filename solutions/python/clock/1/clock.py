class Clock:
    def __init__(self, hour, minute):
        total_minutes = (hour * 60 + minute) % (24 * 60)
        self.hour = total_minutes // 60
        self.minute = total_minutes % 60

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return (self.hour, self.minute) == (other.hour, other.minute)
        return False

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
