def get_min_max_num(num_range):
    num_range_list = num_range.split('-')
    return int(num_range_list[0]), int(num_range_list[1])
 

def parse_elements(item):
    item_list = item.split(' ')
    return item_list[0], item_list[1], item_list[2]


def validate(item):
    num_range, letter, password = parse_elements(item)
    min_num, max_num = get_min_max_num(num_range)
    letter_count = password.count(letter)
    if min_num <= letter_count <= max_num:
        return True
    else:
        return False


def read_lines_in_file_as_list(filename):
    with open(filename, "r") as f:
        input_values = [line.strip("\n").replace(':', '') for line in f]
        return input_values


def main():
    data = read_lines_in_file_as_list('input2.txt')
    counter = 0
    for password in data:
        if validate(password):
            counter += 1
    print(counter)


if __name__ == "__main__":
    main()