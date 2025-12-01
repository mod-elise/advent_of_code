with open('input.txt', 'r') as file:
    turns = file.read().splitlines()

dial_position = 50
zero_count = 0
zero_count_pt2 = 0

def click_dial(position, direction, steps, zero_count, zero_count_pt2):
    for i in range(steps):
        position += direction
        if position < 0:
            position = 99
        elif position > 99:
            position = 0
            zero_count_pt2 += 1
        elif position == 0:
            zero_count_pt2 += 1
    if position == 0:
        zero_count += 1
    return position, zero_count, zero_count_pt2

for turn in turns:
    if turn[0] == 'L':
        direction = -1
    else:
        direction = 1
    steps = int(turn[1:])
    dial_position, zero_count, zero_count_pt2 = click_dial(dial_position, direction, steps, zero_count, zero_count_pt2)

print(f'PART1: Zero was hit {zero_count} times.')
print(f'PART2: Zero was crossed {zero_count_pt2} times.')