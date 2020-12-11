import functions
import day_functions
import copy


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    seat_map = day_functions.get_seat_map(input)
    changed = True
    occupied_seats = 0

    while changed:
        changed = False
        temp_seat_map = copy.deepcopy(seat_map)

        for row in seat_map:
            for col in seat_map[row]:
                seat = seat_map[row][col]
                occupied = 0

                if seat == '.':
                    continue

                if row - 1 in seat_map:
                    if seat_map[row-1][col] == '#':
                        occupied += 1
                    if col - 1 in seat_map[row-1] and seat_map[row-1][col-1] == '#':
                        occupied += 1
                    if col + 1 in seat_map[row-1] and seat_map[row-1][col+1] == '#':
                        occupied += 1

                if col - 1 in seat_map[row] and seat_map[row][col - 1] == '#':
                    occupied += 1

                if col + 1 in seat_map[row] and seat_map[row][col + 1] == '#':
                    occupied += 1

                if row + 1 in seat_map:
                    if seat_map[row+1][col] == '#':
                        occupied += 1
                    if col - 1 in seat_map[row+1] and seat_map[row+1][col-1] == '#':
                        occupied += 1
                    if col + 1 in seat_map[row+1] and seat_map[row+1][col+1] == '#':
                        occupied += 1

                if seat == 'L' and occupied == 0:
                    occupied_seats += 1
                    temp_seat_map[row][col] = '#'
                    changed = True
                elif seat == '#' and occupied >= 4:
                    occupied_seats -= 1
                    temp_seat_map[row][col] = 'L'
                    changed = True

        seat_map = temp_seat_map

    return occupied_seats


