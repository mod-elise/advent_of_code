with open("input.txt") as f:
    int_array = f.read()
int_array = [int(x) for x in int_array.split(',')]
step=4
int_array[1] = 12
int_array[2] = 2

for i in range(0, len(int_array), step):
    if int_array[i] == 99:
        break
    opcode = int_array[i]
    param1 = int_array[i+1]
    param2 = int_array[i+2]
    target = int_array[i+3]
    if opcode == 1:
        int_array[target] = int_array[param1] + int_array[param2]
    elif opcode == 2:
        int_array[target] = int_array[param1] * int_array[param2]
    else:
        print(f"Unknown opcode {opcode} at position {i}")
    
print (int_array[0])