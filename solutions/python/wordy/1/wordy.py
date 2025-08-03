def answer(question):
    """
    Evaluate a simple math word problem expressed in English and return the result as an integer.

    Supports:
    - Basic arithmetic operations: addition, subtraction, multiplication, division
    - Left-to-right evaluation (ignores operator precedence)
    - Error handling for unknown operations or malformed questions

    Parameters:
    - question (str): A word-based math problem ending in a question mark.

    Returns:
    - int: Result of the evaluated expression

    Raises:
    - ValueError: If the operation is unknown or the syntax is malformed
    """
    if not question.startswith("What is ") or not question.endswith("?"):
        raise ValueError("syntax error")

    # Remove "What is " prefix and "?" suffix
    question = question[8:-1].strip()

    if not question:
        raise ValueError("syntax error")

    # Replace English word operations with mathematical symbols
    replacements = {
        "plus": "+",
        "minus": "-",
        "multiplied by": "*",
        "divided by": "/"
    }

    # Replace the longest phrases first to avoid partial matches
    for phrase in sorted(replacements.keys(), key=lambda x: -len(x)):
        question = question.replace(phrase, replacements[phrase])

    # Split the question into tokens (numbers and operators)
    tokens = question.split()

    equation = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in "+-*/":
            # Append operator
            equation.append(token)
        else:
            # Attempt to parse and append number
            try:
                equation.append(int(token))
            except ValueError:
                raise ValueError("unknown operation")
        i += 1

    # Validate structure of equation
    if not isinstance(equation[0], int):
        raise ValueError("syntax error")
    if len(equation) == 1:
        return equation[0]
    if len(equation) < 3 or len(equation) % 2 == 0:
        raise ValueError("syntax error")

    # Evaluate equation from left to right
    result = equation[0]
    i = 1
    while i < len(equation):
        op = equation[i]
        next_val = equation[i+1]

        # Ensure that the next value is a valid number
        if not isinstance(next_val, int):
            raise ValueError("syntax error")

        # Perform the operation
        if op == '+':
            result += next_val
        elif op == '-':
            result -= next_val
        elif op == '*':
            result *= next_val
        elif op == '/':
            result = int(result / next_val)  # Ensure integer division
        else:
            raise ValueError("unknown operation")
        i += 2

    return result
