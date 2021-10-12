#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_3():

    def stop_func():
        if wall_is_above() or wall_is_beneath():
            fill_cell()
            return False
        else:
            return False

    move(3, stop=stop_func)


if __name__ == '__main__':
    run_tasks()
