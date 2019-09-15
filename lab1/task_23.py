#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    count=0
    while not ( wall_is_beneath() and  wall_is_on_the_right() ):
        move_right()
        count+=1
        while wall_is_above() and not wall_is_on_the_right() :
            move_right()
            count+=1
        while not wall_is_above():
            move_up()
            fill_cell()
        while not wall_is_beneath():
            move_down()
    move_left(count)

    
        
    


if __name__ == '__main__':
    run_tasks()
