class StackUnderflowError(Exception):
    """Exception raised when the stack does not have enough values to perform an operation."""
    def __init__(self, message="Insufficient number of items in stack"):
        self.message = message
        super().__init__(self.message)

import copy

def evaluate(input_data):
    """
    Evaluates a list of Forth-like commands.

    Args:
        input_data (list[str]): A list of strings, each representing a line of Forth code.

    Returns:
        list[int]: Final state of the stack.

    Raises:
        StackUnderflowError: If a stack operation is attempted with too few elements.
        ZeroDivisionError: If division by zero is attempted.
        ValueError: For undefined operations or malformed definitions.
    """
    stack = []
    user_words = {}
    MAX_RECURSION = 1000

    def is_number(token):
        try:
            int(token)
            return True
        except ValueError:
            return False

    def execute_token(token, depth=0):
        """Executes a single token (command or number)."""
        nonlocal stack

        if depth > MAX_RECURSION:
            raise RecursionError("maximum recursion depth exceeded")

        if is_number(token):
            stack.append(int(token))
        else:
            token = token.lower()

            if token in user_words:
                for inner_token in user_words[token]:
                    execute_token(inner_token, depth + 1)
            elif token == '+':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                stack.append(a + b)
            elif token == '-':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            elif token == '*':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                stack.append(a * b)
            elif token == '/':
                if len(stack) < 2:
                    raise StackUnderflowError()
                b, a = stack.pop(), stack.pop()
                if b == 0:
                    raise ZeroDivisionError("divide by zero")
                stack.append(a // b)
            elif token == 'dup':
                if not stack:
                    raise StackUnderflowError()
                stack.append(stack[-1])
            elif token == 'drop':
                if not stack:
                    raise StackUnderflowError()
                stack.pop()
            elif token == 'swap':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack[-1], stack[-2] = stack[-2], stack[-1]
            elif token == 'over':
                if len(stack) < 2:
                    raise StackUnderflowError()
                stack.append(stack[-2])
            else:
                raise ValueError("undefined operation")

    for line in input_data:
        tokens = line.split()
        if not tokens:
            continue

        idx = 0
        while idx < len(tokens):
            token = tokens[idx]

            if token.lower() == ':':
                if idx + 1 >= len(tokens):
                    raise ValueError("invalid definition: missing word name")
                word_name = tokens[idx + 1].lower()
                if is_number(word_name):
                    raise ValueError("illegal operation")

                definition = []
                idx += 2
                while idx < len(tokens) and tokens[idx].lower() != ';':
                    current_token = tokens[idx].lower()
                    if current_token in user_words:
                        # Expand definition at definition time
                        definition.extend(copy.deepcopy(user_words[current_token]))
                    else:
                        definition.append(current_token)
                    idx += 1

                if idx >= len(tokens) or tokens[idx].lower() != ';':
                    raise ValueError("invalid definition: missing ';'")

                user_words[word_name] = definition
            else:
                execute_token(token)

            idx += 1

    return stack
