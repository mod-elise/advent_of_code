import itertools as it

running_total_a = 0
running_total_b = 0

with open("input.txt") as f:
    for line in f:
        nums = list(map(int, line.split()))
        running_total_a += max(nums) - min(nums)
        for a, b in it.combinations(nums, 2):
            if a % b == 0:
                running_total_b += a // b
                break
            elif b % a == 0:
                running_total_b += b // a
                break

print(f'The result of part 1 is: {running_total_a}')
print(f'The result of part 2 is: {running_total_b}')
