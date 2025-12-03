try:
    with open('input.txt', 'r') as file:
        print ("found file")
        banks = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded ranges")
        banks = ["987654321111111", "811111111111119", "234234234234278", "818181911112111"]

def getHighestBattery(bank, largest_pos, batteries_left):
    largest = 0
    i=0
    for i in range (largest_pos, len(bank)-batteries_left,1):
        if int(bank[i]) > int(largest):
            largest = bank[i]
            largest_pos = i
        i+=1
    return largest, largest_pos

number_of_batteries = [2,12] 

for battery_quantity in number_of_batteries:
    joltage_list = []
    for bank in banks:
        joltage = ''
        last_pos = -1
        for j in range (1, battery_quantity+1, 1):
            batteries_left = battery_quantity - j + 1
            battery, last_pos = getHighestBattery(bank, last_pos+1, batteries_left-1)
            joltage = joltage + battery
        joltage_list.append(int(joltage))

    print (f'sum of all joltages for {battery_quantity} batteries: {sum(joltage_list)}')