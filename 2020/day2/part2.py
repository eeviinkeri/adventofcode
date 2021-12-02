from part1 import read_lines_in_file_as_list, parse_elements, get_min_max_num


def validate(item):
    num_range, letter, password = parse_elements(item)
    first_num, second_num = get_min_max_num(num_range)
    first_index, second_index = first_num - 1, second_num - 1
    first_index_char = password[first_index]
    second_index_char = password[second_index] 
    if (first_index_char == letter and second_index_char != letter) or (first_index_char != letter and second_index_char == letter):
        return True
    else:
        False


def main():
    data = read_lines_in_file_as_list('input2.txt')
    counter = 0
    for password in data:
        if validate(password):
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()