#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *


@task(delay=0.05)
def task_4_11():

    move(4, 1)
    move(3,1)
    fill_cell()

    max_distance = 13
    for d in range(1,max_distance):
        move(4,1)
        move(3,d)
        move(1,d,lambda : False if fill_cell() else False)

    move(4, 1)




if __name__ == '__main__':
    run_tasks()
