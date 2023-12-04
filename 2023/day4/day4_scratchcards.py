f = open("input.txt", "r")
lines = f.readlines()

total_points = 0
scratchcards = {}

for scratchcard in lines:
    card_points = 0
    winners = 0
    full_scratchcard = (scratchcard.split(': '))
    all_numbers = full_scratchcard[1].split('|')
    winning_numbers = all_numbers[0].split(' ')
    winning_numbers = [int(item) for item in winning_numbers if item != '']
    # print (winning_numbers)
    have_numbers = all_numbers[1].split(' ')
    have_numbers = [int(item.strip('\n')) for item in have_numbers if item != '']
    # print (have_numbers)
    # print (winning_numbers)
    for number in have_numbers:
        if number in winning_numbers:
            winners += 1

    if winners > 0:
        for i in range(1, winners+1):
            # print (i)
            if i == 1:
                card_points = 1
            else:
                card_points = card_points * 2
                # print (f'running card points {card_points}')
    # print (card_points)
    total_points += card_points

print (total_points)
