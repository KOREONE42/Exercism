import random
import string

class Robot:
    """
    Represents a robot with a unique, randomly generated name.

    The name format consists of two uppercase letters followed by three digits (e.g., 'RX837').
    Each name is guaranteed to be unique across all instances, including those that have been reset.
    """

    # Set to store all previously used names to ensure uniqueness
    _used_names = set()

    def __init__(self):
        """
        Initializes the robot without a name.
        A name will be assigned when the `name` property is accessed.
        """
        self._name = None

    def _generate_name(self) -> str:
        """
        Generates a unique robot name in the format 'AA000'–'ZZ999'.

        Returns:
            str: A unique name not used by any other robot.
        """
        while True:
            name = (
                ''.join(random.choices(string.ascii_uppercase, k=2)) +
                ''.join(random.choices(string.digits, k=3))
            )
            if name not in Robot._used_names:
                Robot._used_names.add(name)
                return name

    @property
    def name(self) -> str:
        """
        Gets the robot's name, generating one if necessary.

        Returns:
            str: The robot's unique name.
        """
        if self._name is None:
            self._name = self._generate_name()
        return self._name

    def reset(self) -> None:
        """
        Resets the robot's name to factory settings.

        The old name is not reused. A new unique name will be generated on next access.
        """
        if self._name:
            self._name = None
