#!/usr/bin/python3

from pyrob.api import *
from practise2.actions import *

@task
def task_7_5():

    # for i in range(1,5):
    #     move(3,1)
    #     fill_cell()

    def fib(n):

        f0 = 0
        f1 = 1
        for i in range(n):
            f2 = f0 + f1
            f0 = f1
            f1 = f2

        return f0

    print(fib(6))


if __name__ == '__main__':
    run_tasks()
