def convert(number):
    result = ""
    
    # Check divisibility and append corresponding sounds
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    
    # If result is still an empty string, it means it is not divisible by 3, 5, or 7
    if result == "":
        return str(number)  # Convert number to string if no sounds are appended
    
    return result  # Return the concatenated string of sounds