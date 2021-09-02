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

pen.up()
pen.setpos(-150, -250)
pen.down()

pen.color("brown")
pen.begin_fill()
pen.forward(250)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.forward(250)
pen.left(90)
pen.forward(400)
pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-150, 150)
pen.down()

pen.color("green")
pen.begin_fill()
pen.fillcolor("green")
pen.circle(130)
pen.end_fill()

pen.up()
pen.setpos(-50, 150)
pen.down()
pen.color("green")
pen.fillcolor("green")
pen.begin_fill()
pen.circle(130)
pen.end_fill()

pen.up()
pen.setpos(30, 150)
pen.down()

pen.color("green")
pen.begin_fill()
pen.fillcolor("green")
pen.circle(130)
pen.end_fill()

pen.up()
pen.setpos(30, 175)
pen.down()

pen.color("red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.up()
pen.setpos(100, 194)
pen.down()

pen.color("red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.up()
pen.setpos(-100, 256)
pen.down()

pen.color("red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.up()
pen.setpos(-175, 175)
pen.down()

pen.color("red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()

pen.up()
pen.setpos(-186, 240)
pen.down()

pen.color("red")
pen.begin_fill()
pen.circle(20)
pen.end_fill()






turtle.done()