#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    def above():
        move_up()
        fill_cell()
        move_down()
    def beneath():
        move_down()
        fill_cell()
        move_up()
	
    def rr():
        if not wall_is_above():
            above()
        if not wall_is_beneath():
            beneath()
        if wall_is_beneath() and wall_is_above():
            fill_cell()

    while not wall_is_on_the_right():
        rr()
        move_right()
    rr()
    
        
            


if __name__ == '__main__':
    run_tasks()
