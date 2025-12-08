try:
    with open('input.txt', 'r') as file:
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

def rotate_the_tachyon_manifold(manifold, direction='clockwise'):
    if direction == 'clockwise':
        factor = 1
    else:
        factor = -1
    rotated = zip(*manifold[::factor])
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
    count_upper_splits = 0
    for upper_split in upper_split_list:
        count_upper_splits += 1
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
        x, y = start_position[0], start_position[1]
        rest_of_tachyon_path = manifold[x][y:]

        for char in rest_of_tachyon_path:
            if char == '^':
                self.has_split = True
                self.splitter_position = (start_position[0], rest_of_tachyon_path.index(char)+y)
                self.beam_split(self.splitter_position)
                break

    def beam_split(self, splitter_position):
        self.upper_splitter_position = (splitter_position[0]-1, splitter_position[1])
        self.lower_splitter_position = (splitter_position[0]+1, splitter_position[1])


manifold = rotate_the_tachyon_manifold(manifold)
i = 0
for row in manifold:
    if row[0] == 'S':
        start_position = (manifold.index(row), 0)
    i += 1

existing_start_positions = []
existing_start_positions.append(start_position)
tachyon_beams = []
tachyon_beams.append(TachyonBeam(start_position))
new_tachyon_beams = tachyon_beam_finder(tachyon_beams)

while len(new_tachyon_beams) > 0:
    for beam in new_tachyon_beams:
        new_beam = TachyonBeam(beam)
        duplicate = False
        for existant_beam in tachyon_beams:
            if new_beam.start_position == existant_beam.start_position:
                duplicate = True
        if not duplicate:
            tachyon_beams.append(new_beam)    
    new_tachyon_beams = tachyon_beam_finder(tachyon_beams)


split_spots = []
for beam in tachyon_beams:
    try:
        split_spots.append(beam.splitter_position)
    except:
        continue

split_spots = set(split_spots)
print (f'The split spot count is {len(split_spots)}')
