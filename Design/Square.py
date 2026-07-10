from turtle import*
import colorsys
speed(10)
bgcolor('black')
pensize(2)
h = 0
tracer(10)

for i in range(450):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.008
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(4):
        lt(90)
        fd(10+i/10)
    circle(30, 20)
    end_fill()

done()