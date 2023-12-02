f = open("input.txt", "r")
games = f.readlines()

bag_contains = {
    "red": 12,
    "green": 13,
    "blue": 14
}
running_sum_possible = 0
total_power = 0


def calc_power(rounds):
    power = 1
    max_colours = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for round in rounds:
        colours = round.split(",")
        for colour_quant in colours:
            quantity, colour = colour_quant.split()
            quantity = int(quantity)
            if quantity > max_colours[colour]:
                max_colours[colour] = quantity
    for colour in max_colours:
        power *= max_colours[colour]
    return power

def check_possible(rounds):
    possible = True
    for round in rounds:
        colours = round.split(",")
        for colour_quant in colours:
            quantity, colour = colour_quant.split()
            quantity = int(quantity)
            if quantity > bag_contains[colour]:
                possible = False
    return possible

for game in games:
    game_id_index = game.find(":")
    game_substr = game[:game_id_index]
    rounds = game[game_id_index+1:]
    rounds = rounds.split(";")
    try:
        game_id = int(game_substr.replace("Game ", ""))
    except:
        exit ("End of file")

    power = calc_power(rounds)
    possible = check_possible(rounds)
    if possible:
        running_sum_possible += game_id
    total_power += power

print (f'The sum of all possible games is {running_sum_possible}')
print (f'The total power of all games is {total_power}')
