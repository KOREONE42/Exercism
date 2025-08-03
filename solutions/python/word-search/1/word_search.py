class Point:
    def __init__(self, x, y):
        # Initialize point with x (column) and y (row) coordinates
        self.x = x
        self.y = y

    def __eq__(self, other):
        # Two points are equal if their coordinates match
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class WordSearch:
    def __init__(self, puzzle):
        """
        Initialize the word search with a puzzle grid.
        :param puzzle: A list of equal-length strings or a multiline string.
        """
        # Accept multiline string or list of strings
        if isinstance(puzzle, str):
            lines = puzzle.splitlines()
        else:
            lines = puzzle

        # Create 2D grid of characters
        self.grid = [list(line) for line in lines]
        self.height = len(self.grid)
        self.width = len(self.grid[0]) if self.height > 0 else 0

    def search(self, word):
        """
        Search for a word in the puzzle.
        Returns a tuple of Points for the start and end of the word if found,
        or None otherwise.
        Supports horizontal, vertical, and diagonal in all 8 directions.
        :param word: The word to search for (string).
        :return: (Point(start_x, start_y), Point(end_x, end_y)) or None
        """
        length = len(word)
        # All 8 possible directions: (dx, dy)
        directions = [
            (dx, dy)
            for dx in (-1, 0, 1)
            for dy in (-1, 0, 1)
            if not (dx == 0 and dy == 0)
        ]

        for y in range(self.height):
            for x in range(self.width):
                # Check if first letter matches
                if self.grid[y][x] != word[0]:
                    continue

                # Try each direction
                for dx, dy in directions:
                    end_x = x + (length - 1) * dx
                    end_y = y + (length - 1) * dy

                    # Check if end is within bounds
                    if 0 <= end_x < self.width and 0 <= end_y < self.height:
                        # Check all intermediate letters
                        for i in range(1, length):
                            nx = x + i * dx
                            ny = y + i * dy
                            if self.grid[ny][nx] != word[i]:
                                break
                        else:
                            # All letters matched
                            start = Point(x, y)
                            end = Point(end_x, end_y)
                            return (start, end)
        return None
