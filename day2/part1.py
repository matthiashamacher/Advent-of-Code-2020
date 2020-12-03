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
        [min, max] = parts[0].split('-')
        letter = parts[1].strip(':')
        password_letters = functions.split_string(parts[2])
        letters_count = 0

        for password_letter in password_letters:
            if password_letter != letter:
                continue

            letters_count += 1
            if letters_count > int(max):
                break

        if int(max) >= letters_count >= int(min):
            valid_passwords += 1

    return valid_passwords
