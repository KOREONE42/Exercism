# Append: Adds all items from list2 to the end of list1.
def append(list1, list2):
    result = list1[:]
    for item in list2:
        result.append(item)
    return result

# Concatenate: Flattens a list of lists into a single list.
def concat(lists):
    result = []
    for lst in lists:
        for item in lst:
            result.append(item)
    return result

# Filter: Returns a list of items for which the predicate function returns True.
def filter(function, list):
    result = []
    for item in list:
        if function(item):
            result.append(item)
    return result

# Length: Returns the total number of items in the list.
def length(list):
    count = 0
    for item in list:
        count += 1
    return count

# Map: Applies the given function to each item in the list and returns a list of the results.
def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result

# Foldl: Reduces the list from left to right using the function and an initial accumulator.
def foldl(function, list, initial):
    accumulator = initial
    for item in list:
        accumulator = function(accumulator, item)
    return accumulator

# Foldr: Reduces the list from right to left using the function and an initial accumulator.
def foldr(function, list, initial):
    accumulator = initial
    for item in reversed(list):
        accumulator = function(accumulator, item)
    return accumulator

# Reverse: Returns a new list with the items in reverse order.
def reverse(list):
    result = []
    for item in list:
        result.insert(0, item)
    return result

