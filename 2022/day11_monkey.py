import math

def generateStartingList(line_components):
    item_array = []
    for r in range (2, len(line_components),1):
        item_array.append(line_components[r].strip(','))
    return item_array

with open('day11_input_file') as f:
    monkey_scripts = f.readlines()


monkeys             = {}
monkey_num          = 999999
monkey_symbol       = '<'
monkey_opp_value    = -99
monkey_divisor_test = 999
monkey_true         = 999
monkey_false        = 999
monkey_items        = []
monkey_passes       = [0,0,0,0,0,0,0,0]
common_demonkinator = 1
part1               = False

#note to self - never parse like this again
for monkey_script in monkey_scripts:
    line_components = monkey_script.strip()
    try: 
        line_components[1]
    except:
        continue
    line_components = line_components.split()
    if line_components[0] == 'Monkey':
        monkey_num = int(line_components[1].strip(':'))
    if (line_components[0] == 'Starting'):
        monkey_items = generateStartingList(line_components)
    if line_components[0] == 'Operation:':
        monkey_symbol       = line_components[len(line_components)-2]
        monkey_opp_value    = line_components[len(line_components)-1] 
    if line_components[0] == 'Test:':
        monkey_divisor_test = line_components[3]
        common_demonkinator *= int(monkey_divisor_test)
    if line_components[1] == 'true:':
        monkey_true = line_components[5]
    if line_components[1] == 'false:':
        monkey_false = line_components[5]

    monkeys[monkey_num] = {
        'Items'         :   monkey_items,
        'Operation'     :   [monkey_symbol, monkey_opp_value],
        'Test'          :   int(monkey_divisor_test),
        'ifTrue'        :   int(monkey_true),
        'ifFalse'       :   int(monkey_false)
    }

for i in range (0, 10000, 1):
    print (f'*********************{i}*******************')
    for monkey in monkeys:
        monkey_true = monkeys[monkey]['ifTrue']
        monkey_false = monkeys[monkey]['ifFalse']
        item_num=0
        items = monkeys[monkey]['Items'].copy()
        for item in items:
            if monkeys[monkey]['Operation'][1] == 'old':
                worrier = (item)
            else:
                worrier = monkeys[monkey]['Operation'][1]
            if monkeys[monkey]['Operation'][0]== '*':
                new_worry = (int(item) * int(worrier))
            if monkeys[monkey]['Operation'][0]== '+':
                new_worry = (int(item) + int(worrier))
            if part1:
                new_worry = new_worry // 3
            if new_worry % monkeys[monkey]['Test'] == 0:
                monkey_passes[monkey] += 1
                monkeys[monkey_true]['Items'].append(new_worry)
            else:
                monkey_passes[monkey] += 1
                new_worry = new_worry % common_demonkinator
                monkeys[monkey_false]['Items'].append(new_worry)
            monkeys[monkey]['Items'].pop(0)

monkey_passes.sort(reverse=True)
print(f'Monkey business is {monkey_passes[0] * monkey_passes[1]}')