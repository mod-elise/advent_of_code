import time
import math

def calcDistance (coord1, coord2):
    x_distance = abs(coord1[0] - coord2[0])
    y_distance = abs(coord1[1] - coord2[1])
    return x_distance + y_distance

def calcClosest(coord, items):
    smallest_dist = 5000000
    for item in items:
        item_dist = calcDistance(coord, item)
        if  item_dist < smallest_dist:
            smallest_dist = item_dist
            closest_item = item
    return closest_item

def calcClosestBeacon(coord):
    smallest_dist = 5000000
    for beacon in beacon_list:
        beacon_dist = calcDistance (coord, beacon)
        if beacon_dist < smallest_dist:
            smallest_dist = beacon_dist
            closest_beacon = beacon
    return closest_beacon

def listSensors(coord):
    sensors = []
    for sensor in sensor_list:
        sensor_dist = calcDistance(coord, sensor)
        if sensor_dist<biggest_d:
            sensors.append(sensor)
    return sensors

def getCorners(coords, distance):
    leftMost_x    = (coords[0] - (distance+1))
    rightMost_x   = (coords[0] + (distance+1))
    upMost_y      = (coords[1] - (distance +1))
    bottomMost_y  = (coords[1] - (distance+1))
    return [[leftMost_x, coords[1]],[rightMost_x, coords[1]], [coords[0], upMost_y], [coords[0], bottomMost_y]]

def getOutsideCoords(sensor_coords, beacon_coords):
    d = calcDistance(sensor_coords, beacon_coords)
    corners = getCorners(sensor_coords, d)
    edges           = []
    i = 0

    #left upper quad
    pointer         = corners[0]
    while pointer != corners[2]:
        i+=1
        pointer[0], pointer[1] = pointer[0] +1, pointer[1] - 1
        if (pointer[0] < 0) or (pointer[1] < 0) or (pointer[0]> 4000000) or (pointer[1] > 4000000):
            continue
        else:
            edges.append(pointer.copy())
        if i % 1000000 == 0:
            print (f'{i} left upper edge coords scanned in {time.time() - start}')

    #right upper quad
    pointer         = corners[1]
    while pointer != corners[2]:
        i+=1
        pointer[0], pointer[1] = pointer[0] - 1, pointer[1] - 1
        if (pointer[0] < 0) or (pointer[1] < 0) or (pointer[0]> 4000000) or (pointer[1] > 4000000):
            continue
        else:
            edges.append(pointer.copy())
        if i % 1000000 == 0:
            print (f'{i} right upper edge coords scanned in {time.time() - start}')

    #left lower quad
    pointer         = corners[3]
    while pointer != corners[0]:
        i+=1
        pointer[0], pointer[1] = pointer[0] -1, pointer[1] + 1
        if (pointer[0] < 0) or (pointer[1] < 0) or (pointer[0]> 4000000) or (pointer[1] > 4000000):
            continue
        else:
            edges.append(pointer.copy())
        if i % 1000000 == 0:
            print (f'{i} left lower edge coords scanned in {time.time() - start}')

    #right lower quad
    pointer         = corners[3]
    while pointer != corners[2]:
        i+=1
        pointer[0], pointer[1] = pointer[0] +1, pointer[1] + 1
        if (pointer[0] < 0) or (pointer[1] < 0) or (pointer[0]> 4000000) or (pointer[1] > 4000000):
            continue
        else:
            edges.append(pointer.copy())
        if i % 1000000 == 0:
            print (f'{i} right lower edge coords scanned in {time.time() - start}')

    edges.extend(corners)
    return edges

start = time.time()
with open('day15_input_file') as f:
    sensor_readings = f.readlines()

with open('already_rejected') as g:
    rejections = g.readlines()

rejections = tuple(rejections)

sensor_data = []
min_x = 0
max_x = 4000000
min_y = 0
max_y = 4000000
beacon_list = []
sensor_list = []
noBeaconCount = 0
rowToCheck = 10

for sensor_reading in sensor_readings:
    useful_bits = []
    sensor_reading = sensor_reading.strip()
    sensor_reading_items = sensor_reading.split('=')
    for sensor_reading_item in sensor_reading_items:
        if (sensor_reading_item[0].isdigit() or sensor_reading_item[0]=='-'):
            useful_bits.append(sensor_reading_item)
            
    useful_bits[0] = useful_bits[0].split(',')
    sensor_x = int(useful_bits[0][0])
    useful_bits[1] = useful_bits[1].split(':')
    sensor_y = int(useful_bits[1][0])
    useful_bits[2] = useful_bits[2].split(',')
    beacon_x= int(useful_bits[2][0])
    try:
        beacon_y= int (useful_bits[3])
    except:
        beacon_y = 999
    if [sensor_x, sensor_y] not in sensor_list:
        sensor_list.append([sensor_x, sensor_y])
    if [beacon_x, beacon_y] not in beacon_list:
        beacon_list.append([beacon_x, beacon_y])
    sensor_data.append([sensor_x, sensor_y, beacon_x, beacon_y])

possible_Coords  = []
biggest_d = 0

j=0
for  datum in sensor_data:
    j+=1
    print (f'*******************get sensor {j} of {len(sensor_data)}**************')
    possible_Coords.extend(getOutsideCoords([datum[0],datum[1]],[datum[2], datum[3]]))
    d = calcDistance([datum[0],datum[1]],[datum[2], datum[3]])
    if d > biggest_d:
        biggest_d = d

rejectedCoords = []
acceptedCoords = []
i = 0
possible_Coords = tuple(possible_Coords)
print ('#######now rejecting candidates........#####')
for possible_coord in possible_Coords:
    i=i+1
    if possible_coord in rejections:
        if i % 250001 == 0:
            print (f'{i:,} coords scanned of {len(possible_Coords):,} in {math.floor(time.time() - start):,} seconds')

        continue
    rejected= False
    
    if i % 250001 == 0 :
        print (f'{i:,} coords scanned of {len(possible_Coords):,} in {math.floor(time.time() - start):,} seconds')
        remaining_coords = len(possible_Coords) -i
        time_per = i / math.floor(time.time() - start)
        remaining_time = remaining_coords / time_per / 60
        print (f'estimated time {math.floor(remaining_time):,} minutes')
        
    i = i - 1
    if (possible_coord[0] < 0)or (possible_coord[1] < 0):
        continue
    if (possible_coord[0] > max_x)or (possible_coord[1] > max_x):
        continue

    closest_sensor = calcClosest(possible_coord, sensor_list)
    rel_sensors = listSensors(possible_coord)
    for sensor in rel_sensors:
        closest_beacon = calcClosestBeacon(sensor)
        if (calcDistance(possible_coord, sensor) <= calcDistance(closest_beacon, sensor)):
            rejectedCoords.append(possible_coord)
            rejected=True
            break
    if rejected== False:
        acceptedCoords.append(possible_coord)
    i += 1


i = 0
rejectedCoords = tuple(rejectedCoords)
print ('final checks....')

print (f'candidates: {acceptedCoords}')



for possible_coord in possible_Coords:
    if i %  100000 == 0:
        print (f'{i:,} coords scanned of {len(possible_Coords):,} in {math.floor(time.time() - start):,} seconds')
    if (possible_coord not in rejectedCoords) and (possible_coord[0]>0) and (possible_coord[1]>0):
        print (f'{possible_coord[0]} * 4,000,000 + {possible_coord[1]} equals', end= ' ')
        distress_beacon = (possible_coord[0] * 4000000) + possible_coord[1]
        print (distress_beacon)
    i += 1


print (distress_beacon)
