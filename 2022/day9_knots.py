def moveHead(trail_history):
    global i
    t_list = []
    move = movement.split()
    direction = move[0]
    magnitude = int(move[1])

    for r in range(0,magnitude,1):

        if direction == 'R':
            H[horizontal] += 1
        if direction == 'L':
            H[horizontal] -= 1
        if direction == 'U':
            H[vertical] += 1
        if direction == 'D':
            H[vertical] -= 1
        if not isTailTouching(H,T):
            moveTail()
            t_list.append(T.copy())
    return t_list

def moveTail():
    if (H[horizontal] == T[horizontal]): 
        if H[vertical] > T[vertical]:
            T[1] += 1
            if not isTailTouching(H,T):
                exit ('touching error')
        else:
            T[1] -= 1
            if not isTailTouching(H,T):
                exit ('touching error')            
    elif (H[vertical] == T[vertical]):
        if H[horizontal] > T[horizontal]:
            T[horizontal] += 1
            if not isTailTouching(H,T):
                exit ('touching error')            
        else:
            T[horizontal] -= 1
            if not isTailTouching(H,T):
                exit ('touching error')           
    else:
        if H[vertical] > T[vertical]: 
            T[vertical] += 1
        if H[vertical] < T[vertical]:
            T[vertical] -= 1
        if H[horizontal] > T[horizontal]:
            T[horizontal] += 1
        if H[horizontal] < T[horizontal]:
            T[horizontal] -= 1
    if not isTailTouching(H,T):
        exit ('touching error')


def isTailTouching(head_coord, tail_coord):


    if (abs(head_coord[0] - tail_coord[0]) < 2) and (abs(head_coord[1] - tail_coord[1]) < 2):
        return True
    return False

# with open('day9_test') as f:
#     movements = f.readlines()
#     

with open('day9_input_file') as f:
    movements = f.readlines()

H = [0,0]
T = [0,0]
tail_history = [[0,0]]
unique_tail_history = []

horizontal  = 0
vertical    = 1

for movement in movements:
   tail_history.extend(moveHead(tail_history))


for tailloc in tail_history:
    if tailloc not in unique_tail_history:
        unique_tail_history.append(tailloc)

print (f'The tail of one knot visits {len(unique_tail_history)} unique places')
