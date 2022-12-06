def isStart(signal):
    for letter in signal:
        if signal.count(letter)>1:
            return False
        else:
            continue
    return True

def scanSignals(signal_letters, target_length):
    signal = ''
    position = 0

    for signal_letter in signal_letters:
        signal = signal + signal_letter
        position += 1
        if len(signal)<target_length:
            continue
        if len(signal)>target_length:
            signal = signal[1:]
        if isStart(signal):
            return ([signal, position])


with open('day6_input_file') as f:
    signal_letters = f.readline()

marker_target_length = 4
message_target_length = 14
markerSignal = scanSignals(signal_letters, marker_target_length)
messageSignal = scanSignals(signal_letters, message_target_length)

print (markerSignal[0] + ' found at position ' +str(markerSignal[1]))
print (messageSignal[0] + ' found at position ' +str(messageSignal[1]))