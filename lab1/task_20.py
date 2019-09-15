#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    def kmb():
        for k in range(26):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        for k in range(26):
            fill_cell()
            move_left()
        fill_cell()
        move_down()
    
    move_right()
    for i in range(5):
        kmb()

    kmb()
    
        

if __name__ == '__main__':
    run_tasks()
