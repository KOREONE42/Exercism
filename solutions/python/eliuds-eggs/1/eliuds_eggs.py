def egg_count(display_value):
    count = 0
    while display_value > 0:
        display_value, remainder = divmod(display_value, 2)
        if remainder == 1:
            count += 1
    return count
