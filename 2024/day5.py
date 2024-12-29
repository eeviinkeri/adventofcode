from functools import cmp_to_key


def get_input(is_test: bool):
    if is_test:
        data_1 = ['47|53',
                  '97|13',
                  '97|61',
                  '97|47',
                  '75|29',
                  '61|13',
                  '75|53',
                  '29|13',
                  '97|29',
                  '53|29',
                  '61|53',
                  '97|53',
                  '61|29',
                  '47|13',
                  '75|47',
                  '97|75',
                  '47|61',
                  '75|61',
                  '47|29',
                  '75|13',
                  '53|13']
        data_2 = ['75,47,61,53,29',
                  '97,61,53,29,13',
                  '75,29,13',
                  '75,97,47,61,53',
                  '61,13,29',
                  '97,13,75,29,47']
    else:
        with open('data/input5.txt', 'r') as file:
            data = file.read().split(('\n'))
        data_1 = data[:data.index('')]
        data_2 = data[data.index('')+1:]
    return data_1, data_2


# Don't like these unbound variables but didn't know how else to build the custom sort function
data_1, data_2 = get_input(is_test=False)

rules = list()
for item in data_1:
    rules.append(tuple(map(int, item.split('|'))))


def are_in_right_order(update, rules) -> bool:
    counter = 0
    for rule in rules:
        if not is_in_right_order(update, rule):
            counter += 1
    if counter == 0:
        return True


def is_in_right_order(update, rule) -> bool:
    if rule[0] in update and rule[1] in update and update.index(rule[0]) > update.index(rule[1]):
        return False
    else:
        return True


def compare(a, b):
    if (a, b) in rules:
        return -1
    elif (b, a) in rules:
        return 1
    else:
        return 0


def sum_middle_nums(update_list):
    middle_nums = list()
    for item in update_list:
        middle_nums.append(item[get_middle_number(item)])
    return sum(middle_nums)


def get_middle_number(update) -> int:
    return (len(update))//2


def main():
    updates = list()
    for item in data_2:
        updates.append(item.split(','))

    correct_updates = list()
    incorrect_updates = list()
    for update in updates:
        update = [int(item) for item in update]
        if are_in_right_order(update, rules):
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    middle_num_sum = sum_middle_nums(correct_updates)

    print(f"Answer to part 1 is: {middle_num_sum}")

    # Custom list sorting: https://stackoverflow.com/questions/11850425/custom-python-list-sorting
    cmp_key = cmp_to_key(compare)

    sorted_updates = list()
    for update in incorrect_updates:
        update.sort(key=cmp_key)
        sorted_updates.append(update)

    middle_num_sum = sum_middle_nums(sorted_updates)

    print(f"Answer to part 2 is: {middle_num_sum}")


if __name__ == "__main__":
    main()