#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    for i in range(12):
        s=0
        k=0
        fill_cell()
        move_down()
        while s != i+1:
            s+=1
            fill_cell()
            move_right()
        fill_cell()
        while k != i+1:
            k+=1
            move_left()
    move_down()


if __name__ == '__main__':
    run_tasks()
