def saddle_points(matrix):
    """
    Identifies all saddle points in a matrix.

    A saddle point is defined as an element in the matrix that is:
    - The largest in its row (east-west direction)
    - The smallest in its column (north-south direction)

    Args:
        matrix (list of list of int): A rectangular matrix representing tree heights.

    Returns:
        list of dict: A list of dictionaries, each representing the coordinates of a saddle point
                      with keys 'row' and 'column'. Rows and columns are 1-indexed.

    Raises:
        ValueError: If the matrix is irregular (rows have differing lengths).
    """

    # Return empty list for an empty matrix
    if not matrix:
        return []

    # Check matrix regularity (all rows must have the same number of columns)
    num_cols = len(matrix[0])
    for row in matrix:
        if len(row) != num_cols:
            raise ValueError("irregular matrix")

    saddle_points = []

    # Loop through each row to find row max candidates
    for i, row in enumerate(matrix):
        max_in_row = max(row)

        # Loop through each column in the current row
        for j, value in enumerate(row):
            # Check if value is the maximum in its row
            if value == max_in_row:
                # Extract the entire column j
                column = [matrix[r][j] for r in range(len(matrix))]
                min_in_col = min(column)

                # Check if value is the minimum in its column
                if value == min_in_col:
                    # Append the saddle point (1-indexed)
                    saddle_points.append({"row": i + 1, "column": j + 1})

    return saddle_points