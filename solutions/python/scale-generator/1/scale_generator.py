class Scale:
    """
    A class to represent musical scales based on a given tonic (starting note).
    It supports generating chromatic and interval-based scales using sharps or flats
    according to music theory conventions.
    """

    # Chromatic scale using sharps
    SHARP_SCALE = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    # Chromatic scale using flats
    FLAT_SCALE  = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

    # Keys that typically use sharp notation
    SHARP_KEYS = ["C", "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", "g#", "d#"]
    # Keys that typically use flat notation
    FLAT_KEYS  = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]

    # Mapping of interval symbols to step values
    INTERVAL_STEPS = {
        "m": 1,  # minor second (half step)
        "M": 2,  # major second (whole step)
        "A": 3   # augmented second (whole + half step)
    }

    def __init__(self, tonic):
        """
        Initialize the scale with a tonic.
        
        Parameters:
        tonic (str): The starting note of the scale.
        """
        # Normalize the tonic (e.g., 'c#' → 'C#')
        self.tonic = tonic[0].upper() + tonic[1:].lower()
        
        # Select appropriate chromatic scale based on key signature
        if tonic in self.FLAT_KEYS:
            self.scale = self.FLAT_SCALE
        else:
            self.scale = self.SHARP_SCALE

    def chromatic(self):
        """
        Generate the 12-note chromatic scale starting from the tonic.
        
        Returns:
        list: The chromatic scale starting from the tonic, using sharps or flats.
        """
        # Find the index of the tonic in the selected scale
        start = self.scale.index(self.tonic)
        # Rotate the scale so it begins with the tonic
        return self.scale[start:] + self.scale[:start]

    def interval(self, intervals):
        """
        Generate a scale using a given sequence of intervals.
        
        Parameters:
        intervals (str): A string of interval symbols (e.g., 'MMmMMMm').
        
        Returns:
        list: The scale based on the given tonic and interval pattern.
        """
        # Start the scale with the tonic
        result = [self.tonic]
        # Get the rotated chromatic scale
        scale = self.chromatic()
        idx = 0  # current index in the chromatic scale

        # Build the scale by walking through the interval steps
        for i in intervals:
            # Move ahead by the number of steps defined for the interval
            idx = (idx + self.INTERVAL_STEPS[i]) % 12
            # Append the corresponding note to the result
            result.append(scale[idx])

        return result
