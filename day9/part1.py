import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data, 5)


def function(input, preamble=25):
    numbers = functions.get_data_from_string(input)
    first_wrong_property = None
    length = len(numbers)
    i = preamble
    sum = 0

    while i < length:
        number = int(numbers[i])
        j = i - preamble
        l = i - 1

        while j < l:
            k = j + 1

            while k < i:
                sum = int(numbers[j]) + int(numbers[k])

                if sum == number:
                    break

                k += 1

            if sum == number:
                break

            j += 1

        if sum != number:
            first_wrong_property = number
            break

        i += 1

    return first_wrong_property
