import functions
import re


def main(data):
    return function(data.data)


def test(data):
    return function(data.valid_passports)


def function(input):
    passports = functions.get_data_from_string(input, '\n\n')
    valid = 0
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    if len(passports) <= 1:
        return 0

    for passport in passports:
        lines = functions.get_data_from_string(passport)
        key_value_pair_strings = []
        key_value_pairs = []
        keys = []
        values = []
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
            values.append(value)

        for required_field in required_fields:
            if required_field not in keys:
                if required_field == 'cid':
                    continue
                else:
                    invalid = True
                    break

            pos = keys.index(required_field)
            value = values[pos]

            if required_field == 'byr':
                if len(value) < 4:
                    invalid = True
                    break
                elif int(value) < 1920 or int(value) > 2002:
                    invalid = True
                    break
            elif required_field == 'iyr':
                if len(value) < 4:
                    invalid = True
                    break
                elif int(value) < 2010 or int(value) > 2020:
                    invalid = True
                    break
            elif required_field == 'eyr':
                if len(value) < 4:
                    invalid = True
                    break
                elif int(value) < 2020 or int(value) > 2030:
                    invalid = True
                    break
            elif required_field == 'hgt':
                match = re.match('([0-9]+)([a-z]+)', value, re.I)

                if not match:
                    invalid = True
                    break
                elif match[2] == 'cm' and (int(match[1]) < 150 or int(match[1]) > 193):
                    invalid = True
                    break
                elif match[2] == 'in' and (int(match[1]) < 59 or int(match[1]) > 76):
                    invalid = True
                    break
            elif required_field == 'hcl':
                match = re.match('#[0-9a-f]{6}', value, re.I)

                if not match:
                    invalid = True
                    break
            elif required_field == 'ecl':
                if value not in eye_colors:
                    invalid = True
                    break
            elif required_field == 'pid':
                if len(value) > 9 or len(value) < 9:
                    invalid = True
                    break

        if not invalid:
            valid += 1

    return valid
