import turtle
import math
turtle.shape('turtle')
turtle.speed(15)
for i in range(1, 10000):
	turtle.forward(1-1/i)
	turtle.left(180/(i**0.7))
	