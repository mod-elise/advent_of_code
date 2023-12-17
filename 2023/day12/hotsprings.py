from itertools import product
import re

def generate_strings(s):
    possible_chars = ['.', '#']
    possible_combinations = product(possible_chars, repeat=s.count('?'))
    results = []

    for combination in possible_combinations:
        new_string = s.replace('?', '{}').format(*combination)
        results.append(new_string)

    return results

def get_group_sizes(s):
    pattern = r'#+'
    matches = re.findall(pattern, s)
    sizes = [str(len(match)) for match in matches]
    return ','.join(sizes)


f = open("input.txt", "r")
spring_lines = f.readlines()


split_lines = []

for spring_line in spring_lines:
    spring_line = spring_line.strip()
    spring_line = spring_line.split(" ")
    split_lines.append (spring_line)


sum = 0
for i, split_line in enumerate(split_lines):
    print (f'{i} of  {len(split_lines)}', end='\r')
    possibilities = generate_strings(split_line[0])
    for possibility in possibilities:
        group_sizes = get_group_sizes(possibility)
        if group_sizes == split_line[1]:
            sum += 1

print ('                                    ')
print (sum)
