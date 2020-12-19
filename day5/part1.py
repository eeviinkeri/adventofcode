def find_seat(boarding_pass_end):
    seats = [i for i in range(8)]
    low = 0
    high = len(seats) - 1
    for char in boarding_pass_end:
        middle = (high + low) // 2
        if char == 'R':
            low = middle
        if char == 'L':
            high = middle 
    return high


def find_row(boarding_pass_start):
    rows = [i for i in range(128)]
    low = 0
    high = len(rows) - 1
    for char in boarding_pass_start:
        middle = (high + low) // 2
        if char == 'F':
            high = middle
        if char == 'B':
            low = middle + 1
    return low


def get_seat_id(boarding_pass):
    row = find_row(boarding_pass[:7])
    seat = find_seat(boarding_pass[7:])
    return row * 8 + seat


def read_file_to_list(filename):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f]


def main():
    data = read_file_to_list('input5.txt')

    seat_ids = list()
    for boarding_pass in data:
        seat_id = get_seat_id(boarding_pass)
        seat_ids.append(seat_id)
    
    max_seat_id = max(seat_ids)
    print(max_seat_id)
            

if __name__ == "__main__":
    main()