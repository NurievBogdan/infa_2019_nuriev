from graph import *
import math as m

mcoord=[]

def coordinats(event):
	mcoord.append((event.x , event.y))
	print(mcoord)

def ellipse(x, y, A, B):
	n=200
	tochki_ellipsa=[]
	for i in range(n):
		tochki_ellipsa.append((x+A*m.cos(2*m.pi*i/n), y+B*m.sin(2*m.pi*i/n)))
	polygon(tochki_ellipsa)

penColor('chartreuse')
brushColor('chartreuse')
rectangle(0 , 300 , 500, 600)

penColor('aqua')
brushColor('aqua')
rectangle(0 , 300 , 500, 0)

penColor('yellow')
brushColor('yellow')
circle(470 , 80,  100)

penColor('lightgrey')
brushColor('lightgrey')
rectangle(40, 400, 60, 200)

penColor('green')
brushColor('green')
ellipse(50, 330, 40, 30)



penColor('white')
brushColor('white')
ellipse(345, 403, 90, 40)

onMouseDown(coordinats)
run()
