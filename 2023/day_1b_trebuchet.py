f = open("input.txt", "r")
lines = f.readlines()

def get_first_digit(line):
    for i, char in enumerate(line):
        if char.isdigit():
            return i, char
    return -1, ""

def get_last_digit(line):
    for i, char in enumerate(reversed(line)):
        if char.isdigit():
            return len(line) - i - 1, char
    return -1, ""

def get_first_word(line):
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    first_encounter = {word: line.find(word) for word in number_words if word in line}
    try:
        min_key = min(first_encounter, key=lambda x: first_encounter[x])
        return first_encounter[min_key], min_key
    except ValueError:
        return -1, -1

def get_last_word(line):
    word_positions = {}
    number_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for number_word in number_words:
        if number_word in line:
            word_positions[number_word] = line.rfind(number_word)
    if word_positions:
        max_word = max(word_positions, key=lambda x: word_positions[x])
        return word_positions[max_word], max_word
    else:
        return -1, -1

def get_first_number(line):
    first_digit_index, first_digit = get_first_digit(line)
    first_word_index, first_word = get_first_word(line)
    if first_digit_index == -1:
        return convert_to_integer(first_word)
    elif first_word_index == -1:
        return first_digit
    else:
        if first_digit_index < first_word_index:
            return first_digit
        else:
            return convert_to_integer(first_word)

def get_last_number(line):
    last_digit_index, last_digit = get_last_digit(line)
    last_word_index, last_word = get_last_word(line)
    if last_digit_index == -1:
        return convert_to_integer(last_word)
    elif last_word_index == -1:
        return last_digit
    else:
        if last_digit_index > last_word_index:
            return last_digit
        else:
            return convert_to_integer(last_word)

def convert_to_integer(number):
    word_to_digit = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    return word_to_digit[number]

calibration_value = 0
for line in lines:
    first_num = str(get_first_number(line))
    last_num = str(get_last_number(line))
    two_digit_number = first_num + last_num
    calibration_value = calibration_value + int(two_digit_number)

# 53268 is right
print(f'The calibration value is {calibration_value}')
