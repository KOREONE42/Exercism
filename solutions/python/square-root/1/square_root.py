def square_root(number):
    if number == 1:
        return 1
    
    low = 1
    high = number

    while low <= high:
        mid = (low + high) // 2
        squared = mid * mid

        if squared == number:
            return mid
        elif squared < number:
            low = mid + 1
        else:
            high = mid - 1

    # Shouldn't reach here for perfect squares
    return None
