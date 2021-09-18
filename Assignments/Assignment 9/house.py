#Author Brenden Wade

import turtle

turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("purple")




#draw a square
shapewidth = 170
roof = shapewidth * 1.4
star = shapewidth * .4



pen.up()
pen.setpos(-shapewidth/2, - shapewidth/2)
pen.down()

pen.begin_fill()
for i in range(4):
    pen.forward(shapewidth)
    pen.left(90)
pen.end_fill()

pen.up()
pen.setpos(-roof/2, roof/3)
pen.down()

pen.begin_fill()
for i in range(3):
    pen.color("black")
    pen.fillcolor("orange")
    pen.forward(roof)
    pen.left(120)
pen.end_fill()

pen.up()
pen.setpos(-roof, roof)
pen.down()


for i in range(5):
    pen.color("yellow")
    pen.forward(star)
    pen.left(144)


pen.up()
pen.setpos(roof, -roof)
pen.down()
pen.left(90)

pen.up()
pen.setpos(roof, -roof/2)
pen.down()

pen.begin_fill()
for i in range(5):
    pen.color("black")
    pen.fillcolor("pink")
    pen.circle(30)
    pen.left(70)
pen.end_fill()

pen.up()
pen.setpos(roof, -roof)
pen.down()

pen.left(10)
pen.forward(75)












turtle.done()

