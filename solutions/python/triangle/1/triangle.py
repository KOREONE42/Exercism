def is_valid_triangle(sides):
    # Check if any side is <= 0, which would invalidate the triangle
    if any(side <= 0 for side in sides):
        return False
    # Check if the triangle inequality holds
    a, b, c = sorted(sides)
    return a + b >= c and b + c >= a and a + c >= b

def equilateral(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) == 1
    return False

def isosceles(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) <= 2
    return False

def scalene(sides):
    if is_valid_triangle(sides):
        return len(set(sides)) == 3
    return False
