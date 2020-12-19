def get_valid_outer_bag(bag, rule):
    split_rule = rule.split("bags contain ")
    outer_bag = split_rule[0]
    inner_bags = split_rule[1]
    return outer_bag if bag in inner_bags else None


def get_all_outer_bags(bag_list, rules, outer_bags):
    if len(bag_list) == 0:
        return outer_bags
    bag_list_tmp = list()
    for bag in bag_list:
        for rule in rules:
            outer_bag = get_valid_outer_bag(bag, rule)
            if outer_bag is not None and outer_bag not in outer_bags:
                bag_list_tmp.append(outer_bag)
                outer_bags.append(outer_bag)
    return get_all_outer_bags(bag_list_tmp, rules, outer_bags)


def read_lines_in_file_to_list(filename: str):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def main():
    rules = read_lines_in_file_to_list("input7.txt")
    my_bags = ["shiny gold"]

    bag_list = list()
    bag_list = get_all_outer_bags(my_bags, rules, bag_list)

    bag_count = len(bag_list)
    print(bag_count)


if __name__ == "__main__":
    main()
