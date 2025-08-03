from itertools import permutations

# Define all possible values
colors = ['red', 'green', 'ivory', 'yellow', 'blue']
nationalities = ['Englishman', 'Spaniard', 'Ukrainian', 'Norwegian', 'Japanese']
drinks = ['coffee', 'tea', 'milk', 'orange juice', 'water']
pets = ['dog', 'snail', 'fox', 'horse', 'zebra']
hobbies = ['dancing', 'painter', 'reading', 'football', 'chess']

# Helper to get index of an item in a list
def index_of(value, seq):
    return seq.index(value)

def solve_zebra_puzzle():
    for color in permutations(colors):
        if abs(index_of('green', color) - index_of('ivory', color)) != 1 or index_of('green', color) < index_of('ivory', color):
            continue

        for nationality in permutations(nationalities):
            if nationality[0] != 'Norwegian':
                continue
            if color[index_of('Norwegian', nationality)] != 'blue' and abs(index_of('Norwegian', nationality) - index_of('blue', color)) != 1:
                continue
            if color[index_of('Englishman', nationality)] != 'red':
                continue

            for drink in permutations(drinks):
                if drink[2] != 'milk':
                    continue
                if drink[index_of('green', color)] != 'coffee':
                    continue
                if drink[index_of('Ukrainian', nationality)] != 'tea':
                    continue

                for pet in permutations(pets):
                    if pet[index_of('Spaniard', nationality)] != 'dog':
                        continue

                    for hobby in permutations(hobbies):
                        if hobby[index_of('snail', pet)] != 'dancing':
                            continue
                        if hobby[index_of('yellow', color)] != 'painter':
                            continue
                        if drink[index_of('football', hobby)] != 'orange juice':
                            continue
                        if hobby[index_of('Japanese', nationality)] != 'chess':
                            continue

                        # Check neighbors
                        fox_index = index_of('fox', pet)
                        reading_index = index_of('reading', hobby)
                        if abs(fox_index - reading_index) != 1:
                            continue

                        horse_index = index_of('horse', pet)
                        painter_index = index_of('painter', hobby)
                        if abs(horse_index - painter_index) != 1:
                            continue

                        # All constraints satisfied
                        return {
                            'water_drinker': nationality[index_of('water', drink)],
                            'zebra_owner': nationality[index_of('zebra', pet)]
                        }

    return None

def drinks_water():
    result = solve_zebra_puzzle()
    return result['water_drinker']

def owns_zebra():
    result = solve_zebra_puzzle()
    return result['zebra_owner']
