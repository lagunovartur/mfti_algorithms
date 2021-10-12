#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_10():

    def stop_func():

        if not wall_is_above():
            move(2,1)
            fill_cell()
            move(4, 1)

        if not wall_is_beneath():
            move(4,1)
            fill_cell()
            move(2, 1)

        return False

    move(3,stop=stop_func)



if __name__ == '__main__':
    run_tasks()
