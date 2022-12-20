import time
import math

def calcDistance (coord1, coord2):
    x_distance = abs(coord1[0] - coord2[0])
    y_distance = abs(coord1[1] - coord2[1])
    return x_distance + y_distance

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

start = time.time()
with open('day15_input_file') as f:
    sensor_readings = f.readlines()

sensor_data = []
min_x = 0
max_x = 10
min_y = 0
max_y = 10
beacon_list = []
sensor_list = []
noBeaconCount = 0
rowToCheck = 2000000

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

biggest_d = 0 #quiet, you

for  datum in sensor_data:
    d = calcDistance([datum[0],datum[1]],[datum[2], datum[3]])
    if d > biggest_d:
        biggest_d = d
    minx_distance = datum[0]- d
    maxx_distance = datum[0] + d
    miny_distance = datum[1] - d
    maxy_distance = datum[1] + d
    if minx_distance < min_x:
        min_x = minx_distance
    if maxx_distance > max_x:
        max_x = maxx_distance
    if miny_distance < min_y:
        min_y = miny_distance
    if maxy_distance > max_y:
        max_y = maxy_distance

i=0
for r in range (min_x, max_x+1, 1):
    i += 1
    if (math.floor(time.time()- start)  % 20 == 0) and (i % 100000 == 0) :
        print (f'{i} coords scanned in {time.time() - start}')
        print (r)
    proposedBeacon = [r,rowToCheck]
    closest_beacon = calcClosestBeacon([r,rowToCheck])
    rel_sensors = listSensors(proposedBeacon)
    sensors_Checked = 0
    for sensor in rel_sensors:
        if (calcDistance(proposedBeacon, sensor) <= calcDistance(closest_beacon, sensor)) and (proposedBeacon != closest_beacon):
            noBeaconCount +=1
            break

#well this takes about 90 seconds to complete.  Not going to work for part 2!
print (f'on row {rowToCheck} there are {noBeaconCount} places that cannot have a beacon')