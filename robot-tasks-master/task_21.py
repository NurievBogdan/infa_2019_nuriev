#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for i in range(12):
        fill_cell()
        move_down()
        fill_cell()
        move_right()
    fill_cell()
    move_left(n=2)
    for i in range(10):
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    fill_cell()
    move_down(n=2)
    for i in range(8):
        fill_cell()
        move_down()
        fill_cell()
        move_right()
    fill_cell()
    move_left(n=2)
    for i in range(6):
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    fill_cell()
    move_down(n=2)
    for i in range(4):
        fill_cell()
        move_down()
        fill_cell()
        move_right()
    fill_cell()
    move_left(n=2)
    for i in range(2):
        fill_cell()
        move_left()
        fill_cell()
        move_up()
    fill_cell()
    move_down(n=2)
    fill_cell()
    move_down()

if __name__ == '__main__':
    run_tasks()
