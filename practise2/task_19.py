#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *


@task
def task_8_29():

    def up_move():
        move(2)
        return False

    move(3, stop=up_move)
    move(1, stop=up_move)

    impasse = True
    for i in range(1,5):
        if i == 3:
            continue
        if not wall_is_on_direction(i):
            impasse=False

    if impasse:
        move(3)



if __name__ == '__main__':
    run_tasks()
