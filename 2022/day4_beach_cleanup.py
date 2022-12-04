
def parse_into_pairs(assignment):
    parsedPair = []
    unlistedPairs = assignment.split(",")
    parsedPair.append (unlistedPairs[0].split("-"))
    parsedPair.append (unlistedPairs[1].split("-"))
    return parsedPair

def isContained (range1, range2):
    lowerInRange=False
    upperInRange=False
    if (int(range1[0]) >= int(range2[0])) and (int(range1[0]) <= int(range2[1])):
        lowerInRange = True
    if (int(range1[1]) <= int(range2[1])):
        upperInRange = True
    if lowerInRange and upperInRange:
        return True
    else:
        return False
  

with open('day4_input_file') as f:
    assignments = f.readlines()

count = 0
for assignment in assignments:
    pairList = parse_into_pairs(assignment)
    if isContained(pairList[0], pairList[1]):
        count += 1
    elif isContained(pairList[1], pairList[0]):
        count += 1

print (count)