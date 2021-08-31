#Author Brenden Wade

import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(.5)
#grass
pen.color("medium sea green")
pen.fillcolor("medium sea green")

#bottom corner
pen.up()
pen.setpos(-turtle.window_width()/2, -turtle.window_height()/2)
pen.down()

pen.begin_fill()
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.forward(turtle.window_width())
pen.left(90)
pen.forward(turtle.window_height()/4)
pen.left(90)
pen.end_fill()

#house base
pen.up()
pen.setpos(-200, -200)
pen.down()
pen.color("black")
pen.fillcolor("maroon")
pen.begin_fill()
pen.forward(400)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-200, 200)
pen.down()
pen.begin_fill()
pen.forward(400)
pen.left(120)
pen.forward(400)
pen.left(120)
pen.forward(400)
pen.left(120)
pen.end_fill()




turtle.done()