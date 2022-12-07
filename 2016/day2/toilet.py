import numpy as np

def movePointer3x3 (move, pointer): 
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
            pointer = movePointer3x3(move.strip(), pointer)

    code = str(code) + str(numpad[pointer[0]][pointer[1]])

print (code)


padMap = {
    '1'     : [0,'3',0,0],
    '2'     : [0,'6',0,'3'],
    '3'     : ['1','7','2','4'],
    '4'     : [0,'8','3',0],
    '5'     : [0,0,0,'6'],
    '6'     : ['2','A','5','7'],
    '7'     : ['3','B','6','8'],
    '8'     : ['4','C','7','9'],
    '9'     : [0,0,'8',0],
    'A'     : ['6',0,0,'B'],
    'B'     : ['7','D','A','C'],
    'C'     : ['8',0,'B',0],
    'D'     : ['B',0,0,0],
}

directionMap = {
    'U' :   0,
    'D' :   1,
    'L' :   2,
    'R' :   3
}

currentNum = '5'
code = ''
for direction_list in directions:
    for direction in direction_list:
        try:
            newNum =  padMap[currentNum][directionMap[direction.strip('\n')]]
        except:
            pass
        if newNum:
            currentNum = newNum
    code = code + currentNum

print (code)
