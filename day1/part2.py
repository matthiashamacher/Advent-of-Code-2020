def main(data):
    return function(data)


def test(data):
    return function(data)


def function(expenses):
    endSum = 0
    base = 0
    second_value = 0
    third_value = 0

    for base in expenses.entries:
        for second_value in expenses.entries:
            sum = base + second_value

            if sum >= 2020:
                continue

            for third_value in expenses.entries:
                endSum = sum + third_value

                if endSum == 2020:
                    break

            if endSum == 2020:
                break

        if endSum == 2020:
            break

    return base * second_value * third_value
