with open("input.txt") as f:
    int_array = f.read()
int_array = [int(x) for x in int_array.split(',')]
step=4
int_array[1] = 12
int_array[2] = 2


def function1 (input_array):
    for i in range(0, len(input_array), step):
        if input_array[i] == 99:
            break
        opcode = input_array[i]
        param1 = input_array[i+1]
        param2 = input_array[i+2]
        target = input_array[i+3]
        if opcode == 1:
            input_array[target] = input_array[param1] + input_array[param2]
        elif opcode == 2:
            input_array[target] = input_array[param1] * input_array[param2]
        else:
            print(f"Unknown opcode {opcode} at position {i}")
    return int_array[0]

print(function1(int_array))