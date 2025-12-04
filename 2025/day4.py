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

with open('input.txt', 'r') as file:
    rows = file.read().splitlines()

rows = pad_array(rows)
adj_coords = generate_coords()
available = 0
adjacent_count = 0

for i in range (1, len(rows)-1):
    for j in range (1, len(rows[i])-1):
        if rows[i][j] == '1':
            adjacent_count = count_adjacent(i,j)
            if adjacent_count < 4:
                available +=1
print (available)