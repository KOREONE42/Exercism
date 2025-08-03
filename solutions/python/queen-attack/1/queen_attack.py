class Queen:
    """
    Represents a Queen on a chessboard with a specific row and column position.

    A Queen can attack any piece that is on the same row, column, or diagonal.
    """

    def __init__(self, row, column):
        """
        Initialize a Queen with a given row and column.

        Args:
            row (int): The row position (0-7).
            column (int): The column position (0-7).

        Raises:
            ValueError: If row or column is outside the valid 0-7 range.
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
        Determine whether this Queen can attack another Queen.

        Queens can attack if they share the same row, column, or diagonal.

        Args:
            another_queen (Queen): Another Queen object.

        Returns:
            bool: True if this Queen can attack the other, False otherwise.

        Raises:
            ValueError: If both queens are at the same position.
        """
        # If both queens are in the same square, raise an error
        if self.row == another_queen.row and self.column == another_queen.column:
            raise ValueError("Invalid queen position: both queens in the same square")

        # Check if queens are on the same row or same column
        if self.row == another_queen.row or self.column == another_queen.column:
            return True

        # Check if queens are on the same diagonal
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True

        # Otherwise, the queens cannot attack each other
        return False
