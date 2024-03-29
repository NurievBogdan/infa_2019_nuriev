#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_on_the_right():
        while not wall_is_beneath():
            fill_cell()
            move_down()
        fill_cell()
        move_right()
        while not wall_is_above():
            fill_cell()
            move_up()
    fill_cell()
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        move_down()
    


if __name__ == '__main__':
    run_tasks()
