import turtle
import math

turtle.shape('turtle')
turtle.speed(17)

def round(n , R):
	for i in range(n-1):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.left(180-180*(n-2.019)/n)

def duga(n , R):
	for i in range(n):
		turtle.forward(2*R*math.sin(math.radians(180/(n))))
		turtle.right(180-180*(n-1)/n)


R=201
turtle.penup()
turtle.goto(R , 0)
turtle.pendown()
turtle.left(90)
turtle.begin_fill()
round(100 , R)
turtle.color('yellow')
turtle.end_fill()

turtle.color('black')

R=20
turtle.penup()
turtle.goto(-90+R , 80)
turtle.pendown()
turtle.begin_fill()
round(100, R)
turtle.color('blue')
turtle.end_fill()
turtle.penup()
turtle.goto(90+R , 80)
turtle.pendown()
turtle.color('black')
turtle.begin_fill()
round(100, R)
turtle.color('blue')
turtle.end_fill()

turtle.penup()
turtle.goto(0 , 20)
turtle.right(180)
turtle.width(7)
turtle.color('black')
turtle.pendown()
turtle.forward(40)

R=60
turtle.penup()
turtle.goto(120 , -50)
turtle.color('red')
turtle.pendown()
duga(100 , R)