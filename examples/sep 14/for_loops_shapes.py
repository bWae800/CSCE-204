#Author Brenden Wade

import turtle

turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("pink")

#draw a square
shapewidth = 200
pen.up()
pen.setpos(-shapewidth/2, - shapewidth/2)
pen.down()
shape = turtle.textinput("Shape", "Enter Shape").lower().strip()

if shape == "square":
    for i in range(4):
        pen.forward(shapewidth)
        pen.left(90)

elif shape == "triangle":
    for i in range(3):
        pen.forward(shapewidth)
        pen.left(120)

else:
    print("Invalid shape")
turtle.done()