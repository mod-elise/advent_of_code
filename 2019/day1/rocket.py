input = 100756

def fuel_required(mass):
    return mass // 3 - 2

with open('input.txt') as f:
    mass_totals = f.read().splitlines()

total_fuel = 0

#  part 1
for mass in mass_totals:
    total_fuel += fuel_required(int(mass))
print(f'Part 1 total_fuel: {total_fuel}')

# part 2
total_fuel = 0

for mass in mass_totals:
    fuel_list = []
    fuel_list.append(fuel_required(int(mass)))
    while fuel_list[-1] > 0:
        additional_fuel = fuel_required(fuel_list[-1])
        if additional_fuel > 0:
            fuel_list.append(additional_fuel)
        else:
            break
    total_fuel+= sum(fuel_list)
print(f'Part 2 total_fuel: {total_fuel}')