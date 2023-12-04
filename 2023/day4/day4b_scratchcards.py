import re

f = open("input.txt", "r")
lines = f.readlines()

total_points = 0
scratchcards = {}
extra_scratchcards = []
mega_scratchcards = []
full_scratchcard_dict = {}

def format_array(array):
    return [int(item.strip('\n')) for item in array if item != '']

def count_winners(winning_numbers, have_numbers):
    winners = 0
    for number in have_numbers:
        if number in winning_numbers:
            winners += 1
    return winners

for scratchcard in lines:
    full_scratchcard = (scratchcard.split(': '))
    winners_and_haves = full_scratchcard[1].split('|')
    winners = format_array(winners_and_haves[0].split())
    haves = format_array(winners_and_haves[1].split())
    full_scratchcard[1] = winners
    full_scratchcard.append(haves)
    index = full_scratchcard[0]
    index = re.sub(r'\s+', ' ', index)
    mega_scratchcards.append(index)
    full_scratchcard_dict[index] = full_scratchcard[1:]

extra_scratchcards = mega_scratchcards
counter = len(extra_scratchcards)
while extra_scratchcards != []:
    for scratchcard in extra_scratchcards:
        if len(mega_scratchcards)  % 100000 == 0:
            print (len(mega_scratchcards))
        card_points = 0
        winner_count = 0
        extra_scratchcards = []
        card_number = re.findall(r'\d+', scratchcard)[0]
        winners = full_scratchcard_dict[scratchcard][0]
        haves = full_scratchcard_dict[scratchcard][1]
        winner_count = count_winners(winners, haves)
        if winner_count > 0:
            for i in range(int(card_number)+1, int(card_number)+winner_count+1):
                extra_scratchcards.append(f'Card {i}')
                mega_scratchcards.append(f'Card {i}')

print (f'The final answer is {len(mega_scratchcards)}')
