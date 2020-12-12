def update_two_directions(direction, opposite_direction, value):
    if opposite_direction != 0:
        if opposite_direction - value < 0:
            value -= opposite_direction
            opposite_direction = 0
            direction += value
        else:
            opposite_direction -= value
    else:
        direction += value

    return direction, opposite_direction
