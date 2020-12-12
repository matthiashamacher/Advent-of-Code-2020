import day11.day_functions
import copy


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    seat_map = day11.day_functions.get_seat_map(input)
    changed = True
    occupied_seats = 0

    while changed:
        changed = False
        temp_seat_map = copy.deepcopy(seat_map)

        for row_index in seat_map:
            row = seat_map[row_index]

            for col in row:
                seat = row[col]
                occupied = 0

                if seat == '.':
                    continue

                if col != 0:
                    for l in range(col-1, -1, -1):
                        if row[l] == '#':
                            occupied += 1
                            break
                        elif row[l] == 'L':
                            break

                        l -= 1

                if col != len(row):
                    for r in range(col+1, len(row)):
                        if row[r] == '#':
                            occupied += 1
                            break
                        elif row[r] == 'L':
                            break

                        r += 1

                if row_index != 0:
                    top = False
                    right = False
                    left = False
                    sub = 1
                    add = 1

                    for t in range(row_index-1, -1, -1):
                        new_row = seat_map[t]

                        if not top:
                            if new_row[col] == '#':
                                occupied += 1
                                top = True
                            elif new_row[col] == 'L':
                                top = True

                        if not left:
                            if col != 0:
                                if col - sub in new_row:
                                    if new_row[col - sub] == '#':
                                        occupied += 1
                                        left = True
                                    elif new_row[col - sub] == 'L':
                                        left = True
                                    else:
                                        sub += 1
                            else:
                                left = True

                        if not right:
                            if col != len(new_row):
                                if col + add in new_row:
                                    if new_row[col + add] == '#':
                                        occupied += 1
                                        right = True
                                    elif new_row[col + add] == 'L':
                                        right = True
                                    else:
                                        add += 1
                            else:
                                right = True

                        if top and left and right:
                            break

                        t -= 1

                if row_index != len(seat_map):
                    bottom = False
                    right = False
                    left = False
                    sub = 1
                    add = 1

                    for b in range(row_index+1, len(seat_map)):
                        new_row = seat_map[b]

                        if not bottom:
                            if new_row[col] == '#':
                                occupied += 1
                                bottom = True
                            elif new_row[col] == 'L':
                                bottom = True

                        if not left:
                            if col != 0:
                                if col-sub in new_row:
                                    if new_row[col-sub] == '#':
                                        occupied += 1
                                        left = True
                                    elif new_row[col-sub] == 'L':
                                        left = True
                                    else:
                                        sub += 1
                            else:
                                left = True

                        if not right:
                            if col != len(new_row):
                                if col+add in new_row:
                                    if new_row[col+add] == '#':
                                        occupied += 1
                                        right = True
                                    elif new_row[col+add] == 'L':
                                        right = True
                                    else:
                                        add += 1
                            else:
                                right = True

                        if bottom and left and right:
                            break

                        b += 1

                if seat == 'L' and occupied == 0:
                    occupied_seats += 1
                    temp_seat_map[row_index][col] = '#'
                    changed = True
                elif seat == '#' and occupied >= 5:
                    occupied_seats -= 1
                    temp_seat_map[row_index][col] = 'L'
                    changed = True

        seat_map = temp_seat_map

    return occupied_seats
