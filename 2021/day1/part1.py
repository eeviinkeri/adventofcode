
def depth_measurement_increased(first_measurement, second_measurement):
    if second_measurement > first_measurement:
        return True


def get_num_of_increased_measurements(measurements):
    increased = 0
    for i in range(1, len(measurements)):
        if depth_measurement_increased(measurements[i-1], measurements[i]):
            increased += 1
    return increased


def read_lines_in_file_to_list_of_integers(filename: str):
    with open(filename, "r") as f:
        data = [int(line.strip("\n")) for line in f]
        return data


def main():
    measurements = read_lines_in_file_to_list_of_integers('day1/input.txt')
    increased = get_num_of_increased_measurements(measurements)
    print(f'The depth measurement increases {increased} times.')


if __name__ == "__main__":
    main()
