from part1 import read_file_to_list, validate_required_fields
import re


def passport_id_is_valid(value):
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    return True if len(value) == 9 else False


def eye_color_is_valid(value):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    possible_colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return True if value in possible_colours else False


def hair_color_is_valid(value):
    # hcl (Hair Color) - a number followed by exactly six characters 0-9 or a-f.
    return True if re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', value) else False


def height_is_valid(value):
    #hgt (Height) - a number followed by either cm or in:
    #    If cm, the number must be at least 150 and at most 193.
    #    If in, the number must be at least 59 and at most 76.
    unit = value[-2:]
    number = value[:-2]
    if unit == 'cm':
        return True if 150 <= int(number) <= 193 else False
    elif unit == 'in':
        return True if 59 <= int(number) <= 76 else False 
    else: 
        return False


def expiration_year_is_valid(value):
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    return True if 2020 <= int(value) <= 2030 else False


def issue_year_is_valid(value):
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    return True if 2010 <= int(value) <= 2020 else False


def birth_year_is_valid(value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    return True if 1920 <= int(value) <= 2002 else False


def is_valid_passport(entry):
    return True if ( 
        birth_year_is_valid(entry['byr']) and 
        issue_year_is_valid(entry['iyr']) and
        expiration_year_is_valid(entry['eyr']) and
        height_is_valid(entry['hgt']) and
        hair_color_is_valid(entry['hcl']) and
        eye_color_is_valid(entry['ecl']) and
        passport_id_is_valid(entry['pid'])
    ) else False


def main():
    data = read_file_to_list('input4.txt')

    valid_entries = 0
    for passport in data:
        if validate_required_fields(passport):               
            field_list = passport.split(' ')
            items_dict = dict()
            for item in field_list:
                key_value = item.split(':')
                items_dict[key_value[0]] = key_value[1]
            if is_valid_passport(items_dict):
                valid_entries += 1
    print(valid_entries)


if __name__ == "__main__":
    main()
