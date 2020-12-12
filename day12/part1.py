import functions
import re
import day12.day_functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    instructions = functions.get_data_from_string(input)
    north = 0
    east = 0
    south = 0
    west = 0
    direction_1 = 'east'
    direction_2 = ''

    for instruction in instructions:
        [direction, steps] = re.match('([NSEWLRF])([0-9]+)', instruction, re.I).groups()
        steps = int(steps)

        if direction == 'F':
            if direction_1 == 'north':
                (north, south) = day12.day_functions.update_two_directions(north, south, steps)
            elif direction_1 == 'east':
                (east, west) = day12.day_functions.update_two_directions(east, west, steps)
            elif direction_1 == 'south':
                (south, north) = day12.day_functions.update_two_directions(south, north, steps)
            elif direction_1 == 'west':
                (west, east) = day12.day_functions.update_two_directions(west, east, steps)
        elif direction == 'N':
            if direction_1 == 'north':
                (north, south) = day12.day_functions.update_two_directions(north, south, steps)
            elif direction_1 == 'south':
                if south != 0:
                    if south - steps < 0:
                        steps -= south
                        south = 0
                        north += steps
                        direction_1 = 'north'
                    else:
                        south -= steps
                else:
                    north += steps
            elif direction_2 == '':
                direction_2 = 'north'
                north += steps
            else:
                if south != 0:
                    if south - steps < 0:
                        steps -= south
                        south = 0
                        north += steps
                        direction_2 = 'north'
                    else:
                        south -= steps
                else:
                    north += steps
                    direction_2 = 'north'
        elif direction == 'E':
            if direction_1 == 'east':
                (east, west) = day12.day_functions.update_two_directions(east, west, steps)
            elif direction_1 == 'west':
                if west != 0:
                    if west - steps < 0:
                        steps -= west
                        west = 0
                        east += steps
                        direction_1 = 'east'
                    else:
                        west -= steps
                else:
                    east += steps
            elif direction_2 == '':
                direction_2 = 'east'
                east += steps
            else:
                if west != 0:
                    if west - steps < 0:
                        steps -= west
                        west = 0
                        east += steps
                        direction_2 = 'east'
                    else:
                        west -= steps
                else:
                    east += steps
                    direction_2 = 'east'
        elif direction == 'S':
            if direction_1 == 'south':
                (south, north) = day12.day_functions.update_two_directions(south, north, steps)
            elif direction_1 == 'north':
                if north != 0:
                    if north - steps < 0:
                        steps -= north
                        north = 0
                        south += steps
                        direction_1 = 'south'
                    else:
                        north -= steps
                else:
                    south += steps
            elif direction_2 == '':
                direction_2 = 'south'
                south += steps
            else:
                if north != 0:
                    if north - steps < 0:
                        steps -= north
                        north = 0
                        south += steps
                        direction_2 = 'south'
                    else:
                        north -= steps
                else:
                    south += steps
                    direction_2 = 'south'
        elif direction == 'W':
            if direction_1 == 'west':
                (west, east) = day12.day_functions.update_two_directions(west, east, steps)
            elif direction_1 == 'east':
                if east != 0:
                    if east - steps < 0:
                        steps -= east
                        east = 0
                        west += steps
                        direction_1 = 'west'
                    else:
                        east -= steps
                else:
                    west += steps
            elif direction_2 == '':
                direction_2 = 'west'
                west += steps
            else:
                if east != 0:
                    if east - steps < 0:
                        steps -= east
                        east = 0
                        west += steps
                        direction_2 = 'west'
                    else:
                        east -= steps
                else:
                    west += steps
                    direction_2 = 'west'
        elif direction == 'R':
            if direction_1 == 'north':
                if steps == 90:
                    direction_1 = 'east'
                elif steps == 180:
                    direction_1 = 'south'
                elif steps == 270:
                    direction_1 = 'west'
            elif direction_1 == 'east':
                if steps == 90:
                    direction_1 = 'south'
                elif steps == 180:
                    direction_1 = 'west'
                elif steps == 270:
                    direction_1 = 'north'
            elif direction_1 == 'south':
                if steps == 90:
                    direction_1 = 'west'
                elif steps == 180:
                    direction_1 = 'north'
                elif steps == 270:
                    direction_1 = 'east'
            elif direction_1 == 'west':
                if steps == 90:
                    direction_1 = 'north'
                elif steps == 180:
                    direction_1 = 'east'
                elif steps == 270:
                    direction_1 = 'south'
        elif direction == 'L':
            if direction_1 == 'north':
                if steps == 90:
                    direction_1 = 'west'
                elif steps == 180:
                    direction_1 = 'south'
                elif steps == 270:
                    direction_1 = 'east'
            elif direction_1 == 'east':
                if steps == 90:
                    direction_1 = 'north'
                elif steps == 180:
                    direction_1 = 'west'
                elif steps == 270:
                    direction_1 = 'south'
            elif direction_1 == 'south':
                if steps == 90:
                    direction_1 = 'east'
                elif steps == 180:
                    direction_1 = 'north'
                elif steps == 270:
                    direction_1 = 'west'
            elif direction_1 == 'west':
                if steps == 90:
                    direction_1 = 'south'
                elif steps == 180:
                    direction_1 = 'east'
                elif steps == 270:
                    direction_1 = 'north'

    return north + east + south + west
