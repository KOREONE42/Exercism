"""
This module provides a function 'rectangles' that counts the number of complete rectangles
in an ASCII diagram. A rectangle is defined as having four corners represented by '+', with
horizontal edges containing only '-' or '+' and vertical edges containing only '|' or '+'.
"""

def rectangles(strings):
    """
    Count the number of complete rectangles present in the ASCII diagram represented by the list of strings.

    Each rectangle must have its four corners marked with '+'. The top and bottom edges can only include '-'
    or '+' (besides the corner '+'), and the left and right edges can only include '|' or '+' (besides the corner '+').
    
    Parameters:
        strings (list of str): The list of strings representing rows in the ASCII diagram.

    Returns:
        int: The number of complete rectangles detected in the diagram.
    """
    # Check trivial cases: empty input or rows with no content.
    if not strings or not strings[0]:
        return 0

    rows = len(strings)
    cols = len(strings[0])
    count = 0

    def valid_horizontal(row, start, end):
        """
        Check if the horizontal segment in a given row between the two corner columns is valid.
        
        The segment (excluding the start and end corners) must contain only '-' or '+'.
        
        Parameters:
            row (int): The index of the row in which to check the horizontal segment.
            start (int): The starting column index (a corner).
            end (int): The ending column index (a corner).
        
        Returns:
            bool: True if the horizontal segment is valid, False otherwise.
        """
        for col in range(start + 1, end):
            if strings[row][col] not in "-+":
                return False
        return True

    def valid_vertical(col, start, end):
        """
        Check if the vertical segment in a given column between the two corner rows is valid.
        
        The segment (excluding the start and end corners) must contain only '|' or '+'.
        
        Parameters:
            col (int): The index of the column in which to check the vertical segment.
            start (int): The starting row index (a corner).
            end (int): The ending row index (a corner).
        
        Returns:
            bool: True if the vertical segment is valid, False otherwise.
        """
        for row in range(start + 1, end):
            if strings[row][col] not in "|+":
                return False
        return True

    # Iterate over all potential pairs of top-left and bottom-right corners.
    # We use nested loops to try every possible rectangle defined by two points:
    # (r1, c1) for the top-left and (r2, c2) for the bottom-right.
    for r1 in range(rows):
        for c1 in range(cols):
            # Ensure the top-left corner is a valid corner ('+')
            if strings[r1][c1] != '+':
                continue
            for r2 in range(r1 + 1, rows):
                for c2 in range(c1 + 1, cols):
                    # Verify that the other three corners are also '+'
                    if strings[r1][c2] != '+' or strings[r2][c1] != '+' or strings[r2][c2] != '+':
                        continue

                    # Validate the horizontal edges (top and bottom)
                    if not valid_horizontal(r1, c1, c2):
                        continue
                    if not valid_horizontal(r2, c1, c2):
                        continue

                    # Validate the vertical edges (left and right)
                    if not valid_vertical(c1, r1, r2):
                        continue
                    if not valid_vertical(c2, r1, r2):
                        continue

                    # If all edges are valid, count this rectangle.
                    count += 1

    return count
