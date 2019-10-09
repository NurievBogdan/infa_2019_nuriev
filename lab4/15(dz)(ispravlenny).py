from graph import *





def chaika(x0,y0,a):
    penColor("white")
    penSize(3)
    moveTo(x0, y0)
    b = x0
    c = y0
    x = x0
    y = y0
    for i in range(a):
        x += 1
        y -= ((i + 1)**0.5 - i ** 0.5)*3
        lineTo(x,y)
        x0, y0 = x, y
    x0 = b
    y0 = c
    x = x0
    y = y0 
    moveTo(x0, y0)
    for i in range(a):
        x -= 1
        y -= ((i + 1)**0.5 - i ** 0.5)*3
        lineTo(x,y)
        x0, y0 = x, y      
        
def ellipse(x1,y1,x2,y2,r):
    for i in range (460):
        for j in range(650):
            module1=((x1-i)**2+(y1-j)**2)**0.5
            module2=((x2-i)**2+(y2-j)**2)**0.5
            if ((module1+module2)<r) :
                point(i,j)

def ryba(x1,y1,x2,y2,s,t):
    penColor("orange")
    penSize(1)
    brushColor("orange")
    polygon([(360-s,560-t),(340-s,535-t),(380-s,540-t),(380-s,560-t)])  
    
    penColor("darkcyan")
    penSize(1)
    brushColor("darkcyan")
    
    for i in range (460):
        for j in range(650):    
            a=((x1-s-i)**2+(y1-t-j)**2)**0.5
            b=((x2-s-i)**2+(y2-t-j)**2)**0.5 
            if ((a<80) and (b<80)):
                point(i,j)
                polygon([(325-s,565-t),(305-s,580-t),(310-s,565-t),(305-s,550-t)])
                
    penColor("blue")
    penSize(1)
    brushColor("blue")
    circle(390-s,565-t, 7)
    
    
    penColor("black")
    penSize(1)
    brushColor("black")
    circle(393-s,565-t, 3)    
    
    
    
    


brushColor("navy")
rectangle(0,650,460,280)

brushColor("red")
penColor("red")
rectangle(0,40,460,0)

brushColor("orange")
penColor("orange")
rectangle(0,80,460,40)

brushColor("yellow")
penColor("yellow")
rectangle(0,120,460,80)

brushColor("green")
penColor("green")
rectangle(0,160,460,120)

brushColor("aqua")
penColor("aqua")
rectangle(0,200,460,160)

brushColor("blue")
penColor("blue")
rectangle(0,240,460,200)

brushColor("purple")
penColor("purple")
rectangle(0,280,460,240)

chaika(100,60,50)
chaika(300,100,70)
chaika(150,160,40)
chaika(150,160,40)
chaika(200,140,50)

def lebed(x, y, s,t):

    penColor("black")
    penSize(1)
    brushColor("yellow")
    u=17
    polygon([(380*x-s,437*y-t),(410*x-s,440*y-t),(420*x-s,430*y-t),(410*x-s,430*y-t),(390*x-s,430*y-t),(380*x-s,427*y-t)])
    polygon([(380*x-s,427*y-t),(390*x-s,430*y-t),(410*x-s,430*y-t),(420*x-s,430*y-t),(413*x-s,424*y-t)])
    polygon([(295*x-s,530*y-t),(295*x-s,550*y-t),(300*x-s,535*y-t),(320*x-s,540*y-t),(305*x-s,530*y-t),(325*x-s,535*y-t),(310*x-s,525*y-t),(325*x-s,525*y-t),(317*x-s,520*y-t),(290*x-s,525*y-t)])
    polygon([((295-u)*x-s,(530+u)*y-t),((295-u)*x-s,(550+u)*y-t),((300-u)*x-s,(535+u)*y-t),((320-u)*x-s,(540+u)*y-t),((305-u)*x-s,(530+u)*y-t),((325-u)*x-s,(535+u)*y-t),((310-u)*x-s,(525+u)*y-t),((325-u)*x-s,(525+u)*y-t),((317-u)*x-s,(520+u)*y-t),((290-u)*x-s,(525+u)*y-t)])

    penColor("white")
    penSize(1)
    brushColor("white")
    
    ellipse(290*x-s,450*y-t,345*x-s,450*y-t, 65*abs(x))
    ellipse(335*x-s,435*y-t,380*x-s,435*y-t, 55*abs(x))
    ellipse(200*x-s,490*y-t,240*x-s,530*y-t, 65*abs(x))
    ellipse(220*x-s,475*y-t,260*x-s,515*y-t, 65*abs(x))
    ellipse(230*x-s,537*y-t,280*x-s,547*y-t, 53*abs(x))
    ellipse(245*x-s,520*y-t,295*x-s,530*y-t, 53*abs(x))
    
    penColor("black")
    penSize(1)
    brushColor("white")
    polygon([(150*x-s,470*y-t), (130*x-s,468*y-t), (90*x-s,460*y-t), (100*x-s, 400*y-t), (150*x-s,450*y-t)]) 
    
    polygon([(220*x-s,440*y-t), (220*x-s,400*y-t), (210*x-s,360*y-t), (205*x-s,350*y-t),(90*x-s,340*y-t),(70*x-s,330*y-t),(90*x-s,360*y-t),(140*x-s,370*y-t),(200*x-s,440*y-t) ])
    
    polygon([(160*x-s,440*y-t), (130*x-s,420*y-t), (110*x-s,400*y-t), (60*x-s, 390*y-t), (40*x-s,360*y-t),(60*x-s,370*y-t),(130*x-s,375*y-t),(180*x-s,375*y-t),(185*x-s,380*y-t),(200*x-s,475*y-t) ])
    
    
    
    penColor("white")
    penSize(1)
    brushColor("white")
    ellipse(150*x-s,460*y-t,300*x-s,460*y-t, 170*abs(x))
    
    penColor("black")
    penSize(1)
    brushColor("black")
    ellipse(365*x-s,430*y-t,375*x-s,430*y-t, 12*abs(x))    

    
    

ryba(370, 500,370,630,0,0)
ryba(370, 500,370,630,250,0)
ryba(370, 500,370,630,-30,50)

lebed(1, 1, 0, 0)
#Этого мне надо отредактировать
lebed(-0.4, 0.4, -445, -150)
lebed(0.3, 0.3, -150, -190)

run()
