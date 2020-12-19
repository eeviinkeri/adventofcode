def move_x_right_1_down(slopes, x):
    index = 0
    tree_count = 0
    for slope in slopes:
        while len(slope) < (index + x):
            slope += slope
        if slope[index] == '#':
            tree_count += 1        
        index += x
    return tree_count 


def read_file_to_list(filename):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def main():
    slopes = read_file_to_list("input3.txt")
    trees = move_x_right_1_down(slopes, 3)
    print(trees)


if __name__ == "__main__":
    main()
