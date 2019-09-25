import turtle
turtle.speed(10)
turtle.shape('turtle')
n = 40
for i in range(10):
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n)
	turtle.penup()
	turtle.forward(20)
	turtle.right(90)
	turtle.forward(20)
	turtle.pendown()
	turtle.left(180)
	n+=40
	