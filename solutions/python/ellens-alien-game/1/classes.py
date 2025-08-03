"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class) total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """

    total_aliens_created = 0  # Class attribute to track all alien instances

    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1  # Increment on each instantiation

    def hit(self):
        """Decrement health by 1 (minimum of 0)."""
        if self.health > 0:
            self.health -= 1

    def is_alive(self):
        """Return True if the alien's health is above 0."""
        return self.health > 0

    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Update coordinates to new location."""
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(self, other_object):
        """Placeholder for future collision detection logic."""
        pass


def new_aliens_collection(coordinate_list):
    """Creates a list of Alien objects from a list of (x, y) coordinate tuples."""
    return [Alien(x, y) for x, y in coordinate_list]
