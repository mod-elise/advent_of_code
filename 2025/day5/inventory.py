try:
    with open('input.txt', 'r') as file:
        print ("found file")
        rows = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded ranges")
        rows = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32""".strip().splitlines()
        
def getRangeEdges(range):
    theRange = range.split('-')
    return int(theRange[0]), int(theRange[1])

def isInRange(id, ranges):
    for range in ranges:
        lowerVal, upperVal = getRangeEdges(range)
        if id >=lowerVal and id <= upperVal:
            return True, upperVal  
    return False, 0

def getGlobalHighest(ranges):
    globalHighest = 0
    for theRange in ranges:
        _, upperVal = getRangeEdges(theRange)
        if upperVal > globalHighest:
            globalHighest = upperVal
    return globalHighest

def getLowestRangeValues(ranges):
    allLowestRanges = []
    for theRange in ranges:
        lowerVal, _ = getRangeEdges(theRange)
        allLowestRanges.append(lowerVal)

    return sorted(allLowestRanges)

# -------------- init --------- #
ranges = []
ids = []
inRanges = True
freshCount = 0
fullIdList = []

for row in rows:
    if row != '' and inRanges:
        ranges.append(row)
    else:
        inRanges = False
    if row != '' and not inRanges:
        ids.append(row)

ids = [int(x) for x in ids]

# ---------------part 1-------------#
for id in ids:
    inRange, _ = isInRange (id, ranges)
    if inRange:
        freshCount +=1

print (f'There are {freshCount} fresh items in stock')

# ---------------part 2--------------# 
i=0
freshCount = 0
globalHighest = getGlobalHighest(ranges)
lowestRanges = getLowestRangeValues(ranges)

while (i < globalHighest):
    inRange, upperVal = isInRange (i, ranges)
    if inRange:
        freshCount+= (upperVal - i + 1)
        i = upperVal + 1
    else:
        for nextLow in lowestRanges:
            if nextLow < i:
                continue
            else:
                i = nextLow
                break
 
print (f'There are  {freshCount} fresh item ids possible in the ranges')
