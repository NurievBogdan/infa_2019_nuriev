import turtle
import math

turtle.shape('turtle')
turtle.speed(8)

def zvezda(n):
	for i in range(n):
		turtle.forward(150)
		turtle.left(540-3*(180*(n-2)/n))

n=int(input())
turtle.left(180)
zvezda(n)
turtle.done()