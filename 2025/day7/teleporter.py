try:
    with open('1input.txt', 'r') as file:
        print ("found file")
        manifold = file.read().splitlines()
except FileNotFoundError:
        print ("file not found, using hardcoded values")
        manifold = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".strip().splitlines()

def rotate_the_tachyon_manifold(manifold):
    rotated = zip(*manifold[::1])
    rotated_manifold = []
    for row in rotated:
        new_row= []
        for char in row:
            new_row.append(char)
        rotated_manifold.append(''.join(new_row))
    return rotated_manifold

def starting_position_finder(beams):
    upper_splits = []
    lower_splits = []
    starting_positions = []
    for beams in tachyon_beams:
        if beams.has_split:
            upper_splits.append(beams.upper_splitter_position)
            lower_splits.append(beams.lower_splitter_position)
        starting_positions.append(beams.start_position)
    return starting_positions, upper_splits, lower_splits

def tachyon_beam_finder(tachyon_beams):
    starting_position_list, upper_split_list, lower_split_list = starting_position_finder(tachyon_beams)
    new_beam_list = []
    for upper_split in upper_split_list:
        if upper_split not in starting_position_list:
            new_beam_list.append(upper_split)
    for lower_split in lower_split_list:
        if lower_split not in starting_position_list:
            new_beam_list.append(lower_split)
    return new_beam_list

class TachyonBeam:
    def __init__(self, start_position):
        self.start_position = start_position
        self.has_split = False
        for char in manifold[start_position[0]]:
            if char == '^':
                self.has_split = True
                self.splitter_position = (start_position[0], manifold[start_position[0]].index(char))
                self.beam_split(self.splitter_position)
                break

    def beam_split(self, splitter_position):
        self.upper_splitter_position = (splitter_position[0]-1, splitter_position[1])
        self.lower_splitter_position = (splitter_position[0]+1, splitter_position[1])


manifold = rotate_the_tachyon_manifold(manifold)
print (' 0123456789012345')
i = 0
for row in manifold:
    print(str(i)+row)
    if row[0] == 'S':
        start_position = (manifold.index(row), 0)
    i += 1
tachyon_beams = []
tachyon_beams.append(TachyonBeam(start_position))
new_tachyon_beams = tachyon_beam_finder(tachyon_beams)
temp_counter = 0
while len(new_tachyon_beams) > 0:
    temp_counter += 1
    print (f"Iteration {temp_counter}, new beams found: {len(new_tachyon_beams)}")
    for beam in new_tachyon_beams:
        print(f"  New beam starting at position {beam}")
        tachyon_beams.append(TachyonBeam(beam))


    new_tachyon_beams = tachyon_beam_finder(tachyon_beams)

print (f'Total tachyon beams found: {len(tachyon_beams)}')

