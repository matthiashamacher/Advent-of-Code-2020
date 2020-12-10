import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def test_second_data(data):
    return function(data.second_data)


def function(input):
    jolts = list(map(int, sorted(functions.get_data_from_string(input), key=int)))
    one_jolt_diff = 1
    three_jolt_diff = 1

    for i, jolt in enumerate(jolts):
        if (i + 1) >= len(jolts):
            break

        diff = jolts[i+1] - jolt

        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        elif diff > 3:
            break

    return one_jolt_diff * three_jolt_diff
