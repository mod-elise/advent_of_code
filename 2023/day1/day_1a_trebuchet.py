f = open("input.txt", "r")
lines = f.readlines()

def get_number (line):
    number = ""
    for char in line:
        if char.isdigit():
            number += char
    number = number[0] + number[len(number) - 1]
    return int(number)

calibration_value = 0
for line in lines:
    calibration_value = calibration_value + get_number(line)

print(calibration_value)
