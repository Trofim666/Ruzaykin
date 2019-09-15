#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down()
    def kek():
        for i in range(2):
            fill_cell()
            move_down()
        fill_cell()
        move_up()
        move_right()
        for i in range(2):
            fill_cell()
            move_left()
        fill_cell()
        move_up()
        
    for k in range(4):
        kek()
        move_right(5)
    kek()


    


if __name__ == '__main__':
    run_tasks()
