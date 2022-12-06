import numpy as np

def movePointer (move, pointer): 
    moveMap = {
        'R' : [0,1],
        'L' : [0,-1],
        'D' : [1,0],
        'U' : [-1,0]
    }
    newPointer=np.add(pointer, moveMap[move]).tolist()
    if newPointer[0] < 0:
        newPointer[0] = 0
    if newPointer[0] > 2:
        newPointer[0] = 2
    if newPointer[1] < 0:
        newPointer[1] = 0
    if newPointer[1] > 2:
        newPointer[1] = 2
    return newPointer
    
with open('day2_input_file') as f:
    directions = f.readlines()

numpad = [[1,2,3], [4,5,6], [7,8,9]]
code = ''
for direction_list in directions:
    pointer = [1,1]
    for move in direction_list:
        if move.strip('\n') != '':
            pointer = movePointer(move.strip(), pointer)

    code = str(code) + str(numpad[pointer[0]][pointer[1]])

print (code)