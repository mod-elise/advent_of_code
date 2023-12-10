f = open("input.txt", "r")
race_lines = f.readlines()

def integerise_list(range_list):
    return [int(item) for item in range_list if item != '']

def find_number_pairs(number):
    pairs = []
    for i in range(1, number):
        pair = (i, number - i)
        if pair[0] != 0 and pair[1] != 0:
            pairs.append(pair)
    return pairs

def find_product(pair):
    return pair[0] * pair[1]

times = integerise_list(race_lines[0][7:].split())
distances = integerise_list(race_lines[1][9:].split())

times_chars = race_lines[0][7:].split()
distances_chars = race_lines[1][9:].split()

time_string = ""
distance_string = ""
for time_char in times_chars:
    time_string = time_string + time_char
for distance_char in distances_chars:
    distance_string = distance_string + distance_char

time_p2 = int(time_string)
distance_p2 = int(distance_string)

print (time_string, distance_string)
print (times, distances)

part1_answer = 1
for i, time in enumerate(times):
    k = time
    pairs = find_number_pairs(k)
    ways_to_win = 0
    for pair in pairs:
        if find_product(pair) > distances[i]:
            ways_to_win += 1
    part1_answer = part1_answer * ways_to_win

pairs = find_number_pairs(time_p2)
ways_to_win = 0
part2_answer = 1
for pair in pairs:
    if find_product(pair) > distance_p2:
        ways_to_win += 1
part2_answer = part2_answer * ways_to_win

print (part1_answer)
print (part2_answer)
