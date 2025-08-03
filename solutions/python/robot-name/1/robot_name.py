import random
import string

class Robot:
    """
    A class representing a factory robot with a unique, randomly-generated name.

    Each robot's name follows the pattern of two uppercase letters followed by three digits (e.g., "RX837").
    Robots retain their name unless reset. Names are guaranteed to be unique among all active and reset robots.
    """

    # Class-level set to track all used robot names and ensure uniqueness
    _used_names = set()

    def __init__(self):
        """
        Initialize a new Robot instance without a name.
        The name is generated lazily upon first access.
        """
        self._name = None

    def _generate_name(self):
        """
        Generate a unique random name in the format AA123.
        Retries until a unique name is found.
        """
        while True:
            # Generate two random uppercase letters
            letters = ''.join(random.choices(string.ascii_uppercase, k=2))
            # Generate three random digits
            digits = ''.join(random.choices(string.digits, k=3))
            name = letters + digits
            # Ensure name hasn't been used before
            if name not in Robot._used_names:
                Robot._used_names.add(name)
                return name

    @property
    def name(self):
        """
        Return the robot's name. Generate a new unique name if the robot has none.
        """
        if self._name is None:
            self._name = self._generate_name()
        return self._name

    def reset(self):
        """
        Reset the robot's name to factory settings.
        A new name will be generated the next time it's accessed.
        Note: the old name remains in the used names pool to maintain uniqueness.
        """
        if self._name:
            # Do not remove old name from _used_names to ensure global uniqueness
            self._name = None
