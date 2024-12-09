import time
import itertools

with open('test.txt') as f:
    antenna_data = f.read().splitlines()

def find_antinodes(antenna1, antenna2):
    #calculate distance between antennas
    distance = abs(antenna1[0] - antenna2[0]) + abs(antenna1[1] - antenna2[1])
    print (f'distance between {antenna1} and {antenna2} is {distance}')
    return 1

start_time = time.time()

# [(8, 1), (5, 2), (7, 3), (4, 4)] (7, 3)
# [(8, 1), (5, 2), (7, 3), (4, 4)] (4, 4)
# [(6, 5), (8, 8), (9, 9)] (8, 8)
# [(6, 5), (8, 8), (9, 9)] (9, 9)

antenna_map = {}
for row, line in enumerate(antenna_data):
    for col, char in enumerate(line):
        if char != '.':
            antenna_map[(col, row)] = char

frequency_mate = {}
for key, value in antenna_map.items():
    if value not in frequency_mate.keys():
         frequency_mate[value]= [k for k, v in antenna_map.items() if v == value]


sum =0
frequency_mate_combos = {}
for key, value in frequency_mate.items():
    frequency_mate_combos[key] = list(itertools.combinations(value, 2))
for key, value in frequency_mate_combos.items():
    for combo in value:
        sum += find_antinodes(combo[0], combo[1])










print ("--- %s seconds ---" % (time.time() - start_time))
