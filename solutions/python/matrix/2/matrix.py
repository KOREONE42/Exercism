from typing import List

class Matrix:
    """
    A Matrix class that represents a grid of integers parsed from a string.

    The input string is expected to have rows separated by newline characters,
    with each integer separated by whitespace. This class provides methods
    for retrieving individual rows and columns (using 1-indexing) and for
    retrieving the full list of rows or columns.
    """

    def __init__(self, matrix_string: str) -> None:
        """
        Initialize the Matrix object by parsing a string representation.

        Each line in the input string is split into numbers, which are then
        converted into integers and stored as a list of lists.

        Args:
            matrix_string (str): The string representation of the matrix. 
                                   Each row is separated by a newline and 
                                   each number within a row is separated by spaces.

        Raises:
            ValueError: If not all rows contain the same number of elements.
        """
        # Split the matrix string by lines and convert each number to an integer.
        rows: List[List[int]] = [
            [int(num) for num in line.split()]
            for line in matrix_string.strip().splitlines() if line.strip()
        ]

        # Verify that all rows have the same number of columns.
        if rows:
            expected_columns = len(rows[0])
            for row in rows:
                if len(row) != expected_columns:
                    raise ValueError("Inconsistent number of columns found in rows.")
        
        self._rows: List[List[int]] = rows  # Store the matrix data.

    def row(self, index: int) -> List[int]:
        """
        Retrieve a row from the matrix by its 1-indexed position.

        Args:
            index (int): The 1-indexed row number to retrieve.

        Returns:
            List[int]: The row corresponding to the given index.

        Raises:
            IndexError: If the index is less than 1 or exceeds the number of rows.
        """
        # Check that the requested row index is within valid bounds.
        if index < 1 or index > len(self._rows):
            raise IndexError("Row index out of range.")
        return self._rows[index - 1]

    def column(self, index: int) -> List[int]:
        """
        Retrieve a column from the matrix by its 1-indexed position.

        Args:
            index (int): The 1-indexed column number to retrieve.

        Returns:
            List[int]: The column corresponding to the given index.

        Raises:
            IndexError: If the index is less than 1 or exceeds the number of columns.
        """
        # Ensure there is at least one row and validate the column index.
        if not self._rows or index < 1 or index > len(self._rows[0]):
            raise IndexError("Column index out of range.")
        # Build the column by picking the (index - 1)th element from each row.
        return [row[index - 1] for row in self._rows]

    def get_all_rows(self) -> List[List[int]]:
        """
        Retrieve a copy of all rows in the matrix.

        Returns:
            List[List[int]]: A list of rows, where each row is a list of integers.
        """
        # Return a shallow copy for safety against external modification.
        return [row.copy() for row in self._rows]

    def get_all_columns(self) -> List[List[int]]:
        """
        Retrieve all columns of the matrix as a list of lists.

        Returns:
            List[List[int]]: A list of columns, where each column is a list of integers.
        """
        if not self._rows:
            return []
        num_cols = len(self._rows[0])
        # Construct the list of columns using a nested list comprehension.
        return [[row[i] for row in self._rows] for i in range(num_cols)]
