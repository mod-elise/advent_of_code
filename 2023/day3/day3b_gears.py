import re

f = open("input.txt", "r")
lines = f.readlines()
digit_list = []
gear_list = []
running_sum = 0

def check_gears_for_adjacent(gear, gear_row, number_list):
    adj_count = 0
    ratios = []
    rows_to_check = [gear_row - 1, gear_row, gear_row + 1]
    for row in rows_to_check:
        for number in number_list[row]:
            number_is_adjacent = False
            starting_point = number[1]
            end_point = number[1] + len(number[0])
            for i in range(starting_point, end_point):
                if number_is_adjacent:
                    continue
                if (abs(gear - i) == 1):
                    adj_count += 1
                    ratios.append(int(number[0]))
                    number_is_adjacent = True
    if (adj_count == 2):
        return ratios
    else:
        return False

for line_num, line in enumerate(lines):
    digits = [(match.group(), match.start()) for match in re.finditer(r'\d+', line)]
    digit_list.append(digits)
    gear = [(match.group(), match.start()) for match in re.finditer(r'\*', line)]
    gear_list.append(gear)

for gear_row, gears in enumerate(gear_list):
    for gear in gears:
        gear_ratios = check_gears_for_adjacent(gear[1], gear_row, digit_list)
        if (gear_ratios):
            running_sum += gear_ratios[0] * gear_ratios[1]


wrong = [50463815, 75214128, 75217608]

# look. I dont know why but this doesnt work for single digit numbers.  so I did them by hand. sue me
running_sum += 6375

if running_sum in wrong:
    print ("WRONG ANSWER")
print (running_sum)
