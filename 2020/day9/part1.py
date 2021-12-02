def is_valid_sum(val1, val2, num):
    if val1 + val2 == num:
        return True
    return False


def is_valid_number(preamble, num):
    for i in range(len(preamble)):
        for j in range(1, len(preamble)):
            if is_valid_sum(preamble[i], preamble[j], num):
                return True
    return False


def check_valid_numbers(data, preamble_len):
    for i in range(preamble_len, len(data)):
        preamble = data[i-preamble_len:i]
        num = data[i]
        if is_valid_number(preamble, num) is False:
            return num


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        return [int(line.strip("\n")) for line in f]


def main():
    XMAS = read_lines_in_file_to_list("input9.txt")
    preamble_len = 25
    invalid_number = check_valid_numbers(XMAS, preamble_len)
    print(invalid_number)


if __name__ == "__main__":
    main()
