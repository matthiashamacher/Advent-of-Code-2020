import functions
import re
import day12.day_functions


def main(data):
    return function(data.data)


def test(data):
    return function(data.data)


def function(input):
    instructions = functions.get_data_from_string(input)
    waypoint_north = 1
    waypoint_east = 10
    waypoint_south = 0
    waypoint_west = 0
    north = 0
    east = 0
    south = 0
    west = 0

    for instruction in instructions:
        [direction, steps] = re.match('([NSEWLRF])([0-9]+)', instruction, re.I).groups()
        steps = int(steps)

        if direction == 'F':
            if waypoint_north != 0:
                (north, south) = day12.day_functions.update_two_directions(north, south, waypoint_north * steps)
            if waypoint_east != 0:
                (east, west) = day12.day_functions.update_two_directions(east, west, waypoint_east * steps)
            if waypoint_south != 0:
                (south, north) = day12.day_functions.update_two_directions(south, north, waypoint_south * steps)
            if waypoint_west != 0:
                (west, east) = day12.day_functions.update_two_directions(west, east, waypoint_west * steps)
        elif direction == 'N':
            if waypoint_south != 0:
                if waypoint_south - steps < 0:
                    steps -= waypoint_south
                    waypoint_south = 0
                    waypoint_north += steps
                else:
                    waypoint_south -= steps
            else:
                waypoint_north += steps
        elif direction == 'E':
            if waypoint_west != 0:
                if waypoint_west - steps < 0:
                    steps -= waypoint_west
                    waypoint_west = 0
                    waypoint_east += steps
                else:
                    waypoint_west -= steps
            else:
                waypoint_east += steps
        elif direction == 'S':
            if waypoint_north != 0:
                if waypoint_north - steps < 0:
                    steps -= waypoint_north
                    waypoint_north = 0
                    waypoint_south += steps
                else:
                    waypoint_north -= steps
            else:
                waypoint_south += steps
        elif direction == 'W':
            if waypoint_east != 0:
                if waypoint_east - steps < 0:
                    steps -= waypoint_east
                    waypoint_east = 0
                    waypoint_west += steps
                else:
                    waypoint_east -= steps
            else:
                waypoint_west += steps
        elif direction == 'R':
            tmp_north = waypoint_north
            tmp_east = waypoint_east
            tmp_south = waypoint_south
            tmp_west = waypoint_west

            if steps == 90:
                waypoint_north = tmp_west
                waypoint_east = tmp_north
                waypoint_south = tmp_east
                waypoint_west = tmp_south
            elif steps == 180:
                waypoint_north = tmp_south
                waypoint_east = tmp_west
                waypoint_south = tmp_north
                waypoint_west = tmp_east
            elif steps == 270:
                waypoint_north = tmp_east
                waypoint_east = tmp_south
                waypoint_south = tmp_west
                waypoint_west = tmp_north
        elif direction == 'L':
            tmp_north = waypoint_north
            tmp_east = waypoint_east
            tmp_south = waypoint_south
            tmp_west = waypoint_west

            if steps == 90:
                waypoint_north = tmp_east
                waypoint_east = tmp_south
                waypoint_south = tmp_west
                waypoint_west = tmp_north
            elif steps == 180:
                waypoint_north = tmp_south
                waypoint_east = tmp_west
                waypoint_south = tmp_north
                waypoint_west = tmp_east
            elif steps == 270:
                waypoint_north = tmp_west
                waypoint_east = tmp_north
                waypoint_south = tmp_east
                waypoint_west = tmp_south

    return north + east + south + west
