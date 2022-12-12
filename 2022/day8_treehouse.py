def prRed(skk): print("\033[91m{}\033[00m" .format(skk),end='')
 
 
def prGreen(skk): print("\033[92m{}\033[00m" .format(skk), end='')

def isBlocked_H(start, end, step, height):
    for r in range(start, end, step):
        if tree_row[r] >= height:
            return 1
    return 0

def isBlocked_V(start, end, step, column, height):
    for r in range(start, end, step):
        if tree_rows[r][column] >= height:
            return 1
    return 0

def isVisible(col, row, height):
    visible = True
    blockedCount = 0
    if col == 0 or col == len(tree_row)-1:
        return visible
    if row == 0 or row == len(tree_row)-1:
        return visible
    #check right
    blockedCount += isBlocked_H(col+1, len(tree_row), 1, height)
    #check left
    blockedCount += isBlocked_H(col-1, -1, -1, height)
    #check down
    blockedCount += isBlocked_V(row+1, len(tree_rows), 1, col, height)
    #check up
    blockedCount += isBlocked_V(row-1, -1, -1, col, height)
    if blockedCount == 4:
        visible=False
    return visible

def score_H(start, end, step, height):
    score = 0
    for r in range(start, end, step):
        score += 1
        if tree_row[r] >= height:
            break
    return score
    
def score_V(start, end, step, column, height):
    score = 0 
    for r in range(start, end, step):
        score += 1
        if tree_rows[r][column] >= height:
            break
    return score
    
def calcScenicScore(col, row, height):
    if col == 0 or col == len(tree_row)-1:
        return 0
    if row == 0 or row == len(tree_row)-1:
        return 0
    #check right
    score = score_H(col+1, len(tree_row), 1, height)
    #check left
    score *= score_H(col-1, -1, -1, height)
    #check down    
    score *= score_V(row+1, len(tree_rows), 1, col, height)
    #check up    
    score *= score_V(row-1, -1, -1, col, height)
    
    return score




with open('day8_input_file') as f:
    tree_rows = f.readlines()

tree_grid       = []
tree_row_num    = 0
hiddenCount     = 0
visibleCount    = 0
scenicScores    = []
maprows         = []

for tree_row in tree_rows:
    tree_col_num = 0
    maprow = []
    for tree in tree_row:
        tree_row = tree_row.strip()
        if tree.isdigit():
            if isVisible(tree_col_num, tree_row_num, tree):
                maprow.append(1)
                visibleCount += 1
            else:
                maprow.append(0)
                hiddenCount += 1
            scenicScores.append(calcScenicScore(tree_col_num, tree_row_num, tree))
            tree_col_num += 1
    maprows.append(maprow)
    tree_row_num += 1

print (f' Number of visible trees is {visibleCount}')
print (f' The most scenic tree has a score of {max(scenicScores)}')
for maprow in maprows:
    for t_ree in maprow:
        if t_ree:
            prGreen('T')
        else:
            prRed('T')
    print()