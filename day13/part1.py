import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    data = functions.get_data_from_string(input)

    if not data:
        return 0

    [arrive_timestamp, bus_lines_string] = data
    bus_lines = functions.get_data_from_string(bus_lines_string, ',')
    selected_bus_line = 0
    wait_minutes = 0

    for bus_line in bus_lines:
        if bus_line == 'x':
            continue

        depart_time = int(bus_line)
        previous_depart_minutes = int(arrive_timestamp) % depart_time
        last_depart = int(arrive_timestamp) - previous_depart_minutes

        next_depart = last_depart + depart_time
        possible_wait_minutes = next_depart - int(arrive_timestamp)

        if selected_bus_line == 0 or possible_wait_minutes < wait_minutes:
            selected_bus_line = depart_time
            wait_minutes = possible_wait_minutes

    return selected_bus_line * wait_minutes
