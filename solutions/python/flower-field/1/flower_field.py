def annotate(garden):
    """
    Given a rectangular garden represented as a list of strings containing
    spaces (' ') and flowers ('*'), return a new garden where each empty cell
    is replaced by the count of adjacent flowers (orthogonal + diagonal).
    Cells with zero adjacent flowers remain as spaces.
    """

    # Handle the empty garden case
    if not garden:
        return []

    # Validate rectangular shape and allowed characters
    width = len(garden[0])
    for row in garden:
        if len(row) != width:
            raise ValueError("The board is invalid with current input.")
        for ch in row:
            if ch not in (" ", "*"):
                raise ValueError("The board is invalid with current input.")

    # If there are zero columns (e.g., ["", "", ...]), return as-is
    if width == 0:
        return garden[:]

    rows = len(garden)
    # Work with a mutable grid
    grid = [list(r) for r in garden]

    # Directions for the 8 neighbors
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
    ]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < width

    # Compute counts for empty cells
    for r in range(rows):
        for c in range(width):
            if grid[r][c] == "*":
                continue
            count = 0
            for dr, dc in neighbors:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc) and grid[nr][nc] == "*":
                    count += 1
            if count > 0:
                grid[r][c] = str(count)
            # else leave as space

    return ["".join(row) for row in grid]
