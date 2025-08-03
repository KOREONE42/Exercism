class Matrix:
    """
    A class used to represent a Matrix parsed from a string.

    Attributes:
        _rows (list[list[int]]): A list of rows, where each row is a list of integers.
    """

    def __init__(self, matrix_string):
        """
        Constructs the necessary attributes for the Matrix object.

        The matrix is provided as a multi-line string with numbers separated by spaces.
        This method splits the string into rows and converts each element to an integer.

        Args:
            matrix_string (str): The string representation of the matrix.
        """
        # Remove any leading/trailing whitespace and split the string into individual lines.
        # Each line is split into tokens based on whitespace, and each token is converted to an integer.
        self._rows = [
            [int(num) for num in line.split()] 
            for line in matrix_string.strip().splitlines()
        ]

    def row(self, index):
        """
        Retrieves a row from the matrix at the given 1-indexed position.

        Args:
            index (int): The 1-indexed position of the row to retrieve.

        Returns:
            list[int]: The row at the specified position.
            
        Example:
            For index=1, returns the first row.
        """
        # Adjust for Python's 0-indexed lists: subtract 1 from the 1-indexed input.
        return self._rows[index - 1]

    def column(self, index):
        """
        Retrieves a column from the matrix at the given 1-indexed position.

        Iterates over every row in the matrix and collects the element at the specified column index.

        Args:
            index (int): The 1-indexed position of the column to retrieve.

        Returns:
            list[int]: The column at the specified position.
            
        Example:
            For index=1, returns the first column.
        """
        # Adjust for Python's 0-indexed lists: subtract 1 from the 1-indexed input.
        return [row[index - 1] for row in self._rows]
