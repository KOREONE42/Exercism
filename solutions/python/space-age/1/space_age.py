class SpaceAge:
    """
    A class to calculate age on different planets in the Solar System
    given an age in seconds.

    Attributes:
        seconds (int): Age in seconds.
        earth_years (float): Age in Earth years, computed from seconds.

    Methods:
        on_<planet>(): Returns age on the given planet, rounded to two decimal places.
    """

    # Number of seconds in one Earth year
    EARTH_YEAR_SECONDS = 31557600

    # Orbital periods of planets in Earth years
    ORBITAL_PERIODS = {
        "mercury": 0.2408467,
        "venus": 0.61519726,
        "earth": 1.0,
        "mars": 1.8808158,
        "jupiter": 11.862615,
        "saturn": 29.447498,
        "uranus": 84.016846,
        "neptune": 164.79132,
    }

    def __init__(self, seconds):
        """
        Initialize the SpaceAge instance with seconds and compute Earth years.

        Args:
            seconds (int): The age in seconds.
        """
        self.seconds = seconds
        self.earth_years = seconds / self.EARTH_YEAR_SECONDS

    def on_mercury(self):
        """Return age in Mercury years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["mercury"], 2)

    def on_venus(self):
        """Return age in Venus years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["venus"], 2)

    def on_earth(self):
        """Return age in Earth years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["earth"], 2)

    def on_mars(self):
        """Return age in Mars years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["mars"], 2)

    def on_jupiter(self):
        """Return age in Jupiter years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["jupiter"], 2)

    def on_saturn(self):
        """Return age in Saturn years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["saturn"], 2)

    def on_uranus(self):
        """Return age in Uranus years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["uranus"], 2)

    def on_neptune(self):
        """Return age in Neptune years."""
        return round(self.earth_years / self.ORBITAL_PERIODS["neptune"], 2)
