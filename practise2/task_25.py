#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_2_2():

    def fill_star():

        def fill_current_cell():
            fill_cell()
            return False

        for direction in range(1,5):
            move(direction,1,fill_current_cell)
            move(get_reverse_direction(direction),1,fill_current_cell)


    for i in range(5):
        move(3,4 if i!=0 else 1)
        move(4,2)
        fill_star()
        move(2,2)

    move(1,1)
    move(4,1)



if __name__ == '__main__':
    run_tasks()
