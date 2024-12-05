with open('test.txt') as f:
    wordsearch = f.read()

def getAdjCoords(coords, line_length):
    x = coords[0]
    y = coords[1]
    if x == 0:
        if y == 0:
            return [(x+1, y), (x, y+1), (x+1, y+1)]
        elif y == line_length-1:
            return [(x+1, y), (x, y-1), (x+1, y-1)]
        else:
            return [(x+1, y), (x, y+1), (x+1, y+1), (x, y-1), (x+1, y-1)]
    elif x == line_length-1:
        if y == 0:
            return [(x-1, y), (x, y+1), (x-1, y+1)]
        elif y == line_length-1:
            return [(x-1, y), (x, y-1), (x-1, y-1)]
        else:
            return [(x-1, y), (x, y+1), (x-1, y+1), (x, y-1), (x-1, y-1)]
    elif y == 0:
        return [(x-1, y), (x+1, y), (x-1, y+1), (x+1, y+1)]
    elif y == line_length-1:
        return [(x-1, y), (x+1, y), (x-1, y-1), (x+1, y-1)]
    else:
        return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y+1), (x+1, y+1), (x-1, y-1), (x+1, y-1)]

def checkCoords(coords_list, origin, letter):
    return_obj = {}
    directions = {
        'north': (0,-1),
        'south': (0,1),
        'east': (1,0),
        'west': (-1,0),
        'north-east': (1,-1),
        'north-west': (-1,-1),
        'south-east': (1,1),
        'south-west': (-1,1)
    }
    for coords in coords_list:
        if wordsearch[coords[1]][coords[0]] == letter:
            origin_x = origin[0]
            origin_y = origin[1]
            direction_x = coords[0] + origin_x
            direction_y = coords[1] + origin_y
            direction = list(directions.keys())[list(directions.values()).index((direction_x,direction_y))]
            return_obj[coords] = [origin, direction]
    return return_obj

to_find = 'XMAS'
wordsearch = wordsearch.splitlines()
wordsearch = [list(line) for line in wordsearch]
line_length = len(wordsearch[0])
for i_idx, i in enumerate(wordsearch):
    for j_idx, j in enumerate(i):
        if j == to_find[0]:
            all_adj_coords = getAdjCoords((j_idx,i_idx),line_length)
            next_coords = checkCoords(all_adj_coords, [j_idx,i_idx], to_find[0])
            print (next_coords)
