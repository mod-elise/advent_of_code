import string

f = open("input.txt", "r")
lines = f.readlines()


def is_symbol(char):
    return char in string.punctuation and char != '.'

def is_symbol_adjacent(xcoord, ycoord):
    try:
        if is_symbol(lines[ycoord][xcoord - 1]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord][xcoord + 1]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord - 1][xcoord]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord + 1][xcoord]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord + 1][xcoord]):
            return True
    except:
        pass # index out of bounds

    #diagonals
    try:
        if is_symbol(lines[ycoord + 1][xcoord + 1]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord + 1][xcoord - 1]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord - 1][xcoord + 1]):
            return True
    except:
        pass # index out of bounds
    try:
        if is_symbol(lines[ycoord - 1][xcoord - 1]):
            return True
    except:
        pass # index out of bounds
    return False



def reconstruct_number(xcoord, line):
    number = ''
    start_c= xcoord
    end_c = xcoord

    # Iterate over the characters to the left of the given position
    index = xcoord - 1
    while index >= 0 and line[index].isdigit():
        start_c = index
        index -= 1
     # Iterate over the characters to the right of the given position
    index = xcoord + 1
    while index < len(line) and line[index].isdigit():
        end_c = index
        index += 1

    number = line[start_c:end_c + 1]
    return int(number), end_c +1

running_sum = 0
for ycoord, line in enumerate(lines):
    xcoord = 0
    while xcoord < len(line):
        char = line[xcoord]
        if char.isdigit():
            if is_symbol_adjacent(xcoord, ycoord):
                full_number, xcoord = reconstruct_number(xcoord, line)
                running_sum += full_number
            else:
                xcoord += 1
        else:
            xcoord += 1


print (running_sum)
