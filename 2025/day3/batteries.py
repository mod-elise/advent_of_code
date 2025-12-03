with open('input.txt', 'r') as file:
    banks = file.read().splitlines()

def getHighestBattery(bank):
    largest = 0
    second_largest= 0
    i=0
    for number in bank:
        if int(number) > int(largest) and i != len(bank)-1:
            largest = number
            largest_pos = i
        i+=1

    for i in range (largest_pos+1, len(bank),1):
        if int(bank[i]) >= int(second_largest):
            second_largest = bank[i]

    return int(largest + second_largest)

sum_of_highest = 0

for bank in banks:
    sum_of_highest += getHighestBattery(bank)   

print (sum_of_highest)