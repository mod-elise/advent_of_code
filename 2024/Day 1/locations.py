with open('input.txt') as f:
    contents = f.read().splitlines()
    contents = [tuple(map(int, x.split())) for x in contents]

left, right = (sorted(x) for x in zip(*contents))
print (sum([abs(x-y) for x,y in zip(left, right)]))
