def make_move (moveArray, fullShip):
    removedArray = []
    for i in range (0, int(moveArray[0])):
        stack = fullShip[int(moveArray[1])]
        try:
            removed = stack.pop()
        except:
            print (stack)
            print (moveArray)
            print ("trying to remove from empty stack?")
            exit()
        removedArray.append(removed)
    fullShip[int(moveArray[2])].extend(removedArray)
    return fullShip
    
with open('day5_input_file') as f:
    moves = f.readlines()

arrayZero   = ['']
arrayOne    = ['B', 'P', 'N', 'Q', 'H', 'D', 'R', 'T']
arrayTwo    = ['W', 'G', 'B', 'J', 'T', 'V']
arrayThree  = ['N', 'R', 'H', 'D', 'S', 'V', 'M', 'Q']
arrayFour   = ['P', 'Z', 'N', 'M', 'C']
arrayFive   = ['D', 'Z', 'B']
arraySix    = ['V', 'C', 'W', 'Z']
arraySeven  = ['G', 'Z', 'N', 'C', 'V', 'Q', 'L', 'S']
arrayEight  = ['L', 'G', 'J', 'M', 'D', 'N', 'V']
arrayNine   = ['T', 'P', 'M', 'F', 'Z', 'C', 'G']
fullShip    = [arrayZero, arrayOne, arrayTwo, arrayThree, arrayFour, arrayFive, arraySix, arraySeven, arrayEight, arrayNine]


for move in moves:
    moveArray = []
    words = move.split()
    for word in words:
        if word.isdigit():
            moveArray.append(word)
    fullShip = make_move(moveArray, fullShip)

for crates in fullShip:
    word = word + crates[-1]

print (word)


