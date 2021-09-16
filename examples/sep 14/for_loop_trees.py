#Author Brenden Wade

import turtle

turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("brown")

treeHeight = 300
toptriangle = treeHeight * .2
middletriangle = treeHeight *.3
bottomtriangle = treeHeight *.5
trunk = treeHeight + .1

#set intial position

pen.up()
pen.setpos(-trunk/2, -treeHeight/2)
pen.down()

#draw trunk
pen.begin_fill()
for i in range(4):
    pen.forward(trunk)
    pen.left(90)
pen.end_fill()

#set pos for bottom triangle
pen.up()
pen.setpos(-bottomtriangle/2, -treeHeight/2 + trunk)
pen.down()
pen.fillcolor("forest green")
pen.color("forest green")

#draw bottom triangle
pen.begin_fill()
for i in range(3):
    pen.forward(bottomtriangle)
    pen.left(120)
pen.end_fill()








turtle.done()
