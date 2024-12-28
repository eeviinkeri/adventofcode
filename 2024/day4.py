import numpy as np


def get_input(is_test: bool):
    if is_test:
        return [['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'],
                ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'],
                ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
                ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
                ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'],
                ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
                ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
                ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
                ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
                ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X']]
    else:
        return read_file_to_list_of_lists('data/input4.txt')


def read_file_to_list_of_lists(filename):
    data = list()
    with open(filename, 'r') as file:
        for line in file:
            data.append(list(line.strip()))
    return data


def is_horizontal_fw(data, i, j):
    if j+3 > len(data[i]) - 1:
        return False
    elif list(data[i][j:j+4]) == ['X', 'M', 'A', 'S']:
        return True
    

def is_horizontal_bw(data, i, j):
    if j-3 < 0:
        return False
    elif list(data[i][j-3:j+1]) == ['S', 'A', 'M', 'X']:
        return True


def is_vertical_dw(data, i, j):
    if i+3 > len(data) - 1:
        return False
    elif list(data[i:i+4, j]) == ['X', 'M', 'A', 'S']:
        return True


def is_vertical_uw(data, i, j):
    if i-3 < 0:
        return False
    elif list(data[i-3:i+1, j]) == ['S', 'A', 'M', 'X']:
        return True
    

def is_diagonal_up_right(data, i, j):
    if i-3 < 0 or j+3 > len(data) - 1:
        return False
    word_list = list()
    while len(word_list) < 4:
        word_list.append(str(data[i, j]))
        i -= 1
        j += 1
    if word_list == ['X', 'M', 'A', 'S']:
        return True


def is_diagonal_up_left(data, i, j):
    if i-3 < 0 or j-3 < 0:
        return False
    word_list = list()
    while len(word_list) < 4:
        word_list.append(str(data[i, j]))
        i -= 1
        j -= 1
    if word_list == ['X', 'M', 'A', 'S']:
        return True


def is_diagonal_down_right(data, i, j):
    if i+3 > len(data) - 1 or j+3 > len(data) - 1:
        return False
    word_list = list()
    while len(word_list) < 4:
        word_list.append(str(data[i, j]))
        i += 1
        j += 1
    if word_list == ['X', 'M', 'A', 'S']:
        return True
    

def is_diagonal_down_left(data, i, j):
    if i+3 > len(data) - 1 or j-3 < 0:
        return False
    word_list = list()
    while len(word_list) < 4:
        word_list.append(str(data[i, j]))
        i += 1
        j -= 1
    if word_list == ['X', 'M', 'A', 'S']:
        return True


def is_x_mas(data, i, j):
    if i-1 < 0 or i+1 > len(data[i]) - 1 or j-1 < 0 or j+1 > len(data) - 1:
        return False
    elif ((data[i-1, j-1] == 'M' and data[i+1, j+1] == 'S') or (data[i-1, j-1] == 'S' and data[i+1, j+1] == 'M')) and ((data[i+1, j-1] == 'M' and data[i-1, j+1] == 'S') or (data[i+1, j-1] == 'S' and data[i-1, j+1] == 'M')):
        return True


def main():
    data = get_input(is_test=False)
    data_array = np.array(data)

    rows, indx = np.where(data_array == 'X')
    x_index = np.array((rows, indx)).T

    counter = 0
    for X in x_index:
        if is_horizontal_fw(data_array, X[0], X[1]):
            counter += 1
        if is_horizontal_bw(data_array, X[0], X[1]):
            counter += 1
        if is_vertical_dw(data_array, X[0], X[1]):
            counter += 1
        if is_vertical_uw(data_array, X[0], X[1]):
            counter += 1
        if is_diagonal_up_right(data_array, X[0], X[1]):
            counter += 1
        if is_diagonal_up_left(data_array, X[0], X[1]):
            counter += 1
        if is_diagonal_down_right(data_array, X[0], X[1]):
            counter += 1
        if is_diagonal_down_left(data_array, X[0], X[1]):
            counter += 1

    print(f"Answer to part 1 is: {counter}")

    rows, indx = np.where(data_array == 'A')
    a_index = np.array((rows, indx)).T

    counter = 0
    for A in a_index:
        if is_x_mas(data_array, A[0], A[1]):
            counter += 1

    print(f"Answer to part 2 is: {counter}")


if __name__ == "__main__":
    main()