#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down(n=2)
    for i in range(3):
        fill_cell()
        move_right()
    move_down()
    move_left(n=2)
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_right(n=3)
    move_down()

    for i in range(3):
        fill_cell()
        move_right()
    move_down()
    move_left(n=2)
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_right(n=3)
    move_down()

    for i in range(3):
        fill_cell()
        move_right()
    move_down()
    move_left(n=2)
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_right(n=3)
    move_down()

    for i in range(3):
        fill_cell()
        move_right()
    move_down()
    move_left(n=2)
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_right(n=3)
    move_down()

    for i in range(2):
        fill_cell()
        move_right()
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_up(n=2)
    fill_cell()
    move_left()


if __name__ == '__main__':
    run_tasks()
