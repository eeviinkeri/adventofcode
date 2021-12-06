def get_least_common_bits(most_common_bits):
    least_common_bits = []
    for bit in most_common_bits:
        if bit == 1:
            least_common_bits.append(0)
        else:
            least_common_bits.append(1)
    return least_common_bits


def count_bits(value, bit_list):
    values = []
    for bit in bit_list:
        if bit == value:
            values.append(bit)
    return len(values)


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
    least_common_bits = get_least_common_bits(most_common_bits)

    # convert list of integers to binary number and then to integer
    gamma_rate = int("".join(str(x) for x in most_common_bits), 2)
    epsilon_rate = int("".join(str(x) for x in least_common_bits), 2)

    power_consumption = gamma_rate * epsilon_rate
    print(f'power consumption of the submarine is {power_consumption}')


if __name__ == "__main__":
    main()
