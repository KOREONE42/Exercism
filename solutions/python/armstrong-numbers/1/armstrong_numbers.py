def is_armstrong_number(number):
    # Convert the number to a string to easily access each digit
    str_number = str(number)
    
    # Calculate the number of digits
    num_digits = len(str_number)
    
    # Calculate the Armstrong sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in str_number)
    
    # Return whether the calculated sum is equal to the original number
    return armstrong_sum == number