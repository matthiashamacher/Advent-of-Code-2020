import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    list_entries = functions.get_data_from_string(input)
    valid_passwords = 0

    for entry in list_entries:
        parts = entry.split(' ')
        [pos1, pos2] = parts[0].split('-')
        letter = parts[1].strip(':')
        password_letters = functions.split_string(parts[2])

        if (password_letters[int(pos1) - 1] == letter and password_letters[int(pos2) - 1] != letter) or (password_letters[int(pos1) - 1] != letter and password_letters[int(pos2) - 1] == letter):
            valid_passwords += 1

    return valid_passwords
