#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_27():
    move(2,stop=lambda : cell_is_filled())
    move(1,1)
    if not cell_is_filled():
        move(3,2)


if __name__ == '__main__':
    run_tasks()
