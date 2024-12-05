with open('input.txt') as f:
    wordsearch = f.read()

wordsearch = wordsearch.splitlines()
wordsearch = [list(line) for line in wordsearch]

def find_word(letter):
    count = 0
    if letter[0] + 3 < len(wordsearch[0]):
        if wordsearch[letter[1]][letter[0]+1] == 'M' and wordsearch[letter[1]][letter[0]+2] == 'A' and wordsearch[letter[1]][letter[0]+3] == 'S':
            count += 1
    if letter[0] - 3 >= 0:
        if wordsearch[letter[1]][letter[0]-1] == 'M' and wordsearch[letter[1]][letter[0]-2] == 'A' and wordsearch[letter[1]][letter[0]-3] == 'S':
            count += 1
    if letter[1] + 3 < len(wordsearch):
        if wordsearch[letter[1]+1][letter[0]] == 'M' and wordsearch[letter[1]+2][letter[0]] == 'A' and wordsearch[letter[1]+3][letter[0]] == 'S':
            count += 1
    if letter[1] - 3 >= 0:
        if wordsearch[letter[1]-1][letter[0]] == 'M' and wordsearch[letter[1]-2][letter[0]] == 'A' and wordsearch[letter[1]-3][letter[0]] == 'S':
            count += 1
    if letter[0] + 3 < len(wordsearch[0]) and letter[1] + 3 < len(wordsearch):
        if wordsearch[letter[1]+1][letter[0]+1] == 'M' and wordsearch[letter[1]+2][letter[0]+2] == 'A' and wordsearch[letter[1]+3][letter[0]+3] == 'S':
            count += 1
    if letter[0] + 3 < len(wordsearch[0]) and letter[1] - 3 >= 0:
        if wordsearch[letter[1]-1][letter[0]+1] == 'M' and wordsearch[letter[1]-2][letter[0]+2] == 'A' and wordsearch[letter[1]-3][letter[0]+3] == 'S':
            count += 1
    if letter[0] - 3 >= 0 and letter[1] + 3 < len(wordsearch):
        if wordsearch[letter[1]+1][letter[0]-1] == 'M' and wordsearch[letter[1]+2][letter[0]-2] == 'A' and wordsearch[letter[1]+3][letter[0]-3] == 'S':
            count += 1
    if letter[0] - 3 >= 0 and letter[1] - 3 >= 0:
        if wordsearch[letter[1]-1][letter[0]-1] == 'M' and wordsearch[letter[1]-2][letter[0]-2] == 'A' and wordsearch[letter[1]-3][letter[0]-3] == 'S':
            count += 1
    return count

def find_mas(letter):
    count = 0
    if letter[0] - 1 >= 0 and letter[1] - 1 >= 0 and letter[0] + 1 < len(wordsearch[0]) and letter[1] + 1 < len(wordsearch):
        corners_1 =[wordsearch[letter[1]-1][letter[0]-1],wordsearch[letter[1]+1][letter[0]+1]]
        corners_2 = [wordsearch[letter[1]+1][letter[0]-1],wordsearch[letter[1]-1][letter[0]+1]]
        if ('M' in corners_1) and 'S' in corners_1:
            if ('M' in corners_2) and 'S' in corners_2:
                count += 1
    return count

def part1():
    start_letter = []
    for i_idx, i in enumerate(wordsearch):
        for j_idx, j in enumerate(i):
            if j == 'X':
                start_letter.append([j_idx,i_idx,j])
    foundWords = []
    for letter in start_letter:
        foundWords.append(find_word(letter))
    return sum(foundWords)


def part2():
    start_letter = []
    for i_idx, i in enumerate(wordsearch):
        for j_idx, j in enumerate(i):
            if j == 'A':
                start_letter.append([j_idx,i_idx,j])
    found_xmas = []
    for letter in start_letter:
        found_xmas.append(find_mas(letter))
    return sum(found_xmas)

print (f'part 1: {part1()}')
print (f'part 2: {part2()}')
