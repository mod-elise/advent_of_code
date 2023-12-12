import time

class Pointer:
    def __init__(self, x, y, pipes, direction):
        self.x = x
        self.y = y
        self.symbol = pipes[y][x]
        self.direction = direction
        self.complete = False
        self.loop = False
        self.path = [self.symbol]

        while not self.complete:
            self.calc_symbol()
            if self.symbol == 'S':
                self.loop = True

            self.move()
        self.path.pop(0)
        self.path.pop(len(self.path) - 1)


    def calc_symbol(self):
        self.symbol = pipes[self.y][self.x]
        self.path.append(self.symbol)

    def move(self):
        if self.direction == 'north':
            if self.symbol == '|' and self.y > 0:
                self.y -= 1
            elif self.symbol == '7' and self.x > 0:
                self.x -= 1
                self.direction = 'west'
            elif self.symbol == 'F' and self.y < len(pipes) - 1:
                self.direction = 'east'
                self.x += 1
            else:
                self.complete = True
        elif self.direction == 'east':
            if self.symbol == '-' and self.x < len(pipes[0]) - 1:
                self.x += 1
            elif self.symbol == '7' and self.y < len(pipes) - 1:
                self.y += 1
                self.direction = 'south'
            elif self.symbol == 'J' and self.y > 0:
                self.direction = 'north'
                self.y -= 1
            else:
                self.complete = True
        elif self.direction == 'south':
            if self.symbol == '|' and self.y < len(pipes) - 1:
                self.y += 1
            elif self.symbol == 'L' and self.x < len(pipes[0]) - 1:
                self.direction = 'east'
                self.x += 1
            elif self.symbol == 'J' and self.x > 0:
                self.direction = 'west'
                self.x -= 1
            else:
                self.complete = True
        elif self.direction == 'west':
            if self.symbol == '-' and self.x > 0:
                self.x -= 1
            elif self.symbol == 'L' and self.y > 0:
                self.direction = 'north'
                self.y -= 1
            elif self.symbol == 'F' and self.y < len(pipes) - 1:
                self.direction = 'south'
                self.y += 1
            else:
                self.complete = True
        else:
            self.calc_symbol()
            self.complete = True
            if self.symbol == 'S':
                self.loop = True

def get_adjacent (start):
    #north east south west
    if start[1] > 0:
        north = [start[0], start[1]-1]
    else:
        north = None
    if start[0] < len(pipes[0]) - 1:
        east = [start[0]+1, start[1]]
    else:
        east = None
    if start[1] < len(pipes) - 1:
        south = [start[0], start[1]+1]
    else:
        south = None
    if start[0] > 0:
        west = [start[0]-1, start[1]]
    else:
        west = None
    adjacent_spaces = {
        'north': north,
        'east': east,
        'south': south,
        'west': west
    }
    return adjacent_spaces

start_time = time.time()
f = open("input.txt", "r")
pipes = f.readlines()

for i,pipe_line in enumerate(pipes):
    if 'S' in pipe_line:
        start = [pipe_line.index('S'), i]

pointers = []
adjacent_to_start = get_adjacent(start)
for direction, coordinates in adjacent_to_start.items():
    if coordinates is not None:
        pointers.append(Pointer(coordinates[0], coordinates[1], pipes, direction))

for pointer in pointers:
    if pointer.loop:
        print ((len(pointer.path)//2) + (len(pointer.path) % 2))
        break

print (f'{time.time() - start_time} seconds')
