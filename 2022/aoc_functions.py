def create_list_of_sums (calories):
    cal_sum = 0
    calorie_sums = []
    for calorie in calories:
        if calorie != '\n':
            cal_sum += int(calorie)
        else:
            calorie_sums.append(cal_sum)
            cal_sum = 0
    return calorie_sums

def evaluate_tournament (rounds,map):
    total_sum = 0
    for round in rounds:
        total_sum += map[round.rstrip('\n')]
    return total_sum

def sum_duplicate_priorities(rucksacks):
    priority_sum = 0
    for rucksack in rucksacks:
        compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        comp1list, comp2list = list(compartment1), list(compartment2)
        error_item = str((set(comp1list).intersection(comp2list)))[2]
        priority_sum += get_priority(error_item)
    return priority_sum

def get_priority(error_item):
    if error_item.islower():
        priority = (ord(error_item) - 96)
    else:
        priority = (ord(error_item) - 38)
    return (priority)

def get_duplicate(elf_group):
    elf_1_sack  = list(elf_group[0])
    elf_2_sack  = list(elf_group[1])
    elf_3_sack  = list(elf_group[2])

    for item in elf_1_sack:
        if (item in elf_2_sack and item in elf_3_sack):
            return item