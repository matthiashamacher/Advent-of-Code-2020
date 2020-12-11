import functions
import collections


def get_seat_map(input):
    rows = functions.get_data_from_string(input)
    seat_map = dict()

    for i, row in enumerate(rows):
        seat_map[i] = dict()
        seats = functions.split_string(row)

        for j, seat in enumerate(seats):
            seat_map[i][j] = seat

    return seat_map
