def get_num_of_adapters(data, joltage_diff):
    count = 0
    for i in range(len(data)-1):
        if data[i+1]-data[i] == joltage_diff:
            count += 1
    return count


def add_outlet_and_device_joltages(adapter_joltages):
    device_joltage = max(adapter_joltages) + 3
    outlet_joltage = 0
    adapter_joltages.append(device_joltage)
    adapter_joltages.append(outlet_joltage)
    adapter_joltages.sort()
    return adapter_joltages


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        return [int(line.strip("\n")) for line in f]


def main():
    adapter_joltages = read_lines_in_file_to_list("input10.txt")
    joltages = add_outlet_and_device_joltages(adapter_joltages)

    joltage_diff_1 = get_num_of_adapters(joltages, 1)
    joltage_diff_3 = get_num_of_adapters(joltages, 3)

    print(joltage_diff_1 * joltage_diff_3)


if __name__ == "__main__":
    main()
