#Author Brenden Wade

import turtle
turtle.bgcolor("skyblue")

pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)

turtle.setup(1000,1000)

pen.color("red")
pen.fillcolor("Red")
pen.setpos(0,0)
pen.begin_fill()
pen.circle(150)
pen.backward(20)
pen.end_fill()
pen.up()



pen.color("orange")
pen.fillcolor("orange")
pen.setpos(0,20)
pen.down()
pen.begin_fill()
pen.circle(130)
pen.end_fill()
pen.up()



pen.color("yellow")
pen.fillcolor("yellow")
pen.setpos(0,40)
pen.down()
pen.begin_fill()
pen.circle(110)
pen.end_fill()
pen.up()



pen.color("green")
pen.fillcolor("green")
pen.setpos(0,60)
pen.down()
pen.begin_fill()
pen.circle(90)
pen.end_fill()
pen.up()



pen.color("blue")
pen.fillcolor("blue")
pen.setpos(0,80)
pen.down()
pen.begin_fill()
pen.circle(70)
pen.end_fill()
pen.up()



pen.color("purple")
pen.fillcolor("purple")
pen.setpos(0,100)
pen.down()
pen.begin_fill()
pen.circle(50)
pen.end_fill()


turtle.done()
