def convert(input_grid):
    # Step 1: Validate input
    if len(input_grid) % 4 != 0:
        raise ValueError("Number of input lines is not a multiple of four")

    width = len(input_grid[0])
    if any(len(row) != width for row in input_grid):
        raise ValueError("Input lines are not all the same width")

    if width % 3 != 0:
        raise ValueError("Number of input columns is not a multiple of three")

    # Step 2: Digit pattern definitions
    DIGITS = {
        (
            " _ ",
            "| |",
            "|_|",
            "   "
        ): '0',
        (
            "   ",
            "  |",
            "  |",
            "   "
        ): '1',
        (
            " _ ",
            " _|",
            "|_ ",
            "   "
        ): '2',
        (
            " _ ",
            " _|",
            " _|",
            "   "
        ): '3',
        (
            "   ",
            "|_|",
            "  |",
            "   "
        ): '4',
        (
            " _ ",
            "|_ ",
            " _|",
            "   "
        ): '5',
        (
            " _ ",
            "|_ ",
            "|_|",
            "   "
        ): '6',
        (
            " _ ",
            "  |",
            "  |",
            "   "
        ): '7',
        (
            " _ ",
            "|_|",
            "|_|",
            "   "
        ): '8',
        (
            " _ ",
            "|_|",
            " _|",
            "   "
        ): '9'
    }

    # Step 3: Process the grid line by line
    num_lines = len(input_grid) // 4
    num_cols = len(input_grid[0]) // 3
    results = []

    for line_idx in range(num_lines):
        digits = []
        line_offset = line_idx * 4

        for col_idx in range(num_cols):
            col_offset = col_idx * 3
            pattern = tuple(
                input_grid[line_offset + r][col_offset:col_offset + 3]
                for r in range(4)
            )
            digits.append(DIGITS.get(pattern, '?'))
        
        results.append(''.join(digits))

    return ','.join(results)
