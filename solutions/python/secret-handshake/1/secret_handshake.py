def commands(binary_str):
    actions = []
    
    # Define binary values and corresponding actions
    if int(binary_str[-1]) == 1:  # Check if the rightmost bit is 1
        actions.append("wink")
    if int(binary_str[-2]) == 1:  # Check the second rightmost bit
        actions.append("double blink")
    if int(binary_str[-3]) == 1:  # Check the third rightmost bit
        actions.append("close your eyes")
    if int(binary_str[-4]) == 1:  # Check the fourth rightmost bit
        actions.append("jump")
    if int(binary_str[-5]) == 1:  # Check the fifth rightmost bit (reverse flag)
        actions.reverse()  # Reverse the order of actions if needed
    
    return actions
