# Define the list of color codes
COLOR_CODES = ["black", "brown", "red", "orange", "yellow", 
               "green", "blue", "violet", "grey", "white"]

def color_code(color):
    return COLOR_CODES.index(color)

def colors():
    return COLOR_CODES

# Let's test both functions with a few examples
test_color = "green"
code_for_green = color_code(test_color)
all_colors = colors()

code_for_green, all_colors
