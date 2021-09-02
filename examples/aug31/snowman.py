#Author Brenden Wade
import turtle
turtle.setup(1500,1500)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("white")

drawingSize = turtle.numinput("Snowman", "Size (1,5)" , 3, 1, 5)
snowmanSize = turtle.window_width() * drawingSize / 5

lgCircle = drawingSize /3
medCircle = lgCircle * 3/4
smCircle = medCircle * 3/4

pen.up()
pen.setpos(0, -snowmanSize/2)
pen.down()

pen.begin_fill
pen.circle(lgCircle/2)
pen.end_fill()


turtle.done()