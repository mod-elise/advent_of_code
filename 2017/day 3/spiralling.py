import math

def calculate_ring(input_number):
    for idx, side_length in enumerate(range(1, input_number, 2)):
        if side_length ** 2 >= input_number:
            return idx, side_length ** 2

def calculate_corners(bottom_right, side_length):
    return {
        "bottom_right": bottom_right,
        "bottom_left": bottom_right - side_length + 1,
        "top_left": bottom_right - 2 * side_length + 2,
        "top_right": bottom_right - 3 * side_length + 3
    }

def find_nearest_corner(input_number, corners):
    if input_number in corners.values():
        return input_number
    else:
        return min(corners.values(), key=lambda x: abs(x - input_number))

input_number = 289326
ring_number, bottom_right = calculate_ring(input_number)
side_length = int(math.sqrt(bottom_right))
distance_to_edge = bottom_right - input_number
corners = calculate_corners(bottom_right, side_length)
nearest_corner = find_nearest_corner(input_number, corners)
is_higher = nearest_corner > input_number
centre_distance = side_length // 2

if not is_higher:
    centre_value = nearest_corner + centre_distance
else:
    centre_value = nearest_corner - centre_distance
distance_to_centre = abs(input_number - centre_value)
manhattan_distance = ring_number + distance_to_centre

print(f"Manhattan distance: {manhattan_distance}")
