import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    seats = functions.get_data_from_string(input)
    seat_ids = []
    missing_seat_id = 0

    for seat in seats:
        seat_desc = functions.split_string(seat)
        lowest_row = 0
        highest_row = 127
        lowest_col = 0
        highest_col = 7
        rows = 128
        cols = 8
        row = 0
        col = 0

        for direction in seat_desc:
            if direction == 'F':
                rows /= 2
                highest_row -= rows
            elif direction == 'B':
                rows /= 2
                lowest_row += rows
            elif direction == 'R':
                cols /= 2
                lowest_col += cols
            elif direction == 'L':
                cols /= 2
                highest_col -= cols

        if highest_col == lowest_col:
            col = highest_col

        if highest_row == lowest_row:
            row = highest_row

        seat_id = row * 8 + col
        seat_ids.append(int(seat_id))

    sorted_seat_ids = sorted(seat_ids)

    for i in range(sorted_seat_ids[0], sorted_seat_ids[-1] + 1):
        if i not in sorted_seat_ids:
            missing_seat_id = i
            break

    return missing_seat_id
