import turtle
import math

turtle.shape('turtle')
turtle.speed(9)

def double_round(n, R):
	for i in range(n-1):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.left(180-180*(n-2)/n)
	turtle.forward(2*R*math.sin(math.radians(180/(n))))
	for i in range(n-1):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.right(180-180*(n-2)/n)
	

x=20
n=100
turtle.left(180-90*(n-2)/n)
for i in range(10):
	double_round(n, x)
	x+=10
	n+=10