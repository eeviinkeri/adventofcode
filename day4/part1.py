def validate_required_fields(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    counter = 0
    for field in required_fields:
        if field in passport:
            counter += 1
    if counter == 7:
        return True 


def read_file_to_list(filename):
    with open(filename, "r") as f:
        return f.read().replace('\n', ' ').split('  ')


def main():
    data = read_file_to_list('input4.txt')

    valid_entries = 0
    for passport in data:
        if validate_required_fields(passport):               
            valid_entries += 1

    print(valid_entries)


if __name__ == "__main__":
    main()
