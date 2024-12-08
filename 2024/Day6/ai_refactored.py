import time

def find_guard(lab_map, guard_symbols):
    return next((key for key, value in lab_map.items() if value in guard_symbols), None)

def determine_guard_facing(lab_map, guard_coord, guard_symbols):
    symbol_to_direction = {guard_symbols[0]: 'down', guard_symbols[1]: 'up', guard_symbols[2]: 'left', guard_symbols[3]: 'right'}
    return symbol_to_direction.get(lab_map[guard_coord])

def is_obstacle_ahead(lab_map, guard_coord, guard_direction):
    deltas = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    delta = deltas.get(guard_direction)
    if not delta:
        return False, False

    new_coord = (guard_coord[0] + delta[0], guard_coord[1] + delta[1])
    return (lab_map.get(new_coord) == '#', True) if new_coord in lab_map else (False, False)

def move_guard(guard_coord, guard_direction):
    deltas = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    delta = deltas.get(guard_direction)
    if not delta:
        return guard_coord
    return [guard_coord[0] + delta[0], guard_coord[1] + delta[1]]

def turn_guard(guard_direction):
    turns = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    return turns.get(guard_direction, guard_direction)

def count_guard_steps(lab_map, guard_coord, guard_direction):
    visited_squares = set()
    path_map = {guard_coord: guard_direction}
    visited_squares.add(guard_coord)

    is_obstacle, continue_movement = is_obstacle_ahead(lab_map, guard_coord, guard_direction)
    while continue_movement:
        guard_coord = move_guard(guard_coord, guard_direction)

        if tuple(guard_coord) in path_map and path_map[tuple(guard_coord)] == guard_direction:
            return list(visited_squares), True

        path_map[tuple(guard_coord)] = guard_direction
        visited_squares.add(tuple(guard_coord))

        is_obstacle, continue_movement = is_obstacle_ahead(lab_map, guard_coord, guard_direction)

        if is_obstacle:
            guard_direction = turn_guard(guard_direction)
    return list(visited_squares), False

def main():
    start_time = time.time()
    guard_symbols = ['v', '^', '<', '>']

    with open('input.txt') as f:
        raw_map = f.read()

    lines = raw_map.splitlines()
    lab_map = {(row, col): char for row, line in enumerate(lines) for col, char in enumerate(line)}

    guard_coord = find_guard(lab_map, guard_symbols)
    guard_direction = determine_guard_facing(lab_map, guard_coord, guard_symbols)

    visited_squares = count_guard_steps(lab_map, guard_coord, guard_direction)[0]
    unique_squares = set(tuple(square) for square in visited_squares)
    print(f'Part 1: {len(unique_squares)}')

    loop_count = 0
    for square in unique_squares:
        temp_map = lab_map.copy()
        temp_map[square] = '#'
        _, loop = count_guard_steps(temp_map, guard_coord, guard_direction)
        if loop:
            loop_count += 1
            print(f'Part 2: {loop_count - 2}', end='\r', flush=True)

    print(f"\n--- {time.time() - start_time} seconds ---")

if __name__ == "__main__":
    main()
