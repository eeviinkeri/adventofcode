import day1.part1 as part1


def main():
    measurements = part1.read_lines_in_file_to_list_of_integers('day1/input.txt')

    three_measurements = []
    for i in range (0, len(measurements)):
        sum_lines = sum(measurements[i:i+3])
        three_measurements.append(sum_lines)

    increased = part1.get_num_of_increased_measurements(three_measurements)
    print(f'The depth measurement increases {increased} times.')


if __name__ == "__main__":
    main()

