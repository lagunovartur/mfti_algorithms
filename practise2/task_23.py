#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task(delay=0.01)
def task_6_6():

    move(3,1)

    def fill_column():

        def draw():
            if wall_is_on_direction(1) and wall_is_on_direction(3):
                fill_cell()

        move(2,stop=draw)

        move(4)


    move(3,stop=fill_column)

    move(1)
    move(3,1)


if __name__ == '__main__':
    run_tasks()
