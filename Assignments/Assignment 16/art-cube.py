#Author Brenden Wade

import turtle
import random
import math

turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.hideturtle()
colors = ("maroon", "pink","purple","skyblue","lightgreen","violet")


def drawtriangle(width, angle, colors):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.fillcolor(random.choice(colors))
    
    pen.begin_fill()
    
    
    pen.forward(width)
    pen.left(135)
    pen.forward(width * math.sqrt(2))
    pen.left(135)
    pen.forward(width)
    pen.up()
    pen.end_fill()

def drawartcube(x,y,size):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    width = size
    drawtriangle(size,0,colors)
    drawtriangle(size,90,colors)
    drawtriangle(size,180,colors)
    drawtriangle(size,270,colors)


for i in range(20):
    pen.color(random.choice(colors))
    pen.fillcolor(random.choice(colors))
    x = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
    y = random.randint(-turtle.window_height()/2, turtle.window_height()/2)
    size = random.randint(20,80)
    drawartcube(x,y,size)

    






turtle.done()