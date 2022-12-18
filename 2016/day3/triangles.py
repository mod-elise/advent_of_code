with open('day3_input_file') as f:
    triangles = f.readlines()

def isTriangle (s1,s2,s3):
    if (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
        return True 

validCount = 0
invalidCount = 0 
for triangle in triangles:
    side_list = [int(x) for x in triangle.split()]
    if isTriangle(side_list[0], side_list[1], side_list[2]):
        validCount += 1
    else:
        invalidCount += 1

print (f'pt 1 valid: {validCount}')
print (f'pt 1 invalid: {invalidCount}')
print()
left_triangles = []
middle_triangles = []
right_triangles = []

for triangle in triangles:
    triangle = triangle.lstrip()
    triangle_ints = [int(x) for x in triangle.split()]
    left_triangles.append(triangle_ints[0])
    middle_triangles.append(triangle_ints[1])
    right_triangles.append(triangle_ints[2])

validCount = 0
for r in range(0, len(triangles),3):
    if isTriangle(left_triangles[r], left_triangles[r+1], left_triangles[r+2]):
        validCount += 1
    if isTriangle(middle_triangles[r], middle_triangles[r+1], middle_triangles[r+2]):
        validCount += 1
    if isTriangle(right_triangles[r], right_triangles[r+1], right_triangles[r+2]):
        validCount += 1

print (f'Counting columns valid triangles is {validCount}')
