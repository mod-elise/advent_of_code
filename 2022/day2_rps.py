import aoc_functions

wrong_map =  {
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

right_map = {
        'A X' : 3,
        'A Y' : 4,
        'A Z' : 8,
        'B X' : 1,
        'B Y' : 5,
        'B Z' : 9,
        'C X' : 2,
        'C Y' : 6,
        'C Z' : 7
}

with open('day2_input_file') as f:
    rounds = f.readlines()

print ("Wrong sum = ", str(aoc_functions.evaluate_tournament(rounds, wrong_map)))
print ("Right sum = ", str(aoc_functions.evaluate_tournament(rounds, right_map)))