#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_5_7():
    move(3,stop=lambda:not wall_is_beneath() and not wall_is_above())


if __name__ == '__main__':
    run_tasks()
