with open("input.txt") as f:
    int_array = f.read()
int_array = [int(x) for x in int_array.split(',')]
step=4

def main (input_array, noun, verb):
    for i in range(0, len(input_array), step):
        input_array[1] = noun
        input_array[2] = verb
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
    return input_array[0]

#part 1
print(f'Part 1 answer: {main(int_array.copy(),12,2)}')

#part 2
for noun in range(100):
    for verb in range(100):
        if main(int_array.copy(),noun,verb) == 19690720:
            print(f'Part 2 answer: {100 * noun + verb}')
            exit()