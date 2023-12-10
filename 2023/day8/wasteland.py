import time
start_time = time.time()
f = open("input.txt", "r")
lines = f.readlines()

directions = lines[0]
nodes = {}

for i, line in enumerate(lines):
    if i > 1:
        node = line.strip().split(" = ")
        destinations = node[1].replace(')', '')
        destinations = destinations.replace('(', '')
        destinations = destinations.split(', ')
        nodes[node[0]] = destinations
counter = 0
location = 'AAA'
while location != 'ZZZ':
    i = counter % (len(directions)-1)
    if directions[i] == 'L':
        direction = 0
    else:
        direction = 1
    location = nodes[location][direction]
    print (counter , directions[i], nodes[location], location)
    counter = counter + 1

print (f'Steps taken = {counter}')
print ("--- %s seconds ---" % (time.time() - start_time))
