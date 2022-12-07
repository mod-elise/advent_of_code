with open('day3_input_file') as f:
    triangles = f.readlines()

validCount = 0
invalidCount = 0 
for triangle in triangles:
    side_list = [int(x) for x in triangle.split()]
    if ((side_list[0] + side_list[1]) > side_list[2]
    and (side_list[1] + side_list[2]) > side_list[0]
    and (side_list[0] + side_list[2]) > side_list[1]
    ):
        validCount += 1
    else:
        invalidCount += 1

print (validCount)
print (invalidCount)