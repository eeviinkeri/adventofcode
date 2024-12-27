def get_input(is_test: bool):
    if is_test:
        return [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9], [9, 7, 6, 2, 1], [1, 3, 2, 4, 5], [8, 6, 4, 4, 1], [1, 3, 6, 7, 9]]
    else:
        return read_file_to_list_of_lists('data/input2.txt')


def read_file_to_list_of_lists(filename):
    data = list()
    with open(filename, 'r') as file:
        for line in file:
            data.append(line.strip().split(' '))
    return data


def is_ascending(items: list) -> bool:
    return all(int(items[i]) < int(items[i + 1]) for i in range(len(items) - 1))


def is_descending(items: list) -> bool:
    return all(int(items[i]) > int(items[i + 1]) for i in range(len(items) - 1))


def is_safe_diff(items: list) -> bool:
    cnter = 0
    for i in range(len(items) - 1):
        if abs(int(items[i+1]) - int(items[i])) > 3:
            cnter += 1
    return True if cnter == 0 else False


def is_safe_report(items: list) -> bool:
    if is_ascending(items) and is_safe_diff(items):
        return True
    elif is_descending(items) and is_safe_diff(items):
        return True
    else:
        return False


def is_safe_report_damp(items: list) -> bool:
    for i in range(0, len(items)):
        orig_items_tuple = tuple(items)
        damp_items = list(orig_items_tuple)
        del damp_items[i]
        if is_safe_report(damp_items):
            return True


def main():
    data = get_input(is_test=False)

    counter = 0
    for i in range(0, len(data)):
        if is_safe_report(data[i]):
            counter += 1
    print(f"Answer to part 1 is: {counter}")

    counter = 0
    for i in range(0, len(data)):
        if is_safe_report(data[i]):
            counter += 1
        elif is_safe_report_damp(data[i]):
             counter += 1
    print(f"Answer to part 2 is: {counter}")


if __name__ == "__main__":
    main()