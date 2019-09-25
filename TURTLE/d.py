import turtle

turtle.shape('turtle')
turtle.speed(8)
n=int(input())
for i in range(n):
	turtle.forward(n+60)
	turtle.stamp()
	turtle.left(180)
	turtle.forward(n+60)
	turtle.left(360/n)
