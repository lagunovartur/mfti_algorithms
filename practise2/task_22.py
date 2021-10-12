#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_5_10():

    def draw():
        fill_cell()
        return False

    i=1

    while not (wall_is_on_direction(3) and  wall_is_on_direction(4)):
        if i%2:
            move(3,stop=draw)
        else:
            move(1,stop=draw)
        move(4,1)
        i+=1

    move(1,stop=draw)

if __name__ == '__main__':
    run_tasks()
