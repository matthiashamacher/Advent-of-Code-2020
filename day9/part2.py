import functions


def main(data):
    return function(data.data, 21806024)


def test(data):
    return function(data.data, 127)


def function(input, invalid_number):
    numbers = functions.get_data_from_string(input)
    length = len(numbers)
    i = 0
    smallest_number = 0
    largest_number = 0

    while i < length:
        sum = int(numbers[i])
        smallest_number = int(numbers[i])
        j = i + 1

        while j < length:
            sum += int(numbers[j])

            if sum > invalid_number:
                break

            if int(numbers[j]) > largest_number:
                largest_number = int(numbers[j])

            if int(numbers[j]) < smallest_number:
                smallest_number = int(numbers[j])

            if sum == invalid_number:
                break

            j += 1

        if sum == invalid_number:
            break

        i += 1

    return smallest_number + largest_number
