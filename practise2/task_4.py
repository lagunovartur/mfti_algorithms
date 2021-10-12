#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_3_3():
    for direction in range(1,5):
        if move(direction, 1, chek_wall=True):
            break


if __name__ == '__main__':
    run_tasks()
