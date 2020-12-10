import functions
import collections


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def test_second_data(data):
    return function(data.second_data)


def function(input):
    jolts = list(map(int, sorted(functions.get_data_from_string(input), key=int)))
    possibilities = collections.defaultdict(int)
    possibilities[0] = 1

    for number in jolts:
        possibilities[number] = possibilities[number-1] + possibilities[number-2] + possibilities[number-3]

    return possibilities[max(jolts)]

