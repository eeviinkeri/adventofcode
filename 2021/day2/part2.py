import day2.part1 as part1


def aim_up(aim: int, units: int):
    aim = aim - units
    return aim


def aim_down(aim: int, units: int):
    aim = aim + units
    return aim


def move_forward(horizontal: int, depth: int, aim: int, units: int):
    horizontal = horizontal + units
    depth = depth + aim * units
    return horizontal, depth


def move(horizontal: int, depth: int, aim: int, course_command: str):
    command = course_command[:-2]
    units = int(course_command[-1])
    if command == 'forward':
        horizontal, depth = move_forward(horizontal, depth, aim, units)
    if command == 'down':
        aim = aim_down(aim, units)
    if command == 'up':
        aim = aim_up(aim, units)
    return horizontal, depth, aim


def main():
    horizontal = 0
    depth = 0
    aim = 0

    course_commands = part1.read_lines_in_file_to_list('day2/input.txt')
    for command in course_commands:
        horizontal, depth, aim = move(horizontal, depth, aim, command)

    print(f'final horizontal position * final depth position = {horizontal * depth}')


if __name__ == "__main__":
    main()
