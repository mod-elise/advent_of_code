import random

# read a file into a variable until a new line is reached then read the rest into another variable
with open('test.txt') as f:
    lines = f.read().splitlines()


def check_in_order(left, right, page_order):
    try:
        first_index = page_order.index(left)
        second_index = page_order.index(right, first_index + 1)
        return True
    except:
        return False

def bogo_fix(page_order):
    #this is a meme don't worry about it
    page_order=page_order.split(',')
    random.shuffle(page_order)
    page_order = ','.join(page_order)
    for rule in rules:
        pages_ordered = True
        if rule[0] in page_order and rule[1] in page_order:
            if check_in_order(rule[0], rule[1], page_order):
                continue
            else:
                pages_ordered = False
                break
    return page_order, pages_ordered



rules = []
pages = []

change = False
for line in lines:
    if not change:
        if line == '':
            change = True
        else:
            rules.append(line)
    else:
        pages.append(line)


rules = [tuple(rule.split('|')) for rule in rules]
correct_order = []
incorrect_orders = []

for page_order in pages:
    pages_ordered = True
    for rules_idx,rule in enumerate(rules):
        if rule[0] in page_order and rule[1] in page_order:
            if check_in_order(rule[0], rule[1], page_order):
                continue
            else:
                pages_ordered = False
                incorrect_orders.append(page_order)
                break
    if pages_ordered:
        correct_order.append(page_order)

correct_order_list = [page_order.split(',') for page_order in correct_order]

middle_numbers = []
for page in correct_order_list:
    middle_numbers.append(int(page[len(page)//2]))
print(f'Part 1: {sum(middle_numbers)}')
