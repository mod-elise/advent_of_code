import time

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def calculate_star_combos(coords):
    coord_combos = []
    for i, coord in enumerate(coords):
        for i in range(i+1, len(coords)):
            coord_combos.append([coord, coords[i]])
    return coord_combos

def expand_the_universe(expanding_galaxy, expansion_factor):
    galaxy_width = len(expanding_galaxy[0]) - expansion_factor
    empty_row = ''
    for i in range(galaxy_width):
        empty_row += '.'

    expanded = []

    for line in expanding_galaxy:
        if '#' in line:
            expanded.append(line.strip())
        else:
            expanded.append(empty_row)
            expanded.append(empty_row)

    return expanded

start_time = time.time()
f = open("input.txt", "r")
galaxy = f.readlines()
y_expanded = expand_the_universe(galaxy, 1)
for line in y_expanded:
    print (line)
print ('\n---------------------\n')
rotated_galaxy = [list(row) for row in zip(*reversed(y_expanded))]
rotated_galaxy_strs = []
for line in rotated_galaxy:
    rotated_galaxy_strs.append(''.join(line))

fully_expanded = expand_the_universe(rotated_galaxy_strs, 0)
for line in fully_expanded:
    print (line)

star_coords = []
for y, line in enumerate(fully_expanded):
    for x, char in enumerate(line):
        if char == '#':
            star_coords.append([x, y])


star_combos = calculate_star_combos(star_coords)
sum_of_shortest_distances = 0
print (star_coords)
for i, combo in enumerate(star_combos):
    print (i, combo)
    sum_of_shortest_distances += (calculate_manhattan_distance(combo[0][0], combo[0][1], combo[1][0], combo[1][1]))

print (sum_of_shortest_distances)
print ("--- %s seconds ---" % (time.time() - start_time))
