from part1 import read_file_to_list, get_all_seat_ids


def find_my_seat(seat_ids, max_seat_id):
    seat_ids.sort()
    for id in range(max_seat_id):
        if (id + 1) in seat_ids and (id - 1) in seat_ids and id not in seat_ids:
            return id


def main():
    boarding_passes = read_file_to_list('input5.txt')
    seat_ids = get_all_seat_ids(boarding_passes)
    max_seat_id = max(seat_ids)
    my_seat_id = find_my_seat(seat_ids, max_seat_id)
    print(my_seat_id)


if __name__ == "__main__":
    main()