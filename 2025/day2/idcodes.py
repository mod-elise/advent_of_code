with open("input.txt", "r") as file:
    id_range_list = file.read().split(',')


def is_even_length(id_code):
    return len(id_code) % 2 == 0

def isInvalidCode(id_code, code_length):
    for i in range(1, code_length):
        chunks = []
        if code_length%i== 0:
            for j in range(0,code_length,i):
                chunks.append(id_code[j:j+i])
        chunks_set = set(chunks)
        if len(chunks_set) == 1:
            return True
    return False

invalid_id_codes_pt1 = []
invalid_id_codes_pt2 = []

for id_range in id_range_list:
    start, end = map(int, id_range.split("-"))
    for id_code in range(start, end + 1):
        id_code_str = str(id_code)
        code_length = len(id_code_str)

        # part 1
        if is_even_length(id_code_str):
            left_half = id_code_str[:len(id_code_str) // 2]
            right_half = id_code_str[len(id_code_str) // 2:]
            if left_half == right_half:
                invalid_id_codes_pt1.append(id_code_str)

        # part 2.
        if isInvalidCode(id_code_str, code_length):
            invalid_id_codes_pt2.append(id_code_str)
 
print(f'Sum of invalid ID codes: {sum([int(x) for x in invalid_id_codes_pt1])}')
print(f'Sum of invalid ID codes for part 2: {sum([int(x) for x in invalid_id_codes_pt2])}')