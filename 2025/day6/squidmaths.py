try:
    with open('input.txt', 'r') as file:
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
     
def rightmost_problems_width(sheet):
    max_width = 0
    for row in sheet:
        if row[len(row)-1].isnumeric():
            character = '*'
            column_width = 1
            while character != " ":
                column_width +=1
                try:
                    character = row[len(row)-column_width]
                except:
                    character = " "
            if column_width > max_width:
                max_width = column_width
    return max_width -1

def construct_squid_numbers(numbers, column_width):
    constructed_numbers = []
    numbers_to_calc = []
    for number in numbers:
        final_column = number[-1:]
        if final_column.isnumeric():
            numbers_to_calc.append(final_column)
    constructed_numbers.append(''.join(numbers_to_calc))
    
    for i in range (2, column_width+1,1):
        numbers_to_calc= []
        for number in numbers:
            final_column = number[-i:-(i-1)]
            if final_column.isnumeric():
                numbers_to_calc.append(final_column)
        constructed_numbers.append(''.join(numbers_to_calc))
    return constructed_numbers

def squid_calc(constructed_numbers, operator):
    if operator == '+':
        solution = 0
        for number in constructed_numbers:
            solution += int(number)
    if operator == '*':
        solution = 1
        for number in constructed_numbers:
            solution *= int(number)
    return solution
# ____________________________________________________________________________________________________


maths_roll = make_horizontal(sheet)
problems =  make_vertical(maths_roll)

# print (problems)
print (f'solution to part 1 is {solve_problems(problems)}')

print ("---part 2 incomplete ---")

sheet_length = len(sheet[0])

grand_total = 0
while sheet_length > 1:
    updated_sheet = []
    rightmost_problems = []
    column_width = rightmost_problems_width(sheet)
    for row in sheet:
        rightmost_problems.append(row[len(row)-column_width:])  

    operator = rightmost_problems[-1].strip()
    numbers = rightmost_problems[:-1]

    constructed_numbers = construct_squid_numbers(numbers, column_width)
    constructed_numbers = [x for x in constructed_numbers if x]
    solution = squid_calc(constructed_numbers, operator)
    grand_total += solution

    for row in sheet:
        updated_sheet.append(row[:-column_width-1])
    sheet = updated_sheet
    sheet_length = len(sheet[0])

print (f'the grand total is {grand_total}')