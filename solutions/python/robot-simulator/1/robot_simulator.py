# Globals for the directions
NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'

# Order of directions for turning
DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x = x_pos
        self.y = y_pos

    @property
    def coordinates(self):
        return (self.x, self.y)

    def turn_right(self):
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index + 1) % 4]

    def turn_left(self):
        current_index = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(current_index - 1) % 4]

    def advance(self):
        if self.direction == NORTH:
            self.y += 1
        elif self.direction == EAST:
            self.x += 1
        elif self.direction == SOUTH:
            self.y -= 1
        elif self.direction == WEST:
            self.x -= 1

    def move(self, instructions):
        for command in instructions:
            if command == 'R':
                self.turn_right()
            elif command == 'L':
                self.turn_left()
            elif command == 'A':
                self.advance()
