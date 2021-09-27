#Author Brenden Wade

import turtle
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(9)

side = []
response = turtle.textinput("Shapes", "How many shapes would you like to draw? ")

for i in range(response):
    sides = turtle.textinput("Sides", "Enter number of sides: ")
    side.append(sides)

if side == "0":
    pen.up()
    pen.setpos(-100,0)
    pen.down()
    pen.circle(150)
if side == "3":
        pen.up()
        pen.setpos(0,0)
        pen.down()
        pen.forward(90)
        pen.left(120)
        pen.forward(90)
if side == "4":
    for z in range(4):
        pen.up()
        pen.setpos(100,0)
        pen.down()
        pen.forward(90)
        pen.left(90)
if side == "5":
    for x in range(5):
        pen.up()
        pen.setpos(200,0)
        pen.down()
        pen.forward(90)
        pen.right(72)
if side == "6":
    for c in range(6):
        pen.up()
        pen.setpos(300,0)
        pen.down()
        pen.forward(90)
        pen.right(60)
if side == "8":
    pen.up()
    pen.setpos(400,0)
    pen.down()
    for v in range(8):
        pen.forward(90)
        pen.right(45)

    

    













turtle.done()