import time
import math

def clean_coords(coords):
    coords_to_remove =[]
    for coord in coords:
        
        u= [coord[0], coord[1]-1]
        d= [coord[0], coord[1]+1]
        l= [coord[0]-1, coord[1]]
        r= [coord[0]+1, coord[1]]
        ul= [coord[0]-1, coord[1]-1]
        ur= [coord[0]+1, coord[1]-1]
        dl= [coord[0]-1, coord[1]+1]
        dr= [coord[0]+1, coord[1]+1]

        if (u in coords) and (l in coords) and (r in coords):
            if (ul in coords) and (ur in coords):
                if (dl in coords) and (dr in coords):
                    coords_to_remove.append(coord)
    for removing in coords_to_remove:
        coords.remove(removing)
    return coords


class Cave:
    def isWall (self, x,y):
        start_wall = time.time()
        for coords in self.coord_ranges:
            if (x in coords[0]) and (y in coords[1]):
                if y > self.lowest_wall:
                    self.lowest_wall = y
                return True
        return False

    def __init__ (self, cave_walls):
        walls = []
        self.coord_ranges = []
        for wall_lines in cave_walls:
            wall_lines = wall_lines.strip('\n')
            wall = (wall_lines.split('->'))
            for r in range (0, len(wall),1):
                w = wall[r].strip(' ')
                w = w.split(',')
                w = list(map(int, w))
                wall[r] = w
            walls.append(wall)
        for wall in walls:
            for r in range (0, len(wall)-1, 1):
                if (wall[r][0] < wall[r+1][0]):
                    x_range = range (wall[r][0], wall[r+1][0]+1)
                else:
                    x_range = range (wall[r+1][0], wall[r][0]+1)
                if (wall[r][1] < wall[r+1][1]):                    
                    y_range = range (wall[r][1], wall[r+1][1]+1)
                else:
                    y_range = range (wall[r+1][1], wall[r][1]+1)
                self.coord_ranges.append([x_range, y_range])

        notFound = True
        i = 250
        x_coords = []
        for coords in self.coord_ranges:
            for coord in coords[1]:
                x_coords.append(coord)
        self.lowest = max(x_coords)
        self.lowest_wall = 0

        i =0
        for coords in self.coord_ranges:
            if i in coords[1]:
                self.highest = i
                break
            i+=1

start = time.time()
with open('day14_input_file') as f:
    cave_walls = f.readlines()

cave = Cave(cave_walls)
print (f'lowest is {cave.lowest}')
walls = []

sand_piling = True
sand_x = 500
sand_y = 0
sand_coords = []
sand_coords.extend(walls)
infinity = 0
count = 0

while sand_piling:
    if (not cave.isWall(sand_x,sand_y+1)) and ([sand_x, sand_y+1] not in sand_coords):
        sand_y += 1
        #go left
    elif (not cave.isWall(sand_x-1,sand_y+1)) and ([sand_x-1, sand_y+1] not in sand_coords):
        sand_x -= 1
        sand_y +=1
        #go right
    elif (not cave.isWall(sand_x+1,sand_y+1)) and ([sand_x+1, sand_y+1] not in sand_coords):
        sand_x += 1
        sand_y +=1
        #settle
    else:
        sand_coords.append([sand_x, sand_y])
        sand_x, sand_y = 500,0
        count +=1
    if sand_y > cave.lowest:
        print (f'infinity = {infinity}')
        infinity += 1
        sand_x, sand_y = 500,0
    if infinity == 2:
        sand_piling = False

print (f'sand particles that fell in part 1: {count}')
end = time.time()
total_time = end - start
print (str(total_time))

print ('part 2...')
sand_piling = True
sand_x = 500
sand_y = 0
sand_coords = []
infinity = 0
count = 0
floor = cave.lowest +2


while sand_piling:
    if (not cave.isWall(sand_x,sand_y+1)) and ([sand_x, sand_y+1] not in sand_coords) and (sand_y+1 < floor):
        sand_y += 1
        #go left
    elif (not cave.isWall(sand_x-1,sand_y+1)) and ([sand_x-1, sand_y+1] not in sand_coords) and (sand_y+1 < floor):
        sand_x -= 1
        sand_y +=1
        #go right
    elif (not cave.isWall(sand_x+1,sand_y+1)) and ([sand_x+1, sand_y+1] not in sand_coords and (sand_y+1 < floor)):
        sand_x += 1
        sand_y +=1
        #settle
    else:
        sand_coords.append([sand_x, sand_y])
        if (sand_x==500) and (sand_y==0):
            count+=1
            sand_piling = False
            break
        sand_x, sand_y = 500,0
        count +=1
        if (count) % 250 == 0:
            print (f'{count} grains of sand fallen in {time.time() - start}')
            print (len(sand_coords))
        if count <= 10000:
            if count % 1000 == 0:
                sand_coords = clean_coords(sand_coords)
                print (len(sand_coords))
        else:
            if count % 2500 == 0:
                sand_coords = clean_coords(sand_coords)
                print (len(sand_coords))

print (f'part two grains fell = {count}')