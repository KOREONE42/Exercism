def spiral_matrix(size):
    """
    Generates a square matrix filled with natural numbers in a clockwise spiral pattern.

    Parameters:
    size (int): The size of the square matrix (number of rows and columns).

    Returns:
    list[list[int]]: A 2D list representing the spiral matrix.
    
    Example:
    spiral_matrix(3) returns:
    [
        [1, 2, 3],
        [8, 9, 4],
        [7, 6, 5]
    ]
    """
    # Initialize an empty matrix filled with zeros
    matrix = [[0] * size for _ in range(size)]

    # Start the number sequence from 1
    num = 1

    # Define the current boundaries of the spiral
    left, right = 0, size - 1
    top, bottom = 0, size - 1

    # Loop until the boundaries collapse inward
    while left <= right and top <= bottom:
        # Fill the top row from left to right
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1  # Move the top boundary down

        # Fill the right column from top to bottom
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1  # Move the right boundary left

        # Fill the bottom row from right to left
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1
        bottom -= 1  # Move the bottom boundary up

        # Fill the left column from bottom to top
        for row in range(bottom, top - 1, -1):
            matrix[row][left] = num
            num += 1
        left += 1  # Move the left boundary right

    return matrix
