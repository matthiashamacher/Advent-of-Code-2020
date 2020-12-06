import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    seats = functions.get_data_from_string(input)
    highest_seat_id = 0

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

        if seat_id > highest_seat_id:
            highest_seat_id = int(seat_id)

    return highest_seat_id
