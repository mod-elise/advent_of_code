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
        print (f'longest number is {column_width-1}')

for row in sheet:
    rightmost_problems.append(row[len(row)-column_width:])  

operator = rightmost_problems[-1].strip()
numbers = rightmost_problems[:-1]
print (f'numbers are {numbers}')
print (f'operator is {operator}')
numbers_to_calc = []


for number in numbers:
    print (f'The number is: {number}')
    final_column = number[-1:]
    if final_column.isnumeric():
        numbers_to_calc.append(int(final_column))


if operator == '+':
    result = sum(numbers_to_calc)
if operator == '*':
    result = 1
    for num in numbers_to_calc:
        result *= num

print (result)

print (rightmost_problems)