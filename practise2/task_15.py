#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_21():

    if wall_is_on_the_left() and wall_is_beneath():
        move(3)
        move(2)
    elif wall_is_on_the_right() and wall_is_beneath():
        move(1)
        move(2)
    elif wall_is_on_the_left() and wall_is_above():
        move(3)
        move(4)
    elif wall_is_on_the_right() and wall_is_above():
        move(1)
        move(4)


if __name__ == '__main__':
    run_tasks()
