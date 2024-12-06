import random

with open('input.txt') as f:
    lines = f.read().splitlines()


def check_in_order(left, right, page_order):
    try:
        first_index = page_order.index(left)
        second_index = page_order.index(right, first_index + 1)
        return True
    except:
        return False

def corrected_order(page_order, rules):
    correct_order = True
    for rule in rules:
        if rule[0] in page_order and rule[1] in page_order:
            if check_in_order(rule[0], rule[1], page_order):
                continue
            else:
                correct_order = False
                try:
                    page_order = page_order.split(',')
                except:
                    pass
                first_index = page_order.index(rule[0])
                second_index = page_order.index(rule[1])
                page_order[first_index], page_order[second_index] = page_order[second_index], page_order[first_index]
    return page_order, correct_order

def rule_check(pages, rules):
    correct_orders = []
    incorrect_orders = []
    for page_order in pages:
        pages_ordered = True
        for rule in rules:
            if rule[0] in page_order and rule[1] in page_order:
                if check_in_order(rule[0], rule[1], page_order):
                    continue
                else:
                    pages_ordered = False
                    incorrect_orders.append(page_order)
                    break
        if pages_ordered:
            correct_orders.append(page_order)
    return correct_orders,incorrect_orders

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

correct_orders, incorrect_orders = rule_check(pages, rules)
correct_order_list = [page_order.split(',') for page_order in correct_orders]

middle_numbers = []
for page in correct_order_list:
    middle_numbers.append(int(page[len(page)//2]))
print(f'Part 1: {sum(middle_numbers)}')

corrected_list = []

for fix_my_order in incorrect_orders:
    corrected = False
    while not corrected:
        fix_my_order, corrected = corrected_order(fix_my_order, rules)
    corrected_list.append(fix_my_order)

middle_numbers = []
for page in corrected_list:
    middle_numbers.append(int(page[len(page)//2]))
print(f'Part 2: {sum(middle_numbers)}')
