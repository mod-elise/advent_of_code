
def create_list_of_sums (calories):
    cal_sum = 0
    calorie_sums = []
    for calorie in calories:
        if calorie != '\n':
            cal_sum = cal_sum + int(calorie)
        else:
            calorie_sums.append(cal_sum)
            cal_sum = 0
    return calorie_sums


with open('day1_input_file') as f:
    calories = f.readlines()

calorie_sum_list = create_list_of_sums(calories)
print (max(calorie_sum_list))
