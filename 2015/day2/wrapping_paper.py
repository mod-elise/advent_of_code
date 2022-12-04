with open('day2_input_file') as f:
    presents = f.readlines()

def parse_dimensions(present):
    return (present.split('x'))

def calc_area (dimension_list):
    area1 = (dimension_list[0]) * (dimension_list[1])
    area2 = (dimension_list[1]) * (dimension_list[2])
    area3 = (dimension_list[0]) * (dimension_list[2])
    area_list = [area1, area2, area3]
    return ((2 * sum(area_list)) + (min(area_list)))

def calc_ribbon (dimension_list):
    dimension_list.sort()
    ribbon = (2*(dimension_list[0])) + (2*(dimension_list[1]))
    bow = (dimension_list[0]) * (dimension_list[1] * (dimension_list[2]))
    return (ribbon + bow)

total_area = 0
total_ribbon = 0
for present in presents:
    dimension_list = parse_dimensions(present.rstrip('\n'))
    dimension_list = list(map(int, dimension_list))
    total_area += calc_area(dimension_list)
    total_ribbon += calc_ribbon(dimension_list)

print (total_area)
print (total_ribbon)