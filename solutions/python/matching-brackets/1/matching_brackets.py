def is_paired(input_string):
    """
    Check if all brackets in the input string are balanced and properly nested.

    The function supports the following brackets: (), {}, and [].
    Any other characters in the string are ignored.

    Parameters:
    -----------
    input_string : str
        The string to be checked for balanced brackets.

    Returns:
    --------
    bool
        True if the string has balanced brackets, False otherwise.
    """
    stack = []  # Stack to keep track of opening brackets
    opening = {'(': ')', '{': '}', '[': ']'}  # Mapping of opening brackets to their corresponding closing ones
    closing = {')': '(', '}': '{', ']': '['}  # Mapping of closing brackets to their corresponding opening ones

    for char in input_string:
        if char in opening:
            # Push opening bracket onto the stack
            stack.append(char)
        elif char in closing:
            # If stack is empty or top doesn't match, brackets are unbalanced
            if not stack or stack[-1] != closing[char]:
                return False
            # Pop the matched opening bracket
            stack.pop()

    # If stack is empty, all brackets were matched correctly
    return not stack
