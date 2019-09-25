import turtle
import math
turtle.shape('turtle')
turtle.speed(12)

def round(n):
	turtle.left(180-90*(n-2)/n)
	for i in range(n-1):
		turtle.forward(2*30*math.sin(math.radians(180/(n))))
		turtle.left(180-180*(n-2)/n)
	turtle.forward(2*30*math.sin(math.radians(180/(n))))
	turtle.right(90*(n-2)/n)

for i in range(10):
	round(100)
	turtle.left(60)	
