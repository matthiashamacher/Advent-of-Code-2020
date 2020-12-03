import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    map = functions.get_data_from_string(input)
    slopes = [
        [
            1,
            1
        ],
        [
            3,
            1
        ],
        [
            5,
            1
        ],
        [
            7,
            1
        ],
        [
            1,
            2
        ]
    ]
    length = 0
    trees_per_slope = []

    for slope in slopes:
        [right, down] = slope
        trees = 0
        pos = 1
        downwards = 0

        for i in range(len(map)):
            if length == 0:
                length = len(map[i])

            if length < pos:
                pos -= length

            if i == 0:
                pos += right
                downwards += 1
                continue

            if downwards < down:
                downwards += 1
                continue
            else:
                downwards = 0

            map_elements = functions.split_string(map[i])

            map_element = map_elements[pos - 1]

            if map_element == '#':
                trees += 1

            pos += right
            downwards += 1

        trees_per_slope.append(trees)

    result = 1

    for trees in trees_per_slope:
        result *= trees

    return result
