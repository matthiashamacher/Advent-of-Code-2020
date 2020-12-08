import functions
import re


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    instructions = functions.get_data_from_string(input)
    accumulator = 0
    length = len(instructions)
    i = 0
    pos = []

    if length < 1:
        return accumulator

    while i < length:
        if i in pos:
            break

        pos.append(i)
        [operation, argument] = functions.get_data_from_string(instructions[i], ' ')
        argument_parts = re.match('(\+|-)([0-9]+)', argument, re.I).groups()
        [operator, number] = argument_parts

        if operation == 'acc':
            if operator == '+':
                accumulator += int(number)
            elif operator == '-':
                accumulator -= int(number)
        elif operation == 'jmp':
            if operator == '+':
                i += int(number)
            elif operator == '-':
                i -= int(number)

        if operation != 'jmp':
            i += 1

    return accumulator
