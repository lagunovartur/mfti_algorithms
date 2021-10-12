#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_8_28():

    def up_move():
        move(2)
        return False


    move(3,stop=up_move)
    move(1,stop=up_move)


if __name__ == '__main__':
    run_tasks()
