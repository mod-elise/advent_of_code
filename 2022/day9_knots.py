def moveHead():
    t_list = []
    move = movement.split()
    direction = move[0]
    magnitude = int(move[1])
    for r in range(0,magnitude,1):
        #move the head       
        if direction == 'R':
            head[horizontal] += 1
        if direction == 'L':
            head[horizontal] -= 1
        if direction == 'U':
            head[vertical] += 1
        if direction == 'D':
            head[vertical] -= 1
        #move all the tails
        for i in range(0, len(knots), 1):
            try:
                if not isTailTouching(knots[i],knots[i+1]):
                    knots[i+1] = moveTail(knots[i],knots[i+1])
            except:
                continue
            #record the coords of the last tail 
            t_list.append(knots[len(knots)-1].copy())
    return t_list

def moveTail(Front, Follower):
    if (Front[horizontal] == Follower[horizontal]): 
        if Front[vertical] > Follower[vertical]:
            Follower[1] += 1
        else:
            Follower[1] -= 1         
    elif (Front[vertical] == Follower[vertical]):
        if Front[horizontal] > Follower[horizontal]:
            Follower[horizontal] += 1        
        else:
            Follower[horizontal] -= 1          
    else:
        if Front[vertical] > Follower[vertical]: 
            Follower[vertical] += 1
        if Front[vertical] < Follower[vertical]:
            Follower[vertical] -= 1
        if Front[horizontal] > Follower[horizontal]:
            Follower[horizontal] += 1
        if Front[horizontal] < Follower[horizontal]:
            Follower[horizontal] -= 1
    return Follower

def isTailTouching(head_coord, tail_coord):
    if (abs(head_coord[0] - tail_coord[0]) < 2) and (abs(head_coord[1] - tail_coord[1]) < 2):
        return True
    return False

with open('day9_input_file') as f:
    movements = f.readlines()

knots               = [
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0],
                        [0,0]
                    ]
head                = knots[0]
tail_history        = [[0,0]]
unique_tail_history = []
#constants
horizontal          = 0
vertical            = 1

for movement in movements:
   tail_history.extend(moveHead())

for tailloc in tail_history:
    if tailloc not in unique_tail_history:
        unique_tail_history.append(tailloc)

print (f'The tail visits {len(unique_tail_history)} unique places')