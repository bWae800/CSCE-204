#Author Brenden Wade

import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(10)
pen.color("black")
pen.fillcolor("pink")

shape = turtle.textinput("Shapes", "Enter shape: ").lower().strip()
shapesize = turtle.window_width()/4

if shape == "circle":
    pen.setpos(0,-shapesize/2)
    pen.begin_fill()
    pen.circle(shapesize/2)
    pen.end_fill()
elif shape == "square":
    pen.setpos(-shapesize/2,-shapesize/2)
    pen.begin_fill()
    pen.forward(shapesize)
    pen.left(90)
    pen.forward(shapesize)
    pen.left(90)
    pen.forward(shapesize)
    pen.left(90)
    pen.forward(shapesize)
    pen.end_fill()
elif shape == "triangle":
    pen.setpos(-shapesize/2,-shapesize/2)
    pen.begin_fill()
    pen.forward(shapesize)
    pen.left(120)
    pen.forward(shapesize)
    pen.left(120)
    pen.forward(shapesize)
    pen.end_fill()

    




turtle.done()