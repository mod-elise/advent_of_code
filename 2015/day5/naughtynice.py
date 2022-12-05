def ridiculous_niceCount(naughynices):

    naughties = ['ab', 'cd', 'pq', 'xy']
    vowels = "aeiou"
    niceCount = 0
    naughtyCount = 0

    for naughtynice in naughtynices:
        naughty = False
        if any(x in naughtynice for x in naughties):
            naughtyCount += 1
            naughty = True
        if naughty:
            continue
        vowel_count = 0
        for v in vowels:
            vowel_count += (naughtynice.lower().count(v))
        if vowel_count < 3:
            naughtyCount += 1
            naughty = True
        if naughty:
            continue
        naughty = True
        for i in range (len(naughtynice)-1):
            if naughtynice[i] == naughtynice[i+1]:
                naughty = False
        if not naughty:
            niceCount +=1
        else:
            naughtyCount +=1
    return (niceCount)
    
def checkNice(checkString):
    nice = False
    save = []
    niceCriteria =0
    xyxCriteria = False
    doubleStringCriteria = False
    for i in range (len(checkString)-1):
        pairToTest = checkString[i] + checkString[i+1]
        checkWithoutTest =  checkString[0 : i : ] + checkString[i + 2 : :]
        checkWithoutTest = checkWithoutTest[:i] + '99' + checkWithoutTest[:i]
        if not doubleStringCriteria:
            if pairToTest in checkWithoutTest:
                doubleStringCriteria = True
                save.append(pairToTest)


    for i in range (len(checkString)-2):
        if not xyxCriteria:
            if checkString[i] == checkString[i+2]:
                xyxCriteria = True
                save.append(checkString[i]+checkString[i+1]+checkString[i+2])
    if doubleStringCriteria:
        niceCriteria += 1
    if xyxCriteria:
        niceCriteria += 1
    if niceCriteria == 2:
        nice = True
    return nice


with open('day5_input_file') as f:
    naughtynices = f.readlines()


print (ridiculous_niceCount(naughtynices))

niceCount = 0
for naughtynice in naughtynices:
    if checkNice(naughtynice.rstrip("\n")):
        niceCount +=1

print (niceCount)