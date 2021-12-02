def find_two_entries_that_sum_to_2020(values: list):
    for i in range(0, len(values)):
        first_value = values[i]
        if i != (len(values) - 1):
            rest_of_values = values[i+1:]
            for j in range (0, len(rest_of_values)):
                second_value = rest_of_values[j]
                if first_value + second_value == 2020:
                    return (first_value, second_value)


def read_lines_in_file_to_list_of_integers(filename: str):
    with open(filename, "r") as f:
        data = [int(line.strip("\n")) for line in f]
        return data


def main():
    data = read_lines_in_file_to_list_of_integers('input1.txt')
    values = find_two_entries_that_sum_to_2020(data)
    values_multiplied = values[0] * values[1]
    print(values_multiplied)


if __name__ == "__main__":
    main()