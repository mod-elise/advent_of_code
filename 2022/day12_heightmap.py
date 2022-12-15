class mapNode:
    def __init__(self, coords, connected_nodes):
        self.coords         = coords
        self.up             = connected_nodes['up']
        self.down           = connected_nodes['down']
        self.left           = connected_nodes['left']
        self.right          = connected_nodes['right']
        self.height         = map_points[self.coords[0]][self.coords[1]]     
 
    def calcWeight(self, endNote):
        horizontalDistance  = abs(self.coords[1] - endNode.coords[1])
        verticalDistance    = abs(self.coords[0] - endNode.coords[0])
        self.weight         =  horizontalDistance + verticalDistance

    def setChildren(self):
        self.children   = []
        for node in nodes:
            if height_map[self.height] - height_map[node.height] < -1:
                #too steep
                continue
            if self.up:
                if node.coords == self.up:
                        self.children.append(node)
                        continue
            if self.down:   
                if node.coords == self.down:
                    self.children.append(node)
                    continue
            if self.left:
                if node.coords == self.left:
                    self.children.append(node)
                    continue
            if self.right:
                if node.coords == self.right:   
                    self.children.append(node)
                    continue
    def setG(self, g):
        self.g = g

        
with open('day12_input_file') as f:
    map_points = f.readlines()

coord_table = []
nodes = []
opened = []
closed = []

height_map = {
    'S'     : 1,
    'E'     : 26,
    'a'     : 1,
    'b'     : 2,
    'c'     : 3,
    'd'     : 4,
    'e'     : 5,
    'f'     : 6,
    'g'     : 7,
    'h'     : 8,
    'i'     : 9,
    'j'     : 10,
    'k'     : 11,
    'l'     : 12,
    'm'     : 13,
    'n'     : 14,
    'o'     : 15,
    'p'     : 16,
    'q'     : 17,
    'r'     : 18,
    's'     : 19,
    't'     : 20,
    'u'     : 21,
    'v'     : 22,
    'w'     : 23,
    'x'     : 24,
    'y'     : 25,
    'z'     : 26
}

y=0
finished = False

for map_row in map_points:
    x=0
    map_row = map_row.strip('\n')
    for map_point in map_row:
        coord_table.append([y,x])
        x += 1
    y += 1

for coords in coord_table:
    connected_nodes = {}
    upNode = []
    downNode = []
    leftNode = []
    rightNode = []

    upNode.append(coords[0] - 1)
    upNode.append(coords[1])
    downNode.append(coords[0] + 1)
    downNode.append(coords[1])
    leftNode.append(coords[0])
    leftNode.append(coords[1] - 1)
    rightNode.append(coords[0])
    rightNode.append(coords[1] + 1)
    if upNode[0] >= 0:
        connected_nodes['up'] = upNode
    else:
        connected_nodes['up'] = False
    if downNode[0] < len(map_points):
        connected_nodes['down'] = downNode
    else:
        connected_nodes['down'] = False
    if leftNode[1] > 0:
        connected_nodes['left'] = leftNode
    else:
        connected_nodes['left'] = False
    if rightNode[1] < len(map_points[0]):
        connected_nodes['right'] = rightNode
    else:
        connected_nodes['right'] = False
    nodes.append(mapNode(coords, connected_nodes))

# print (coord_table)
for node in nodes:
    if node.height=='S':
        startNode = node
        node.setG(0)
    if node.height=='E':
        endNode = node

for node in nodes:
    node.calcWeight(endNode)
    node.setChildren()



opened.append(startNode)

step_count = 0
while not finished:
    min_open_weight = 9999999
    step_count += 1
    for open in opened:
        full_weight = open.weight + open.g
        if full_weight <= min_open_weight:
            min_open_weight = open.weight
            selected = open
    opened.pop(opened.index(selected))
    closed.append(selected)
    for child in selected.children:
        if (child not in opened) and (child not in closed):
            child.setG(selected.g+1)
            opened.append(child)
        elif child.g > (selected.g+1):
            child.setG(selected.g+1)
            opened.append(child)
    if (selected.weight == 0):
        print ('cool!')
        print (f'path length from origin = {selected.g}')
        finished=True