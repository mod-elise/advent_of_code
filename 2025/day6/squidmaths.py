import re

try:
    with open('1input.txt', 'r') as file:
        print ("found file")
        sheet = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded ranges")
        sheet = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +""".strip().splitlines()

def make_horizontal(sheet, part=1):
    horizontal_lists = []    
    for row in sheet:
        if part==1:   
            horizontal_lists.append(row.split())
        if part==2:
            horizontal_lists.append(row)
    return horizontal_lists

def make_vertical(sheet):
    vertical_lists = []
    for i in range (0, len(sheet[0])):
        column = []
        for j in range (0, len(sheet)):
            column.append(sheet [j][i])
        vertical_lists.append(column)
    return vertical_lists
        
def get_nums_and_ops(problem):
    numbers = problem[:-1]
    operator = problem[-1]
    return numbers, operator

def solve_problems(problems):
    total = 0
    for problem in problems:
        numbers, operator = get_nums_and_ops(problem)
        if operator == '+':
            solution = 0
            for number in numbers:
                solution += int(number)
        if operator == '*':
            solution = 1
            for number in numbers:
                solution *= int(number)
        total += solution
    return total
     
def findLongestNumber(problem):
    longest_number = 0
    for number in problem[:-1]:
        if len(number) > longest_number:
            longest_number = len(number) 
    return longest_number

def squidify(problems):
    exit()

maths_roll = make_horizontal(sheet)
problems =  make_vertical(maths_roll)

# print (problems)
print (f'solution to part 1 is {solve_problems(problems)}')

print ("---part 2 incomplete ---")

rightmost_problems = []

for row in sheet:
    if row[len(row)-1].isnumeric():
        character = '*'
        column_width = 1
        while character != " ":
            column_width +=1
            character = row[len(row)-column_width]
        print (f'longest number is {column_width-1} digits long')

for row in sheet:
    rightmost_problems.append(row[len(row)-column_width:])  

operator = rightmost_problems[-1].strip()
numbers = rightmost_problems[:-1]
numbers_to_calc = []

constructed_numbers = []

numbers_to_calc = []
for number in numbers:
    final_column = number[-1:]
    if final_column.isnumeric():
        numbers_to_calc.append(final_column)

constructed_numbers.append(''.join(numbers_to_calc))
numbers_to_calc= []
for number in numbers:
    final_column = number[-2:-1]
    if final_column.isnumeric():
        numbers_to_calc.append(final_column)

constructed_numbers.append(''.join(numbers_to_calc))
numbers_to_calc= []
for number in numbers:
    final_column = number[-3:-2]
    if final_column.isnumeric():
        numbers_to_calc.append(final_column)
constructed_numbers.append(''.join(numbers_to_calc))

print (f'squid numbers are {constructed_numbers}')

if operator == '+':
    solution = 0
    for number in constructed_numbers:
        solution += int(number)

print (f'the answer to the right most column is {solution}')