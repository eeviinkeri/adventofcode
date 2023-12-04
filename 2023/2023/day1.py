import os
import re


def read_file_to_list(filename):
    with open(filename) as file:
        lines = [line.rstrip() for line in file]
    return lines


def get_digits(char_string):
    return re.findall(r'\d+', char_string)


def get_all_digits(char_string):
    digit_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    digit_nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    all = digit_words + digit_nums
    return re.findall(r"(?=("+'|'.join(all)+r"))", char_string)


def map_words_to_numbers(digit_list):
    digit_map = {
        "one": "1",
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven": "7", 
        "eight": "8", 
        "nine": "9"
    }
    digit_nums = list()
    for digit in digit_list:
        if digit in list(digit_map.keys()):
            digit_nums.append(digit_map[digit])
        else:
            digit_nums.append(digit)
    return digit_nums


def main():
    filename = f"{os.getcwd()}/data/input1.txt"
    lines = read_file_to_list(filename)

    # Part 1
    calibration_values_1 = list()
    for line in lines:
        digits = get_digits(line)
        first_digit = digits[0][0]
        last_digit = digits[-1][-1]
        calibration_value = int(first_digit + last_digit)
        calibration_values_1.append(calibration_value)
    print("Answer to part one is:", sum(calibration_values_1))

    # Part 2
    calibration_values_2 = list()
    for line in lines:
        digits = get_all_digits(line)
        digits_num = map_words_to_numbers(digits)
        first_digit = digits_num[0][0]
        last_digit = digits_num[-1][-1]
        calibration_value = int(first_digit + last_digit)
        calibration_values_2.append(calibration_value)
    print("Answer to part two is:", sum(calibration_values_2))


if __name__ == "__main__":
    main()
