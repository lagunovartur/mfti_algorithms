#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_5_2():
    move(3,chek_wall=False,stop=lambda:not wall_is_beneath())



if __name__ == '__main__':
    run_tasks()
