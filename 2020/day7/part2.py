from part1 import read_lines_in_file_to_list


def get_bag_count(bag_item):
    count = 0 if bag_item == "no other" else int(bag_item[0])
    color = bag_item[2:]
    return color, count


def get_inner_bag_list(rule):
    inner_bag_str = rule.split("contain ")[1].replace(" bags", "").replace(" bag", "")  
    inner_bag_list = inner_bag_str.split(", ")
    return inner_bag_list


def find_rule_for_bag(bag, rules):
    for rule in rules:
        outer_bag = rule.split(" bags contain")[0]
        if outer_bag == bag:
            bag_rule = rule
    return bag_rule


def get_inner_bag_count(bag, rules):
    rule = find_rule_for_bag(bag, rules)
    inner_bags = get_inner_bag_list(rule)
    contains = 0
    for bag in inner_bags:
        bag, count = get_bag_count(bag)
        if count == 0:
            return 0
        else:
            contains += count
            contains += count * get_inner_bag_count(bag, rules)
    return contains


def main():
    rules = read_lines_in_file_to_list("input7.txt")
    my_bag = "shiny gold"

    count = get_inner_bag_count(my_bag, rules)
    print(count)


if __name__ == "__main__":
    main()
