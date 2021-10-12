#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

# from practise2.actions import *


@task
def task_3_1():
    move(3)


if __name__ == '__main__':
    run_tasks()
