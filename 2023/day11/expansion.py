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

def calculate_blank_rows(galaxy):
    blank_rows = []
    for i,line in enumerate(galaxy):
        if '#' not in line:
            blank_rows.append(i)
    return blank_rows

def calculate_blank_columns(galaxy):
    blank_columns = []
    for i,line in enumerate(zip(*galaxy)):
        if '#' not in line:
            blank_columns.append(i)
    blank_columns.pop(len(blank_columns)-1)
    return blank_columns

start_time = time.time()
f = open("input_test.txt", "r")
galaxy = f.readlines()
y_expanded = expand_the_universe(galaxy, 1)
rotated_galaxy = [list(row) for row in zip(*reversed(y_expanded))]
rotated_galaxy_strs = []
for line in rotated_galaxy:
    rotated_galaxy_strs.append(''.join(line))

fully_expanded = expand_the_universe(rotated_galaxy_strs, 0)
# for line in fully_expanded:
#     print (line)

star_coords = []
for y, line in enumerate(fully_expanded):
    for x, char in enumerate(line):
        if char == '#':
            star_coords.append([x, y])


star_combos = calculate_star_combos(star_coords)
sum_of_shortest_distances = 0
for i, combo in enumerate(star_combos):
    sum_of_shortest_distances += (calculate_manhattan_distance(combo[0][0], combo[0][1], combo[1][0], combo[1][1]))

print (f'Sum of shortest distances in small galaxy: {sum_of_shortest_distances}')

# rather than actually expanding the galaxy (ie appending to a 2d array
# we can just infer the coordinates of the stars and push that into the manhattan calc
# so count the number of black rows and blank columns between them
# and add add a million to the relevant axis for each)
rows_that_have_no_stars = calculate_blank_rows(galaxy)
print (rows_that_have_no_stars)
columns_that_have_no_stars = calculate_blank_columns(galaxy)
print (columns_that_have_no_stars)

star_coords = []
for y, line in enumerate(galaxy):
    for x, char in enumerate(line):
        if char == '#':
            star_coords.append([x, y])


star_combos = calculate_star_combos(star_coords)
sum_of_shortest_distances = 0
for star_combo in star_combos:
    # rows_between = star_combo[1][1] - star_combo[0][1]

    add_rows = 0
    add_columns = 0
    start_row = min(star_combo[0][1],star_combo[1][1])
    end_row = max(star_combo[0][1],star_combo[1][1])
    for i in range(start_row,end_row):
        if i+star_combo[0][1] in rows_that_have_no_stars:
            add_rows += 1
    start_col = min(star_combo[0][0],star_combo[1][0])
    end_col = max(star_combo[0][0],star_combo[1][0])
    # if star_combo[1][0] < star_combo[0][0]:
    #     print ('start is greater than end')
    #     is_left = True
    # else:
    #     is_left = False
    for i in range(start_col,end_col):
        if i+star_combo[0][0] in columns_that_have_no_stars:
            add_columns += 1


#  this doesn't work because when the column of the second combo is to the 'left' of the first, it brings them closer,
# not further away
    combo[0][0] = star_combo [0][0]
    combo[0][1] = star_combo[0][1]
    combo[1][1] = star_combo[1][1] +add_rows
    # if the second combo is to the right of the first
    # if not is_left:
    #     combo[1][0] = star_combo[1][0] + add_columns
    # # if the second combo is to the left of the first
    # elif is_left:
    #     combo[0][0] = star_combo[0][0] + add_columns

    print (star_combo, add_rows, add_columns, combo, calculate_manhattan_distance(combo[0][0], combo[0][1], combo[1][0], combo[1][1]))
    sum_of_shortest_distances += (calculate_manhattan_distance(combo[0][0], combo[0][1], combo[1][0], combo[1][1]))

print (sum_of_shortest_distances)
    # print(star_combo,rows_between)
print ("--- %s seconds ---" % (time.time() - start_time))
