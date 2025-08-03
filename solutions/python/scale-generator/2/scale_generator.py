class Scale:
    """
    Represents a musical scale starting from a given tonic (root note).
    
    Supports:
    - Chromatic scale generation (12-tone)
    - Interval-based scale generation (e.g. major, minor, modes)
    
    Automatically selects between sharp and flat notation based on the tonic.
    """

    # Chromatic scales written with sharps or flats
    SHARP_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    FLAT_NOTES  = ["A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab"]

    # Tonics that traditionally use sharps or flats
    SHARP_KEYS = ["C", "G", "D", "A", "E", "B", "F#", "e", "b", "f#", "c#", "g#", "d#"]
    FLAT_KEYS  = ["F", "Bb", "Eb", "Ab", "Db", "Gb", "d", "g", "c", "f", "bb", "eb"]

    # Mapping of interval types to steps in the chromatic scale
    INTERVAL_MAP = {
        "m": 1,  # minor second (half step)
        "M": 2,  # major second (whole step)
        "A": 3   # augmented second (step and a half)
    }

    def __init__(self, tonic):
        """
        Initializes the Scale with a tonic (starting note).
        
        Args:
            tonic (str): The tonic note (case-insensitive), e.g., 'C', 'g#', 'Eb'.
        """
        # Normalize tonic to standard format: first letter uppercase, rest lowercase
        self.tonic = tonic[0].upper() + tonic[1:].lower()

        # Choose appropriate chromatic scale based on the tonic
        if tonic in self.FLAT_KEYS:
            self.notes = self.FLAT_NOTES
        else:
            self.notes = self.SHARP_NOTES

    def chromatic(self):
        """
        Generates the 12-note chromatic scale starting from the tonic.
        
        Returns:
            list of str: Chromatic scale beginning with the tonic.
        """
        # Find tonic index in selected chromatic set
        start_index = self.notes.index(self.tonic)
        # Rotate the scale to begin at the tonic
        return self.notes[start_index:] + self.notes[:start_index]

    def interval(self, pattern):
        """
        Generates a scale based on a pattern of intervals.
        
        Args:
            pattern (str): A string of interval codes, e.g., "MMmMMMm".
                - 'm' = half step (minor second)
                - 'M' = whole step (major second)
                - 'A' = step and a half (augmented second)

        Returns:
            list of str: Notes in the scale, starting from the tonic and
                         following the specified interval pattern.
        """
        # Begin with the tonic
        scale = [self.tonic]
        # Use rotated chromatic scale for reference
        chromatic_scale = self.chromatic()
        current_index = 0

        # Traverse the pattern and add notes by stepping through intervals
        for step in pattern:
            current_index = (current_index + self.INTERVAL_MAP[step]) % 12
            scale.append(chromatic_scale[current_index])

        return scale
