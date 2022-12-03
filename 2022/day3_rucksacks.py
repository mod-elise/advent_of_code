import aoc_functions

with open('day3_input_file') as f:
    rucksacks = f.readlines()
print (aoc_functions.sum_duplicate_priorities(rucksacks))

elf_group =[]
priority_sum = 0
for rucksack in rucksacks:
    if (rucksacks.index(rucksack)+1) % 3 != 0:
        elf_group.append(rucksack)
    else:
        elf_group.append(rucksack)
        badge=aoc_functions.get_duplicate(elf_group)
        priority_sum = priority_sum + aoc_functions.get_priority(badge)
        elf_group = []

print (priority_sum)