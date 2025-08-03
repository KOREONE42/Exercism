def steps(number):
    # Validate the input
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    count = 0
    
    # Apply Collatz Conjecture rules
    while number != 1:
        if number % 2 == 0:  # Even number
            number //= 2
        else:  # Odd number
            number = number * 3 + 1
        count += 1

    return count