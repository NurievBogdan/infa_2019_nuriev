from graph import *

def ellipse(x1,y1,x2,y2,r):
    for i in range (460):
        for j in range(650):
            module1=((x1-i)**2+(y1-j)**2)**0.5
            module2=((x2-i)**2+(y2-j)**2)**0.5
            if ((module1+module2)<r) :
                point(i,j)

def lebed(x,s,t):

    penColor("black")
    penSize(1)
    brushColor("yellow")
    u=17
    polygon([(380*x-s,437*x-t),(410*x-s,440*x-t),(420*x-s,430*x-t),(410*x-s,430*x-t),(390*x-s,430*x-t),(380*x-s,427*x-t)])
    polygon([(380*x-s,427*x-t),(390*x-s,430*x-t),(410*x-s,430*x-t),(420*x-s,430*x-t),(413*x-s,424*x-t)])
    polygon([(295*x-s,530*x-t),(295*x-s,550*x-t),(300*x-s,535*x-t),(320*x-s,540*x-t),(305*x-s,530*x-t),(325*x-s,535*x-t),(310*x-s,525*x-t),(325*x-s,525*x-t),(317*x-s,520*x-t),(290*x-s,525*x-t)])
    polygon([((295-u)*x-s,(530+u)*x-t),((295-u)*x-s,(550+u)*x-t),((300-u)*x-s,(535+u)*x-t),((320-u)*x-s,(540+u)*x-t),((305-u)*x-s,(530+u)*x-t),((325-u)*x-s,(535+u)*x-t),((310-u)*x-s,(525+u)*x-t),((325-u)*x-s,(525+u)*x-t),((317-u)*x-s,(520+u)*x-t),((290-u)*x-s,(525+u)*x-t)])

    penColor("white")
    penSize(1)
    brushColor("white")
    
    ellipse(290*x-s,450*x-t,345*x-s,450*x-t, 65*x)
    ellipse(335*x-s,435*x-t,380*x-s,435*x-t, 55*x)
    ellipse(200*x-s,490*x-t,240*x-s,530*x-t, 65*x)
    ellipse(220*x-s,475*x-t,260*x-s,515*x-t, 65*x)
    ellipse(230*x-s,537*x-t,280*x-s,547*x-t, 53*x)
    ellipse(245*x-s,520*x-t,295*x-s,530*x-t, 53*x)
    
    penColor("black")
    penSize(1)
    brushColor("white")
    polygon([(150*x-s,470*x-t), (130*x-s,468*x-t), (90*x-s,460*x-t), (100*x-s, 400*x-t), (150*x-s,450*x-t)]) 
    
    polygon([(220*x-s,440*x-t), (220*x-s,400*x-t), (210*x-s,360*x-t), (205*x-s,350*x-t),(90*x-s,340*x-t),(70*x-s,330*x-t),(90*x-s,360*x-t),(140*x-s,370*x-t),(200*x-s,440*x-t) ])
    
    polygon([(160*x-s,440*x-t), (130*x-s,420*x-t), (110*x-s,400*x-t), (60*x-s, 390*x-t), (40*x-s,360*x-t),(60*x-s,370*x-t),(130*x-s,375*x-t),(180*x-s,375*x-t),(185*x-s,380*x-t),(200*x-s,475*x-t) ])
    
    
    
    penColor("white")
    penSize(1)
    brushColor("white")
    ellipse(150*x-s,460*x-t,300*x-s,460*x-t, 170*x)
    
    penColor("black")
    penSize(1)
    brushColor("black")
    ellipse(365*x-s,430*x-t,375*x-s,430*x-t, 12*x)

lebed(1,0,0)