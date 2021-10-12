#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task(delay=0.02)
def task_2_4():

    def fill_star():

        def fill_current_cell():
            fill_cell()
            return False

        for direction in range(1,5):
            move(direction,1,fill_current_cell)
            move(get_reverse_direction(direction),1,fill_current_cell)


    move(4,1)
    move(3,1)


    for j in range(2,7):

        for i in range(10):
            fill_star()
            if i != 9:
                move(1 if j % 2 else 3, 4)

        move(4,4)

    move(1)
    move(2,2)


if __name__ == '__main__':
    run_tasks()
