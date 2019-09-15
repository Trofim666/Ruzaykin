#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    if wall_is_beneath() and wall_is_on_the_right():
        fill_cell()
    else:
        while  True :
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            if wall_is_beneath() and wall_is_on_the_right() :
                 break
            fill_cell()
            move_down()
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            fill_cell()
            if wall_is_beneath() and wall_is_on_the_left() :
                break
            move_down()
        if wall_is_on_the_right():
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
        
            


if __name__ == '__main__':
    run_tasks()
