import aoc_functions

with open('day1_input_file') as f:
    calories = f.readlines()

calorie_sum_list = aoc_functions.create_list_of_sums(calories)
calorie_sum_list.sort(reverse=True)

print ("Total carried by snackiest elf: " + str(max(calorie_sum_list)))
top3_list = calorie_sum_list[0:3]
print ("The total carried by the top 3 elves: " + str(sum(top3_list)))