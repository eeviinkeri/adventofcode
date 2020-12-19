from collections import Counter
from part1 import read_file_to_list


def count_yes_answers(answers, group_size):
    counter = Counter(answers)
    everyone_agrees_count = 0
    for key in counter:
        if counter[key] == group_size:
            everyone_agrees_count += 1
    return everyone_agrees_count


def get_group_size(answers):
    separate_answers = answers.split('\n')
    return len(separate_answers)


def main():
    form_answers = read_file_to_list("input6.txt", "\n\n")

    all_yes = list()
    for entry in form_answers:
        group_size = get_group_size(entry)
        answers = entry.replace('\n', '')
        yes_count = count_yes_answers(answers, group_size)
        all_yes.append(yes_count)

    all_yes_sum = sum(all_yes)
    print(all_yes_sum)    


if __name__ == "__main__":
    main()