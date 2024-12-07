with open('input.txt') as f:
    labmapp = f.read()

def find_guard(lab_map, guard_symbols):
    return [key for key, value in lab_map.items() if value in guard_symbols][0]

def guard_facing(lab_map, guard_coord, guard_symbols):
    if lab_map[guard_coord] == guard_symbols[0]:
        return 'down'
    elif lab_map[guard_coord] == guard_symbols[1]:
        return 'up'
    elif lab_map[guard_coord] == guard_symbols[2]:
        return 'left'
    elif lab_map[guard_coord] == guard_symbols[3]:
        return 'right'

def isObstacleAhead(lab_map, guard_coord, guard_facing):
    if guard_facing == 'up':
        try:
            new_coord = tuple([guard_coord[0]-1, guard_coord[1]])
            if lab_map[new_coord] == '#':
                return True, True
            else:
                return False, True
        except:
            return False, False
    elif guard_facing == 'down':
        try:
            new_coord = tuple([guard_coord[0]+1, guard_coord[1]])
            if lab_map[new_coord] == '#':
                return True, True
            else:
                return False, True
        except:
            return False, False
    elif guard_facing == 'left':
        try:
            new_coord = tuple([guard_coord[0], guard_coord[1]-1])
            if lab_map[new_coord] == '#':
                return True, True
            else:
                return False, True
        except:
            return False, False
    elif guard_facing == 'right':
        try:
            new_coord = tuple([guard_coord[0], guard_coord[1]+1])
            if lab_map[new_coord] == '#':
                return True, True
            else:
                return False, True
        except:
            return False, False


    exit ("Obstacle detection error")


def moveGuard(guard_coord, guard_facing):
    if guard_facing == 'up':
        return [guard_coord[0]-1, guard_coord[1]]
    elif guard_facing == 'down':
        return [guard_coord[0]+1, guard_coord[1]]
    elif guard_facing == 'left':
        return [guard_coord[0], guard_coord[1]-1]
    elif guard_facing == 'right':
        return [guard_coord[0], guard_coord[1]+1]

def turnGuard(guard_facing):
    if guard_facing == 'up':
        return "right"
    elif guard_facing == 'down':
        return "left"
    elif guard_facing == 'left':
        return "up"
    elif guard_facing == 'right':
        return "down"

def drawPath(lab_map, full_path, guard_loop, counter):
    for square in full_path:
        if square == guard_loop:
            lab_map[square] = '∞'
        if square != guard_start:
            if full_path[(square[0], square[1])] == 'up' or full_path[(square[0], square[1])] == 'down':
                lab_map[square] = '|'
            elif full_path[(square[0], square[1])] == 'left' or full_path[(square[0], square[1])] == 'right':
                lab_map[square] = '-'
  # Determine grid bounds

        # Determine grid bounds
    max_y = max(coord[0] for coord in lab_map)
    max_x = max(coord[1] for coord in lab_map)

    # Build the grid as a list of strings
    grid = []
    for y in range(max_y + 1):  # Iterate over rows
        row = []
        for x in range(max_x + 1):  # Iterate over columns
            value = lab_map.get((y, x), '.')  # Access using (y, x)
            row.append(str(value))
        grid.append("".join(row))

    # write grid to file
    # print (str(counter))
    with open("loopmap" + str(counter) + ".txt" , "w") as f:
        f.write("\n".join(grid))

def countGuardSteps(lab_map, guard_coord, guard_facing):
    squaresVisited = set()
    full_path = {guard_coord: guard_facing}

    squaresVisited.add(guard_coord)
    isObstacle, continueProgram = isObstacleAhead(lab_map, guard_coord, guard_facing)
    counter = 0
    while continueProgram:
        counter += 1
        if counter > 25000:
            # drawPath(lab_map, full_path, guard_coord, loop_count)
            return list(squaresVisited), True
        guard_coord = moveGuard(guard_coord, guard_facing)

        # if tuple(guard_coord) in full_path and full_path[tuple(guard_coord)] == guard_facing:
        #     return list(squaresVisited), True

        full_path[tuple(guard_coord)] = guard_facing
        squaresVisited.add(tuple(guard_coord))

        isObstacle, continueProgram = isObstacleAhead(lab_map, guard_coord, guard_facing)

        if isObstacle:
            guard_facing = turnGuard(guard_facing)
    return list(squaresVisited), False


guard_symbols = ['v', '^', '<', '>']

lines = labmapp.splitlines()
lab_map = {}

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        lab_map[(row, col)] = char

guard_coord = find_guard(lab_map, guard_symbols)
guard_start = guard_coord
# print (guard_coord)
guard_facing = guard_facing(lab_map, guard_coord, guard_symbols)

squaresVisited = countGuardSteps(lab_map, guard_coord, guard_facing)[0]
squares_visited_no_start = squaresVisited[1:]
unique_squares = set(tuple(square) for square in squaresVisited)
squares_visited_no_start = set(tuple(square) for square in squares_visited_no_start)
print (f'Part 1: {len(unique_squares)}') # +1 for the guard starting position


loop_count = 0
full_path_list = []
#add a new obstacle '#' to the map and check if the guard enters into a loop and count how often that happens
loop_count = 0
for square in squares_visited_no_start:
    proposed_lab_map = {k:v for k,v in lab_map.items() if k != square}
    proposed_lab_map[square] = '#'
    _, loop = countGuardSteps(proposed_lab_map, guard_coord, guard_facing)
    if loop:
        loop_count += 1
        #print the loop count on the same line
        print (f'Loop count: {loop_count}', end='\r', flush=True)

print (f'\nPart 2: {loop_count}')


#1890,1889 is too high
