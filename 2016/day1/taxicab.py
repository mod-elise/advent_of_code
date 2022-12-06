def changeCoord(coords, params, distance):
    if params[1] == 'up':
        coords[params[0]] += int(distance)
    if params[1] == 'down':
        coords[params[0]] -= int(distance)
    return coords

def changeCoordSteps(coords, params, distance, coordsHistory):
    if params[1] == 'up':
        for i in range (0,int(distance)):
            coords[params[0]] += 1
            if coords in coordsHistory:
                coordsHistory.append(coords.copy())
                return ([True, coords, coordsHistory])
            else:
                coordsHistory.append(coords.copy())
    if params[1] == 'down':
        for i in range (0,int(distance)):
            coords[params[0]] -= 1
            if coords in coordsHistory:
                coordsHistory.append(coords.copy())
                return ([True, coords, coordsHistory])
            else:
                coordsHistory.append(coords.copy())
    return ([False, coords, coordsHistory])
           

with open('day1_input_file') as f:
    directions = f.readline()

coords          = [0,0]
coordsHistory   = [[0,0]]
orientations    = ['N', 'E', 'S', 'W']
orientation     = 0
directions = directions.split(', ')
for direction in directions:
    turn    = direction[0:1]
    distance= direction[1:]
    if turn == 'R':
        orientation += 1
    else:
        orientation -= 1
    lookupOrientation = orientations[orientation % 4]
    if lookupOrientation == 'N':
        params = [1, 'up']
    elif lookupOrientation == 'S':
        params = [1, 'down']
    elif lookupOrientation == 'E':
        params = [0, 'up']
    else:
        params = [0, 'down']

    coordArray = changeCoordSteps(coords, params, distance, coordsHistory)
    coords = coordArray[1]
    coordsHistory = coordArray[2]
    if coordArray[0]:
        break

print (coords)
print (abs(coords[0]) + abs(coords[1]))