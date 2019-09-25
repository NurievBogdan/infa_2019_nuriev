import turtle
import math

turtle.shape('turtle')
turtle.speed(5)
def pravmnogougol(n, R):
	turtle.left(180-90*(n-2)/n)
	for i in range(n-1):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.left(180-180*(n-2)/n)
	turtle.forward(2*R*math.sin(math.radians(180/(n))))
	turtle.right(90*(n-2)/n)

x=10
n=3
for i in range(10):
	pravmnogougol(n, x)
	turtle.penup()
	turtle.forward(x)
	turtle.pendown()
	x=2*x
	n+=1

