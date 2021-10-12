#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_2_1():

    move(3,2)
    move(4,2)

    def draw():
        fill_cell()
        return False

    def fill_star():
        for direction in range(1,5):
            move(direction,1,draw)
            move(get_reverse_direction(direction),1,draw)

    fill_star()

    move(2,1)
    move(1,1)


if __name__ == '__main__':
    run_tasks()
