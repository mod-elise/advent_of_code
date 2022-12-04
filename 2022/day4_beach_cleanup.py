import aoc_functions

with open('day4_input_file') as f:
    assignments = f.readlines()

containedCount = 0
anyOverlap = 0

for assignment in assignments:
    pairList = aoc_functions.parse_into_pairs(assignment)
    if aoc_functions.isContained(pairList[0], pairList[1]):
        containedCount += 1
    elif aoc_functions.isContained(pairList[1], pairList[0]):
        containedCount += 1
    if aoc_functions.isOverlap(pairList[0], pairList[1]):
        anyOverlap += 1
    elif aoc_functions.isOverlap(pairList[1], pairList[0]):
        anyOverlap += 1

print ("completely contained count: " +str(containedCount))
print ("any overlap: " + str(anyOverlap))