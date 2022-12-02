def evaluate_round (round):
    res_map = {
        'A X' : 4,
        'A Y' : 8,
        'A Z' : 3,
        'B X' : 1,
        'B Y' : 5,
        'B Z' : 9,
        'C X' : 7,
        'C Y' : 2,
        'C Z' : 6
    }
    return res_map[round]

with open('day2_input_file') as f:
    rounds = f.readlines()

total_sum = 0
for round in rounds:
    total_sum = total_sum +  evaluate_round(round.rstrip('\n'))

print (total_sum)