runningTotal = 0
listOfFrequencies = [0]
listOfFreqChanges = []
duplicateFound = False
with open('input.txt') as f:
    for line in f:
        runningTotal += int(line.strip())
        listOfFreqChanges.append(int(line.strip()))
print(f"Final frequency reached is: {runningTotal}")
runningTotal = 0
listOfFrequencies = [0]
iterations = 0
seenFrequencies = set(listOfFrequencies)
while not duplicateFound:
    for freqChange in listOfFreqChanges:
        runningTotal += freqChange
        if runningTotal in seenFrequencies:
            duplicateFound = True
            break
        seenFrequencies.add(runningTotal)
    iterations += 1
print(f"First frequency reached twice is: {runningTotal}")
