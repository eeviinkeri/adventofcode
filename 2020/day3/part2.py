from part1 import read_file_to_list, move_x_right_1_down


def multiply(iterable):
    prod = 1
    for x in iterable:
        prod *= x
    return prod


def move_1_right_2_down(slopes):
    index = 0
    tree_count = 0
    slope_num = 0
    for slope in slopes:
        slope_num += 1
        if slope_num % 2 == 0:
            continue 
        while len(slope) < (index + 1):
            slope += slope
        if slope[index] == '#':
            tree_count += 1        
        index += 1
    return tree_count   


def main():
    slopes = read_file_to_list("input3.txt")
    
    tree_counts = list()
    for x in [1, 3, 5, 7]:
        tree_counts.append(move_x_right_1_down(slopes, x)) 
    tree_counts.append(move_1_right_2_down(slopes))

    product = multiply(tree_counts)
    print(product)



if __name__ == "__main__":
    main()
