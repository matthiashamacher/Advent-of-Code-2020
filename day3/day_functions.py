import functions


def get_map_array(map):
    array = []

    for map_row in map:
        array.append(functions.split_string(map_row))

    return array


def get_map_array_relevant_rows(map):
    array = get_map_array(map)

    return array[1::2]
