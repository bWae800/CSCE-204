#Author: Brenden Wade
import turtle
turtle.bgcolor("skyblue")

#setup pen
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(.5)

#draw square
pen.color("maroon")
pen.fillcolor("black")
pen.begin_fill()
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.left(90)
pen.forward(200)
pen.end_fill()


#draw a triangle
pen.up()
pen.setpos(350,350)
pen.down()
pen.setheading(0)

pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)
pen.forward(100)
pen.right(120)

turtle.done()