import functions
import day3.day_functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    map = functions.get_data_from_string(input)
    length = 0
    trees = 0
    pos = 1

    for i in range(len(map)):
        if length == 0:
            length = len(map[i])

        if length < pos:
            pos -= length

        if i == 0:
            pos += 3
            continue

        map_elements = functions.split_string(map[i])

        map_element = map_elements[pos - 1]

        if map_element == '#':
            trees += 1

        pos += 3

    return trees
