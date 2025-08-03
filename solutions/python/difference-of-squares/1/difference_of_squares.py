def square_of_sum(number):
    # Calculate the sum of the first 'number' natural numbers
    sum_of_numbers = (number * (number + 1)) // 2
    # Return the square of this sum
    return sum_of_numbers ** 2

def sum_of_squares(number):
    # Calculate the sum of the squares of the first 'number' natural numbers
    return (number * (number + 1) * (2 * number + 1)) // 6

def difference_of_squares(number):
    # Calculate the difference between the square of the sum and the sum of the squares
    return square_of_sum(number) - sum_of_squares(number)
