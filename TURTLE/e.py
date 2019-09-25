import turtle

turtle.shape('turtle')
n=5
for i in range(40):
	turtle.forward(n)
	turtle.left(90)
	turtle.forward(n+5)
	n+=5
