def grep(pattern, flags, files):
    # Split the flags string into individual flags.
    flags_list = flags.split() if flags else []
    add_line_numbers = "-n" in flags_list
    list_files_only = "-l" in flags_list
    ignore_case = "-i" in flags_list
    invert_match = "-v" in flags_list
    exact_match = "-x" in flags_list

    # Prepare output collection.
    output_lines = []
    # Determine if we have to prefix matches with filename (when searching multiple files).
    multiple_files = len(files) > 1

    # Prepare the pattern for case-insensitive comparison if needed.
    comp_pattern = pattern.lower() if ignore_case else pattern

    for file in files:
        matched_in_file = False
        file_output = []
        with open(file, "r") as f:
            for line_number, line in enumerate(f, start=1):
                # Remove the trailing newline for comparison.
                line_stripped = line.rstrip("\n")
                if ignore_case:
                    comp_line = line_stripped.lower()
                else:
                    comp_line = line_stripped

                # Decide whether the line is a match.
                if exact_match:
                    match = (comp_line == comp_pattern)
                else:
                    match = (comp_pattern in comp_line)

                # Invert match if necessary.
                if invert_match:
                    match = not match

                # If the line meets the search criteria, handle it appropriately.
                if match:
                    if list_files_only:
                        matched_in_file = True
                        break  # No need to examine more lines for this file.
                    else:
                        prefix = ""
                        if multiple_files:
                            prefix += f"{file}:"
                        if add_line_numbers:
                            prefix += f"{line_number}:"
                        file_output.append(prefix + line)
        if list_files_only:
            if matched_in_file:
                output_lines.append(file + "\n")
        else:
            output_lines.extend(file_output)
    return "".join(output_lines)
