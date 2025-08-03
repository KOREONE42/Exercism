def transpose(text):
    lines = text.splitlines()
    if not lines:
        return ""
    max_len = max(len(line) for line in lines)
    transposed_rows = []
    for col_index in range(max_len):
        col_chars = []
        for line in lines:
            # If the column index is within the line, mark the character as "real"
            if col_index < len(line):
                col_chars.append((line[col_index], True))
            else:
                # Otherwise, use a space that is considered "padded"
                col_chars.append((' ', False))
        # Remove any trailing padded spaces (where flag is False)
        while col_chars and not col_chars[-1][1]:
            col_chars.pop()
        # Join just the characters, disregarding the flags
        transposed_rows.append("".join(char for char, _ in col_chars))
    return "\n".join(transposed_rows)
