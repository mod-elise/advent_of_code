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

class TachyonBeam:
    def __init__(self, start_position):
        self.start_position = start_position
        self.splitter_position = False
        for char in manifold[start_position[0]]:
            if char == '^':
                self.splitter_position = (start_position[0], manifold[start_position[0]].index(char))
                self.beam_split(self.splitter_position)
                break

    def beam_split(self, splitter_position):
        self.upper_splitter_position = (splitter_position[0]-1, splitter_position[1])
        self.lower_splitter_position = (splitter_position[0]+1, splitter_position[1])


manifold = rotate_the_tachyon_manifold(manifold)
for row in manifold:
    print(row)
    if row[0] == 'S':
        start_position = (manifold.index(row), 0)

tachyon_beams = []
tachyon_beams.append(TachyonBeam(start_position))
print ("Beam 1 splits into beams at positions:")
print (tachyon_beams[0].upper_splitter_position)
print (tachyon_beams[0].lower_splitter_position)

tachyon_beams.append(TachyonBeam(tachyon_beams[0].lower_splitter_position))
tachyon_beams.append(TachyonBeam(tachyon_beams[0].upper_splitter_position))

print ("Beam 2 splits into beams at positions:")
print (tachyon_beams[1].upper_splitter_position)
print (tachyon_beams[1].lower_splitter_position)

print ("Beam 3 splits into beams at positions:")
print (tachyon_beams[2].upper_splitter_position)
print (tachyon_beams[2].lower_splitter_position)