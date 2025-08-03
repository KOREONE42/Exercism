def rectangles(strings):
    # Check trivial cases when input is empty or blank rows.
    if not strings or not strings[0]:
        return 0

    rows = len(strings)
    cols = len(strings[0])
    count = 0

    # Helper functions to validate edges.
    def valid_horizontal(row, start, end):
        # Check the segment between start and end along a horizontal line.
        # The segment (excluding the corners) must only contain '-' or '+'.
        for col in range(start + 1, end):
            if strings[row][col] not in "-+":
                return False
        return True

    def valid_vertical(col, start, end):
        # Check the segment between start and end along a vertical column.
        # The segment (excluding the corners) must only contain '|' or '+'.
        for row in range(start + 1, end):
            if strings[row][col] not in "|+":
                return False
        return True

    # Iterate over all pairs of potential rectangle corners.
    for r1 in range(rows):
        for c1 in range(cols):
            # Top left corner must be '+'
            if strings[r1][c1] != '+':
                continue
            for r2 in range(r1 + 1, rows):
                for c2 in range(c1 + 1, cols):
                    # The potential rectangle's top-right, bottom-left, and bottom-right must also be '+'
                    if strings[r1][c2] != '+' or strings[r2][c1] != '+' or strings[r2][c2] != '+':
                        continue
                    # Now, check the horizontal edges (r1, c1 to c1->c2) and (r2, c1 to c2)
                    if not valid_horizontal(r1, c1, c2):
                        continue
                    if not valid_horizontal(r2, c1, c2):
                        continue
                    # Check the vertical edges (c1, r1 to r2) and (c2, r1 to r2)
                    if not valid_vertical(c1, r1, r2):
                        continue
                    if not valid_vertical(c2, r1, r2):
                        continue
                    # If all edges are valid, we have a complete rectangle.
                    count += 1

    return count
