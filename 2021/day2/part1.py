def move_up(horizontal: int, depth: int, units: int):
    depth = depth - units
    return horizontal, depth


def move_down(horizontal: int, depth: int, units: int):
    depth = depth + units
    return horizontal, depth


def move_forward(horizontal: int, depth: int, units: int):
    horizontal = horizontal + units
    return horizontal, depth


def move(horizontal: int, depth: int, course_command: str):
    command = course_command[:-2]
    units = int(course_command[-1])
    if command == 'forward':
        horizontal, depth = move_forward(horizontal, depth, units)
    if command == 'down':
        horizontal, depth = move_down(horizontal, depth, units)
    if command == 'up':
        horizontal, depth = move_up(horizontal, depth, units)
    return horizontal, depth


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        data = [line.strip("\n") for line in f]
        return data


def main():
    horizontal = 0
    depth = 0

    course_commands = read_lines_in_file_to_list('day2/input.txt')
    for command in course_commands:
        horizontal, depth = move(horizontal, depth, command)

    print(f'final horizontal position * final depth position = {horizontal * depth}')


if __name__ == "__main__":
    main()
