def rows(row_count):
    if row_count < 0:
        raise ValueError("number of rows is negative")
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]
    
    # Recursively generate the triangle with one row less.
    previous_triangle = rows(row_count - 1)
    last_row = previous_triangle[-1]
    
    # A helper function that recursively computes the inner values 
    # for the new row based on the last row.
    def compute_inner(index):
        # When there are no more adjacent pairs, end recursion.
        if index >= len(last_row) - 1:
            return []
        # Sum the current pair and continue recursively.
        return [last_row[index] + last_row[index + 1]] + compute_inner(index + 1)
    
    # Construct the new row by placing 1 on each end and the computed inner values in between.
    new_row = [1] + compute_inner(0) + [1]
    
    return previous_triangle + [new_row]
