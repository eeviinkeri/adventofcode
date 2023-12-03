import numpy as np


def get_sum_of_unmarked_numbers(board):
    return True


def is_winner(board):
    return True


def play_one_round():
    return True


def play_bingo(numbers_drawn, bingo_boards):
    for number in numbers_drawn:
        for board in bingo_boards:
            result = play_one_round(number, board)
            if is_winner(result):
                return number, get_sum_of_unmarked_numbers(board)


def create_arrays(list_of_lists, array_size):
    arrays = []
    i = 0
    while i < len(list_of_lists) - array_size:
        arr = list_of_lists[i:i+array_size]
        arrays.append(np.array(arr))
        i += array_size
    return arrays


def filter_empty_elements(input_list):
    return [x for x in input_list if x]


def parse_bingo_boards(bingo_boards_raw):
    bingo_boards_list = filter_empty_elements(bingo_boards_raw)
    bingo_boards_list_of_lists = [
        filter_empty_elements(row.split(" ")) for row in bingo_boards_list
        ]
    bingo_board_arrays = create_arrays(bingo_boards_list_of_lists, 5)
    return bingo_board_arrays


def read_puzzle_input(filename):
    with open(filename, "r") as file:
        numbers_drawn = file.readline().split(",")
        bingo_boards = [line.strip("\n") for line in file]
    return numbers_drawn, bingo_boards


def main():
    numbers_drawn, bingo_boards = read_puzzle_input("day4/input.txt")
    bingo_boards = parse_bingo_boards(bingo_boards)

    last_called_num, unmarked_numbers_sum = play_bingo(numbers_drawn, bingo_boards)
    final_score = int(unmarked_numbers_sum) * int(last_called_num)

    print(f"The final score of bingo is {final_score}")


if __name__ == "__main__":
    main()
