#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *


@task(delay=0.05)
def task_4_3():

    def stop_func():
        if not wall_is_on_the_left() and not wall_is_on_the_right():
            fill_cell()

        return False

    for i in range(1,13):
        if i % 2:
            move(3,stop=stop_func)
        else:
            move(1,stop=stop_func)
        move(4,1)

    move(3,1)


if __name__ == '__main__':
    run_tasks()
