#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_right()
    for j in range(4):
        for k in range(9):
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
            move_right(5)


            
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
        move_right()
        move_down(4)
        move_left(36)


    for k in range(9):
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
        move_right(5)


    
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
    move_right()
    move_left(37)
    


if __name__ == '__main__':
    run_tasks()
