import aoc_functions


with open('day6_input_file') as f:
    signal_letters = f.readline()

marker_target_length = 4
message_target_length = 14
markerSignal = aoc_functions.scanSignals(signal_letters, marker_target_length)
messageSignal = aoc_functions.scanSignals(signal_letters, message_target_length)

print (markerSignal[0] + ' found at position ' +str(markerSignal[1]))
print (messageSignal[0] + ' found at position ' +str(messageSignal[1]))