from pyrob.api import *


def move(direction, distance=0, stop=None, chek_wall=True):
    steps_taken = 0

    if direction == 1:
        move_to = move_left
        check_wall_func = wall_is_on_the_left
    elif direction == 2:
        move_to = move_up
        check_wall_func = wall_is_above
    elif direction == 3:
        move_to = move_right
        check_wall_func = wall_is_on_the_right
    elif direction == 4:
        move_to = move_down
        check_wall_func = wall_is_beneath

    if not chek_wall:
        check_wall_func = lambda: False

    while True:

        if stop and stop():
            break

        if check_wall_func():
            break

        if steps_taken >= distance and distance:
            break

        move_to(n=1)
        steps_taken += 1

    return steps_taken


def get_direction(excluding=0):

    for direction in range(1,5):
        if not wall_is_on_direction(direction) and not excluding==direction and not (isinstance(excluding,list) and excluding.find(direction)):
            return direction


def wall_is_on_direction(direction):

    if direction == 1:
        return wall_is_on_the_left()
    elif direction == 2:
        return wall_is_above()
    elif direction == 3:
        return wall_is_on_the_right()
    elif direction ==4:
        return wall_is_beneath()


def get_reverse_direction(direction):

    if direction == 1:
        return 3
    elif direction == 3:
        return 1
    elif direction == 2:
        return 4
    elif direction == 4:
        return 2