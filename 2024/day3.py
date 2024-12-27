import re


def get_input(is_test: bool):
    if is_test:
        # return "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        return "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    else:
        with open('data/input3.txt', 'r') as file:
            return file.read()


def is_regex(item: str, regex: str) -> bool:
    return re.search(regex, item)


def multiply(item: str) -> int:
    numbers = re.findall(r"\d+", item)
    return int(numbers[0]) * int(numbers[1])


def main():
    data = get_input(is_test=False)

    mul_regex = r"mul\(\d+,\d+\)"
    mul_list = re.findall(mul_regex, data)

    multiplications = list()
    for i in mul_list:
        mul = multiply(i)
        multiplications.append(mul)

    print(f"Answer to part 1 is: {sum(multiplications)}")


    do_regex = r"do\(\)"
    dont_regex = r"don\'t\(\)"

    only_interesting_parts = re.findall(f"{mul_regex}|{do_regex}|{dont_regex}", data)

    multiplications = list()
    i = 0
    while i <= len(only_interesting_parts) - 1:
        if is_regex(only_interesting_parts[i], mul_regex):
            multiplications.append(multiply(only_interesting_parts[i]))
            i += 1
        elif is_regex(only_interesting_parts[i], dont_regex):
            i += 1
            while not is_regex(only_interesting_parts[i], do_regex):
                i += 1
            i += 1
        elif is_regex(only_interesting_parts[i], do_regex):
            i += 1

    print(f"Answer to part 2 is: {sum(multiplications)}")


if __name__ == "__main__":
    main()