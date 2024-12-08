import itertools
import time
from multiprocessing import Pool
from functools import lru_cache

with open('input.txt') as f:
    lines = f.read().splitlines()


@lru_cache(maxsize=5000)
def perform_operation (operator, num1, num2):
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    elif operator == 'C':
        result = int(str(num1) + str(num2))

    return result

def is_Valid (value,  numbers, operator_combos):
    for operator_combo in operator_combos:
        left = numbers[0]
        for operator, num in zip(operator_combo, numbers[1:]):
            left = perform_operation(operator, left, num)
            if left > value:
                break
            else:
                if left == value:
                  return True
    return False

def calibrate(callibration_list, operators):
    total = 0
    operator_combos = {i: list(itertools.product(operators, repeat=i)) for i in range(11)}

    for callibration in callibration_list:
        total_operators = len(callibration['numbers']) - 1
        sorted_combinations = operator_combos.get(total_operators,
                                                  list(itertools.product(operators, repeat=total_operators)))
        is_calibration_valid = is_Valid(callibration['value'], callibration['numbers'], sorted_combinations)
        if is_calibration_valid:
            total += callibration['value']
    return total

callibration_list = []
for line in lines:
    line = line.split(':')
    callibration_data = {
        'value': int(line[0]),
        'numbers': [int(x) for x in line[1].split()]
    }
    callibration_list.append(callibration_data)

#calcuate time it takes to complete
start_time = time.time()
operators = ['+', '*']
part1_answer = calibrate(callibration_list, operators)
print (f'Part 1: {part1_answer}')
print ("--- %s seconds ---" % (time.time() - start_time)) # 0.5 seconds on my machine
start_time = time.time()
operators = ['+', '*', 'C']
total = 0
part2_answer = calibrate(callibration_list, operators)
print (f'Part 2: {part2_answer}')
print ("--- %s seconds ---" % (time.time() - start_time)) # 36 seconds on my machine
