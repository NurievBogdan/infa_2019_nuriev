from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)

colors = ['red', 'orange', 'green', 'lightblue', 'blue', 'purple']
skorost = [1, 2, -1, -2] 

class Ball:

    def __init__(self, name):
    	self.name = name
    	self.x = rnd(100, 700)
    	self.y = rnd(100, 420)
    	self.vx = choice(skorost)
    	self.vy = choice(skorost)
    	self.r = rnd(30, 50)
    	self.id = None
    	self.color = None


    def draw(self):
    	self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=self.color, width=0)

    def update(self):
    	canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
    	canv.update()

    def move(self):
    	global balls1, balls2, quantity 
    	self.x += self.vx
    	self.y += self.vy
    	if self.x + self.r >= 800 or self.x - self.r <= 0:
    		self.vx = -self.vx
    	if self.y + self.r >= 460 or self.y - self.r <= 0:
    		self.vy = -self.vy
    	self.update()
    	root.after(1, self.move)


class Ball1(Ball):
	def initialization(self):
		self.color = red

	def move_plus(self):
		global balls1, balls2, quantity 
		for i in range(quantity):
			for j in range(quantity):
				if( ( ( (balls1[i].x - balls2[j].x)**2 + (balls1[i].y - balls2[j].y)**2))**0.5 <= balls1[i].r + balls2[j].r):
					balls1[i].vx *= -1
					balls1[i].vy *= -1
					balls2[j].vx *= -1
					balls2[j].vy *= -1
			for i in range(quantity):
				for j in range(quantity):
					if( ( ( (balls1[i].x - balls1[j].x)**2 + (balls1[i].y - balls1[j].y)**2))**0.5 <= balls1[i].r + balls1[j].r):
						balls1.remove(balls1[i])
						balls1.remove(balls1[j])

class Ball2(Ball):
	def initialization(self):
		self.color = blue

	def move_plus(self):
		for i in range(quantity):
			for j in range(quantity):
				if( ( ( (balls2[i].x - balls2[j].x)**2 + (balls2[i].y - balls2[j].y)**2))**0.5 <= balls2[i].r + balls2[j].r):
					balls2.remove(balls2[i])
					balls2.remove(balls2[j])
balls1 = []
balls2 = []

quantity = rnd(2, 5)

for i in range(quantity):
	ball1 = Ball1(name=('ball1' + str(i)))
	balls1.append(ball1)
for ball1 in balls1:
	ball1.draw()
	ball1.move()

for i in range(quantity):
	ball2 = Ball2(name=('ball2' + str(i)))
	balls2.append(ball2)
for ball2 in balls2:
	ball2.draw()
	ball2.move()

for ball1 in balls1:
	ball1.move_plus()
for ball2 in balls2:
	ball2.move_plus()



tk.mainloop()