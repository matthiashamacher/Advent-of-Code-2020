def main(data):
    return function(data)


def test(data):
    return function(data)


def function(expenses):
    sum = 0
    base = 0
    second_value = 0

    for base in expenses.entries:
        for second_value in expenses.entries:
            sum = base + second_value

            if sum == 2020:
                break

        if sum == 2020:
            break

    return base * second_value
