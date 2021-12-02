from part1 import read_lines_in_file_to_list, check_valid_numbers


def find_value_range(numbers, invalid_number):
    values = list()
    for i in range(len(numbers)):
        if sum(values) == invalid_number:
            return values
        if sum(values) < invalid_number:
            values.append(numbers[i])
        if sum(values) > invalid_number:
            return find_value_range(numbers[1:], invalid_number)


def find_encryption_weakness(numbers, invalid_number):
    value_list = find_value_range(numbers, invalid_number)
    return min(value_list) + max(value_list)


def main():
    XMAS = read_lines_in_file_to_list("input9.txt")
    invalid_number = check_valid_numbers(XMAS, 25)

    encryption_weakness = find_encryption_weakness(XMAS, invalid_number)
    print(encryption_weakness)


if __name__ == "__main__":
    main()