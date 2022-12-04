with open('day1_input_file') as f:
    directions = f.readlines()


dir_list = list(str(directions))
up = dir_list.count('(')
down = dir_list.count(')')
print (up-down)

position = 0
floor = 0 
for dir in dir_list:
    if dir == '(':
        floor +=1
    elif dir == ')':
        floor -=1
    else:
        continue
    print (dir + ' -> ' + str(floor))
    position +=1
    if floor < 0:
        print (position)
        exit()