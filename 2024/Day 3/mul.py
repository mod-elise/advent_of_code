import re

with open('input.txt') as f:
    contents = f.read()

#part 1
result = sum(int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", contents))
print (f'The result of part 1 is: {result}')

#part 2
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
matches = list(re.finditer(pattern, contents))
result = []
sum = 0
for match in matches:
    if match.group(1) and match.group(2):  # It's a mul(x, y)
        result.append((int(match.group(1)), int(match.group(2))))
    elif match.group(0) == 'do()':  # It's a do()
        result.append('do()')
    elif match.group(0) == "don't()":  # It's a don't()
        result.append("don't()")

enabled = True
for operation in result:
    if operation == 'do()':
        enabled = True
    elif operation == "don't()":
        enabled = False
    if enabled and operation.__class__ == tuple:
        sum += operation[0] * operation[1]
print(f'The result of part 2 is: {sum}')
