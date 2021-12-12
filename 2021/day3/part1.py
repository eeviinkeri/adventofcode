def convert_binary_to_integer(binary_as_list_of_int):
    return int("".join(str(x) for x in binary_as_list_of_int), 2)


def count_bits(value, bit_list):
    values = []
    for bit in bit_list:
        if bit == value:
            values.append(bit)
    return len(values)


def find_least_common_bit(position, diagnostinc_report):
    bit_list = [int(report[position]) for report in diagnostinc_report]
    ones = count_bits(1, bit_list)
    zeros = count_bits(0, bit_list)
    if ones >= zeros:
        return 0
    else:
        return 1


def get_least_common_bits(diagnostic_report):
    least_common_bits = []
    for position in range(0, 12):
        least_commont_bit = find_least_common_bit(position, diagnostic_report)
        least_common_bits.append(least_commont_bit)
    return least_common_bits


def find_most_common_bit(position, diagnostinc_report):
    bit_list = [int(report[position]) for report in diagnostinc_report]
    ones = count_bits(1, bit_list)
    zeros = count_bits(0, bit_list)
    if ones >= zeros:
        return 1
    else: 
        return 0


def get_most_common_bits(diagnostic_report):
    most_common_bits = []
    for position in range(0, 12):
        most_commont_bit = find_most_common_bit(position, diagnostic_report)
        most_common_bits.append(most_commont_bit)
    return most_common_bits


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        data = [line.strip("\n") for line in f]
        return data


def main():
    diagnostic_report = read_lines_in_file_to_list('day3/input.txt')

    most_common_bits = get_most_common_bits(diagnostic_report)
    least_common_bits = get_least_common_bits(diagnostic_report)

    gamma_rate = convert_binary_to_integer(most_common_bits)
    epsilon_rate = convert_binary_to_integer(least_common_bits)

    power_consumption = gamma_rate * epsilon_rate
    print(f'power consumption of the submarine is {power_consumption}')


if __name__ == "__main__":
    main()
