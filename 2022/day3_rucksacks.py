
with open('day3_input_file') as f:
    rucksacks = f.readlines()

priority_sum = 0
for rucksack in rucksacks:
    compartment1, compartment2 = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
    comp1list, comp2list = list(compartment1), list(compartment2)
    error_item = str((set(comp1list).intersection(comp2list)))[2]
    if error_item.islower():
        
        priority_sum = priority_sum + (ord(error_item) - 96)
    else:
        priority_sum = priority_sum + (ord(error_item) - 38)

print (priority_sum)
     