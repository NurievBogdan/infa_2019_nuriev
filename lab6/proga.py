from tkinter import *
from random import randrange as rnd, choice
import time
from math import *

root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')

canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']

global score
score=0
vx=1
vy=2
x = rnd(100,700)
y = rnd(100,500)
r = rnd(30,50)

color1 = choice(colors)
def new_ball():
    global x,y,r,vx,vy
    canv.delete(ALL)
    if (x + r) > 700  or x < r :
    	vx = -vx
    if (y + r) > 500  or y < r :
    	vy = -vy
    x += vx
    y += vy
    canv.create_oval(x-r,y-r,x+r,y+r,fill = color1, width=0)
    root.after(10,new_ball)



def click_score(event):
	global score
	l_ot_cliсka_do_sharika=sqrt((y-event.y)**2+(x-event.x)**2)
	if l_ot_cliсka_do_sharika<=r :
		score+=1
		print("score:", score)




new_ball()

score=0
canv.bind('<Button-1>', click_score)
mainloop()
