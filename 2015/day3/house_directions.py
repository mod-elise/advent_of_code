def unique_list(input_list):
    u_list =[] 
    for coord in input_list:
        if coord not in u_list:
            u_list.append(coord)
    return u_list

def follow_directions (coords, direction):
    if direction == '^':
        coords[1] +=1
    elif direction == 'v':
        coords[1] -=1
    elif direction == '>':
        coords[0] +=1
    elif direction == '<':
        coords[0] -=1
    return coords

with open('day3_input_file') as f:
    directions = f.readline()

dir_list = list(directions)

coords = [0,0]
santa_coords = [0,0]
robo_coords = [0,0]
one_coord_list = []
santa_coord_list = []
robo_coord_list = []
iterator = 1

for direction in dir_list:
    coords=follow_directions(coords, direction)
    one_coord_list.append([coords[0], coords[1]])
    if iterator % 2 == 1:
        santa_coords = follow_directions(santa_coords, direction)
        santa_coord_list.append([santa_coords[0], santa_coords[1]])
    else:
        robo_coords = follow_directions(robo_coords, direction)
        robo_coord_list.append([robo_coords[0], robo_coords[1]])
    iterator +=1
 

robo_santa_houses= []
unique_houses = len(unique_list(one_coord_list))
robo_santa_houses.extend(santa_coord_list)
robo_santa_houses.extend(robo_coord_list)
unique_robo_santa_houses = len(unique_list(robo_santa_houses))


print ("Santa Alone: " + str(unique_houses))
print ("Santa and Robo: " + str(unique_robo_santa_houses))
