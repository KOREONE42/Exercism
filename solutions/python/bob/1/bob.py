def response(hey_bob):
    # Strip whitespace from the input
    stripped_input = hey_bob.strip()
    
    # Check if the input is silence
    if stripped_input == "":
        return "Fine. Be that way!"
    
    # Check if the input is in all capital letters
    if stripped_input.isupper():
        # Check if it is a question
        if stripped_input.endswith('?'):
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    
    # Check if the input is a question
    if stripped_input.endswith('?'):
        return "Sure."
    
    # Default response
    return "Whatever."