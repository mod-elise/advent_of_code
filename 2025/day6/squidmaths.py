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

def make_horizontal(sheet):
    horizontal_lists = []    
    for row in sheet:   
        horizontal_lists.append(row.split())
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

# print (sheet)
sheet = make_horizontal(sheet)
# print (sheet)
# exit()
problems =  make_vertical(sheet)
# squid_problems = squidify(problems)

# print (problems)
print (f'solution to part 1 is {solve_problems(problems)}')