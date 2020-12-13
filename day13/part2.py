import functions


def main(data):
    return function(data.data, 100000000000000)


def test(data):
    return function(data.data)


def function(input, higher_than=0):
    data = functions.get_data_from_string(input)

    if not data:
        return 0

    bus_lines = functions.get_data_from_string(data[1], ',')
    length = len(bus_lines)
    i = 1
    add = 0

    if higher_than != 0:
        previous_minutes = higher_than % int(bus_lines[0])
        previous_departure = higher_than - previous_minutes
        timestamp = previous_departure + int(bus_lines[0])
    else:
        timestamp = int(bus_lines[0])

    while i < length:
        add += 1

        if bus_lines[i] == 'x':
            i += 1
            continue

        last_timestamp = timestamp + (length - 1)

        if last_timestamp % int(bus_lines[length-1]) != 0:
            i = 1
            add = 0
            timestamp += int(bus_lines[0])
            continue

        next_timestamp = timestamp + add

        if next_timestamp % int(bus_lines[i]) == 0:
            i += 1
        else:
            i = 1
            add = 0
            timestamp += int(bus_lines[0])

    return timestamp
