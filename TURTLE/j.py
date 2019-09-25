import turtle
import math

turtle.shape('turtle')
turtle.speed(13)

def duga(n, R):
	for i in range(n):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.right(180-180*(n-1)/n)

turtle.left(90)
for i in range(10):
	n=100
	R=30
	duga(n, R)
	R=4
	duga(n, R)