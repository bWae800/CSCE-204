#Author Brenden Wade

import turtle
import random
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)

pen.color("black")

gridSize = int(turtle.numinput("Size", "Enter Size: ", 5, 1, 10))

square = turtle.window_width()/gridSize

padding = square * .1
radius = square * .4

colors = ("purple" , "gold", "white", "orange", "blue")

for row in range(gridSize):
    x = -turtle.window_width()/2 + padding + radius
    y = turtle.window_height()/2 - padding - 2 * radius - square * row 
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.circle(radius)

    if row % 2 == 0:
        pen.color("deep pink")
    else:
        pen.color("violet")
    for col in range(gridSize):
        pen.circle(radius)
        x += square
        pen.up()
        pen.setpos(x,y)
        pen.down()





turtle.done()