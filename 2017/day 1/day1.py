with open("input.txt") as f:
    line = f.read().strip()
    summation = sum(int(a) for a, b in zip(line, line[1:] + line[0]) if a == b)
    summation2 = sum(int(a) for a, b in zip(line, line[len(line) // 2:] + line[:len(line) // 2]) if a == b)
print(f'The result of part 1 is: {summation}')
print(f'The result of part 2 is: {summation2}')
