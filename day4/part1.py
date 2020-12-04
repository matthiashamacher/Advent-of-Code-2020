import functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    passports = functions.get_data_from_string(input, '\n\n')
    valid = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

    if len(passports) <= 1:
        return 0

    for passport in passports:
        lines = functions.get_data_from_string(passport)
        key_value_pair_strings = []
        key_value_pairs = []
        keys = []
        invalid = False

        for line in lines:
            data = functions.get_data_from_string(line, ' ')

            for string in data:
                key_value_pair_strings.append(string)

        for key_value_pair_string in key_value_pair_strings:
            key_value_pairs.append(functions.get_data_from_string(key_value_pair_string, ':'))

        for key_value_pair in key_value_pairs:
            [key, value] = key_value_pair
            keys.append(key)

        for required_field in required_fields:
            if required_field not in keys:
                if required_field == 'cid':
                    continue
                else:
                    invalid = True
                    break

        if not invalid:
            valid += 1

    return valid
