#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_22():
    direction = get_direction()
    move(direction)
    direction = get_direction(direction)
    move(direction)

if __name__ == '__main__':
    run_tasks()
