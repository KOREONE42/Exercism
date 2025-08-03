def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # The number of grains on a given square is 2^(number-1)
    return 2 ** (number - 1)

def total():
    # The total number of grains on the chessboard
    # This is the sum of a geometric series: 1, 2, 4, ..., 2^(64-1)
    # The formula for the sum of the first n terms of a geometric series is:
    # S_n = a * (1 - r^n) / (1 - r) where a is the first term, r is the common ratio, and n is the number of terms
    return (2 ** 64) - 1  # 2^64 - 1 gives the total number of grains on the chessboard