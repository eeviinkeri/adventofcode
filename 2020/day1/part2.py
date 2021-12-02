from part1 import read_lines_in_file_to_list_of_integers


def find_three_entries_that_sum_to_2020(values: list):
    for i in range(0, len(values)):
        first_value = values[i]
        if i != (len(values) - 2):
            rest_of_values = values[i+1:]
            for j in range (0, len(rest_of_values)):
                second_value = rest_of_values[j]
                if j != (len(rest_of_values) - 1):
                    remaining_list = rest_of_values[j+1:]
                    for k in range(0, len(remaining_list)):
                        third_value = remaining_list[k]
                        if first_value + second_value + third_value == 2020:
                            return (first_value, second_value, third_value)


def main():
    data = read_lines_in_file_to_list_of_integers('input1.txt')
    values = find_three_entries_that_sum_to_2020(data)
    values_multiplied = values[0] * values[1] * values[2]
    print(values_multiplied)


if __name__ == "__main__":
    main()