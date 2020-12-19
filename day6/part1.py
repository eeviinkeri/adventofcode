def count_unique_letters(answers):
    unique = ''.join(set(answers))
    return len(unique)


def read_file_to_list(filename: str, separator: str):
    with open(filename, "r") as f:
        return f.read().split(separator)


def main():
    form_answers = read_file_to_list("input6.txt", "\n\n")

    unique_value_counts = list()
    for entry in form_answers:
        entry = entry.replace('\n', '').replace(' ', '')
        count_unique = count_unique_letters(entry)
        unique_value_counts.append(count_unique)
    count_sum = sum(unique_value_counts)
    print(count_sum)


if __name__ == "__main__":
    main()