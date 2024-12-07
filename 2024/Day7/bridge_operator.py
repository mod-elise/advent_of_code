import itertools
import time
with open('input.txt') as f:
    lines = f.read().splitlines()

def perform_operation (operator, num1, num2):
    if operator == '+':
        return int(num1) + int(num2)
    elif operator == '*':
        return int(num1) * int(num2)
    elif operator == 'C':
        return num1 + num2

def is_Valid (value,  numbers, operator_combos):

    for operator_combo in operator_combos:
        left = (numbers[0])
        for idx, operator in enumerate(operator_combo):
            left = str(perform_operation(operator, left, (numbers[idx+1])))
        if int(left) == value:
            return True
    return False

def calibrate (callibration_list, operators):
    total = 0
    for callibration in callibration_list:
        total_operators = len(callibration['numbers']) -1
        combinations = list(itertools.product(operators, repeat=total_operators))
        if is_Valid(callibration['value'], callibration['numbers'], combinations):
            total += callibration['value']
    return total

callibration_list = []
for line in lines:
    line = line.split(':')
    callibration_data = {
        'value': int(line[0]),
        'numbers': line[1].split()
    }
    callibration_list.append(callibration_data)

#calcuate time it takes to complete
start_time = time.time()
operators = ['+', '*']
print (f'Part 1: {calibrate(callibration_list, operators)}')
print ("--- %s seconds ---" % (time.time() - start_time)) # 2 seconds on my machine

start_time = time.time()
operators = ['+', '*', 'C']
total = 0
print (f'Part 2: {calibrate(callibration_list, operators)}')
print ("--- %s seconds ---" % (time.time() - start_time)) # 75 seconds on my machine
