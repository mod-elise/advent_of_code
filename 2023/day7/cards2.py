import math
import time
from collections import Counter



def score_hand(hand):
    score = 0
    value = 0
    for i, card in enumerate(hand):
        if card == "A":
            value = 14
        elif card == "K":
            value = 13
        elif card == "Q":
            value = 12
        elif card == "J":
            value = 0
        elif card == "T":
            value = 10
        else:
            value = int(card)
        score+= math.pow(15,(5-(i+1))) * value
    return score

def get_highest_card(highest_cards):
    highest_card = ['E', 0]

    for card in highest_cards:
        if card =="J":
            continue
        if card == "A":
            value = 14
        elif card == "K":
            value = 13
        elif card == "Q":
            value = 12
        elif card == "T":
            value = 10
        else:
            value = int(card)
        if value > highest_card[1]:
            highest_card = [card, value]
    if highest_card[1] == 0:
        highest_card = ['A', 14]
    return highest_card[0]

def categorise_hand (hand_obj):
    pair_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    for hand in hand_obj["card_count"]:
        if hand_obj["card_count"][hand] == 2:
            pair_count += 1
        if hand_obj["card_count"][hand] == 3:
            three_count += 1
        if hand_obj["card_count"][hand] == 4:
            four_count += 1
        if hand_obj["card_count"][hand] == 5:
            five_count += 1
    if pair_count == 1:
        if three_count == 1:
            hand_obj["category"] = "Full House"
            hand_obj["score"] = (math.pow(15, 5) * 5) + score_hand(hand_obj["unwildcarded"])
        else:
            hand_obj["category"] = "One Pair"
            hand_obj["score"] = (math.pow(15, 5) * 2) + score_hand(hand_obj["unwildcarded"])
    elif pair_count == 2:
        hand_obj["category"] = "Two Pairs"
        # print (f'{hand_obj["cards"]}, ')
        hand_obj["score"] = (math.pow(15, 5) * 3) + score_hand(hand_obj["unwildcarded"])
    elif three_count == 1:
        hand_obj["category"] = "Three of a Kind"
        hand_obj["score"] = (math.pow(15, 5) * 4)+ score_hand(hand_obj["unwildcarded"])
    elif four_count == 1:
        hand_obj["category"] = "Four of a Kind"
        hand_obj["score"] = (math.pow(15, 5) * 6) + score_hand(hand_obj["unwildcarded"])
    elif five_count == 1:
        hand_obj["category"] = "Five of a Kind"
        hand_obj["score"] = (math.pow(15, 5) * 7) + score_hand(hand_obj["unwildcarded"])
    else:
        hand_obj["category"] = "High Card"
        hand_obj["score"] = math.pow(15, 5) + score_hand(hand_obj["unwildcarded"])

    return hand_obj


start_time = time.time()
f = open("input.txt", "r")
hands = f.readlines()
hand_objs = []
running_score = 0

for hand_details in hands:
    hand_details = hand_details.split()

    card_count = Counter(card for card in hand_details[0] if card != 'J')
    try:
        highest_count = card_count.most_common(1)[0][1]
        highest_cards = [card for card, count in card_count.items() if count == highest_count and card != 'J']
    except:
        highest_cards = ['J']

    wildcarded_hand = hand_details[0].replace("J",get_highest_card(highest_cards))
    card_count = Counter(wildcarded_hand)

    hand_obj = {
        "raw" : hand_details,
        "unwildcarded" : hand_details[0],
        "cards" : wildcarded_hand,
        "bid" : int(hand_details[1]),
        "card_count" : card_count
    }
    hand_objs.append(hand_obj)

for i, hand_obj in enumerate(hand_objs):
    hand_objs[i] = categorise_hand(hand_obj)


sorted_hand_objs = sorted(hand_objs, key=lambda x: x["score"], reverse=False)




for i in range(0, len(sorted_hand_objs)):
    # print (sorted_hand_objs[i]["category"], sorted_hand_objs[i]["score"], sorted_hand_objs[i]["cards"], sorted_hand_objs[i]["unwildcarded"], (i+1) * sorted_hand_objs[i]["bid"])
    running_score += (i+1) * sorted_hand_objs[i]["bid"]

print (running_score)
