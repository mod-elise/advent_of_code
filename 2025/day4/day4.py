def pad_array(rows):
    new_list = []
    row_length = len(rows[0])
    blank_row = ''
    for i in range (0, row_length+2):
        blank_row = blank_row + '0'
    new_list.append(blank_row)
    for row in rows:
        row = row.replace('.', '0')
        row = row.replace('@', '1')
        new_row = '0' + row + '0'
        new_list.append(new_row)
    new_list.append(blank_row)
    return (new_list)

def generate_coords():
    tl = [-1, -1]
    tm = [-1, 0]
    tr = [-1, 1]
    l = [0, -1]
    r = [0, 1]
    bl = [1, -1]
    bm = [1, 0]
    br = [1,1]
    return ([tl, tm, tr, l, r, bl, bm, br])

def count_adjacent(i,j):
    total = 0
    for coord_to_check in adj_coords:
        x = coord_to_check[0]
        y = coord_to_check[1]
        total += int(rows[i+y][j+x])
    return total

def isAvailable(i, j):
    if rows[i][j] == '1':
        adjacent_count = count_adjacent(i,j)
        if adjacent_count < 4:
            return True
    return False

def getListOfAvailable():
    available_list = []
    for i in range (1, len(rows)-1):
        for j in range (1, len(rows[i])-1):
            if isAvailable(i, j):
                available_list.append((i-1, j-1))
    return available_list

def removeFromAvailable(coord):
    i = coord[0] + 1
    j = coord[1] + 1
    rows[i] = rows[i][:j] + '0' + rows[i][j+1:]

# -------------------------Main Code----------------------------
try:
    with open('input.txt', 'r') as file:
        print ("found file")
        rows = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded ranges")
        rows = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".strip().splitlines()

rows = pad_array(rows)
adj_coords = generate_coords()

#----Part 1----
available = getListOfAvailable()
print (f'Totally initial available: {len(available)}')

can_be_removed = 0
while len(available) > 0:
    available = getListOfAvailable()
    can_be_removed += len(available)
    if len(available) == 0:
        break
    else:
        for coord in available:
            removeFromAvailable(coord)

print (f'Totally can be removed: {can_be_removed}')