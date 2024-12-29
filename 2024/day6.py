import re


def get_input(is_test: bool):
    if is_test:
        return ['....#.....',
                '.........#',
                '..........',
                '..#.......',
                '.......#..',
                '..........',
                '.#..^.....',
                '........#.',
                '#.........',
                '......#...']
    else:
        with open('data/input6.txt', "r") as f:
            return [line.strip("\n") for line in f]


def get_original_guard_position(map) -> tuple:
    guard_regex = r"\^"
    line_num = -1
    for line in map:
        line_num += 1
        position = re.search(guard_regex, line)
        if position is not None:
            pos_index = position.start()
            return (line_num, pos_index)


def check_next_pos(map, position, direction, line_count, line_len):
    line = position[0]
    pos_index = position[1]
    if direction == 'up':
        if line - 1 >= 0:
            return map[line-1][pos_index]
        else:
            return None
    if direction == 'right':
        if pos_index + 1 <= line_len:
            return map[line][pos_index+1]
        else:
            return None
    if direction == 'down':
        if line + 1 <= line_count:
            return map[line+1][pos_index]
        else:
            return None
    if direction == 'left':
        if pos_index - 1 >= 0:
            return map[line][pos_index-1]
        else:
            return None


def take_step_forward(position, direction):
    line_num = position[0]
    pos_index = position[1]
    if direction == 'up':
        return (line_num - 1, pos_index)
    if direction == 'right':
        return (line_num, pos_index + 1)
    if direction == 'down':
        return (line_num + 1, pos_index)
    if direction == 'left':
        return (line_num, pos_index - 1)


def turn_right(direction):
    if direction == 'up':
        return 'right'
    if direction == 'right':
        return 'down'
    if direction == 'down':
        return 'left'
    if direction == 'left':
        return 'up' 


def main():
    map = get_input(is_test=False)
    line_count = len(map) - 1
    line_len = len(map[0]) - 1
    guard_pos = get_original_guard_position(map)
    direction = 'up'
    guard_positions = [guard_pos]
    next_position = check_next_pos(map, guard_pos, direction, line_count, line_len)
    counter = 0
    while next_position is not None:
        # print(guard_pos, direction)
        if next_position != '#':
            guard_pos = take_step_forward(guard_pos, direction)
        else:
            direction = turn_right(direction)
        counter += 1
        if counter > 10000000:
            break
        guard_positions.append(guard_pos)
        next_position = check_next_pos(map, guard_pos, direction, line_count, line_len)

    unique_positions = list(set(guard_positions))
    print(f"Answer to part 1 is: {len(unique_positions)}")


if __name__ == "__main__":
    main()
