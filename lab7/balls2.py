import tkinter as tk
from random import randrange as rnd, choice
import math

n = 0
root = tk.Tk()
root.geometry('800x600')

canv = tk.Canvas(root, bg="white")
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
        self.color = choice(colors)


    def draw(self):
        self.id = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r,
                                   self.y + self.r, fill=self.color, width=0)

    def update(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r,
                    self.x + self.r, self.y + self.r)
        canv.update()

    def move(self):
        global balls, quantity 
        self.x += self.vx
        self.y += self.vy
        if self.x + self.r >= 800 or self.x - self.r <= 0:
            self.vx = -self.vx
        if self.y + self.r >= 460 or self.y - self.r <= 0:
            self.vy = -self.vy
        for i in range(quantity):
            for j in range(2, quantity):
                if j == i+1:
                    if( ( ( (balls[i].x - balls[j].x)**2 + (balls[i].y == balls[j].y)**2))**0.5 <= balls[i].r + balls[j].r):
                        balls[i].vx *= -1
                        balls[i].vy *= -1
                        balls[j].vx *= -1
                        balls[j].vy *= -1
        self.update()
        root.after(1, self.move)

balls = []
quantity = rnd(2, 7)
for i in range(quantity):
    ball = Ball(name=('ball' + str(i)))
    balls.append(ball)
for ball in balls:
    ball.draw()
    ball.move()
    



tk.mainloop()