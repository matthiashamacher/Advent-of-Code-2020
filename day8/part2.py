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
    jmps = []
    nops = []
    jumped = False
    noped = False

    if length < 1:
        return accumulator

    while i < length:
        if i in pos:
            accumulator = 0
            i = 0
            pos = []
            noped = False
            jumped = False
            continue

        pos.append(i)
        [operation, argument] = functions.get_data_from_string(instructions[i], ' ')
        old_operation = operation
        argument_parts = re.match('(\+|-)([0-9]+)', argument, re.I).groups()
        [operator, number] = argument_parts

        if operation == 'acc':
            if operator == '+':
                accumulator += int(number)
            elif operator == '-':
                accumulator -= int(number)

        if operation == 'nop':
            if i not in nops and not noped and not jumped:
                operation = 'jmp'
                noped = True
                nops.append(i)

        if operation == 'jmp':
            if i not in jmps and not jumped and not noped and old_operation != 'nop':
                jmps.append(i)
                i += 1
                jumped = True
            else:
                if operator == '+':
                    i += int(number)
                elif operator == '-':
                    i -= int(number)

        if operation != 'jmp':
            i += 1

    return accumulator
