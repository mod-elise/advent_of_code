import time

def convert_list_items_to_ints (array):
    return [int(item) for item in array]

def get_diff (array):
    diff_array = []
    for i in range(len(array) -1):
        diff_array.append(array[i+1] - array[i])
    return diff_array

def extrapolate_value (original_reading,diffs):
    last_values = []
    for diff in diffs:
        last_values.append(diff[-1])
    return (original_reading + sum(last_values))

start_time = time.time()
f = open("input.txt", "r")
readings = f.readlines()
extrapolated_values = []

for reading in readings:
    reading = reading.split()
    reading = convert_list_items_to_ints(reading)
    original_reading = reading
    diffs = []
    while (sum(reading)) != 0:
        reading = get_diff(reading)
        diffs.append(reading)
    extrapolated_values.append(extrapolate_value(original_reading[len(original_reading)-1], diffs))

print (sum(extrapolated_values))
