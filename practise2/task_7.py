#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_5_4():

    move(4,chek_wall=True)
    move(3, stop=lambda:not wall_is_beneath())
    move(4, 1)
    move(1,chek_wall=True)

if __name__ == '__main__':
    run_tasks()
