with open('input.txt') as f:
    contents = f.read().splitlines()
    contents = [tuple(map(int, x.split())) for x in contents]

left, right = (sorted(x) for x in zip(*contents))
print (f'The difference score is ' + str(sum([abs(x-y) for x,y in zip(left, right)])))

similarity_score = 0
for x,y in zip(left, right):
    similarity_score += x * right.count(x)

print (f'The similarity score is ' + str(similarity_score))
