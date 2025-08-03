class Queen:
    """
    Represents a queen on a standard 8x8 chessboard.

    A queen can move any number of squares along a rank, file, or diagonal.
    """

    def __init__(self, row, column):
        """
        Initialize the Queen with a given position on the board.

        Args:
            row (int): The row index (0 to 7 inclusive).
            column (int): The column index (0 to 7 inclusive).

        Raises:
            ValueError: If the row or column is outside the board boundaries.
        """
        if row < 0:
            raise ValueError("row not positive")
        if row > 7:
            raise ValueError("row not on board")
        if column < 0:
            raise ValueError("column not positive")
        if column > 7:
            raise ValueError("column not on board")

        self.row = row
        self.column = column

    def can_attack(self, another_queen):
        """
        Determine whether this queen can attack another queen.

        Queens can attack if they are in the same row, same column, or on the same diagonal.

        Args:
            another_queen (Queen): The other queen to check against.

        Returns:
            bool: True if this queen can attack the other queen, False otherwise.

        Raises:
            ValueError: If both queens occupy the same square.
        """
        # Queens cannot occupy the same square
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Check for same row or column
        if self.row == another_queen.row or self.column == another_queen.column:
            return True

        # Check for diagonal attack (slope of 1 or -1)
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        # Otherwise, queens cannot attack each other
        return False
