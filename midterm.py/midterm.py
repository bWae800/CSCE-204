#Author Brenden Wade

import turtle
import random
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.hideturtle()
pen.pensize(2)

pen.up()
pen.setpos(-800,800)
pen.down()


style = ("Arial", 30)
turtle.write("Car Listings", font=style, align= "right")











carname = []
carcolors = []

num = int(turtle.numinput("Num", f"How many cars would you like to draw? "))

square = turtle.window_width()/num
padding = square * .3
radius = square * .4 
for i in range(0,num):
    colors = turtle.textinput("colors", "Enter the colors of the car: ")
    carcolors.append(colors)

    nombre = str(turtle.textinput("name", "Enter the name: "))
    carname.append(nombre)
    pen.write(nombre)   
       


for j in range(0,num):
    for c in range(4):
        pen.forward(square-padding)
        pen.left(90)
    pen.up()
    pen.forward(square)
    pen.down()

pen.up()
pen.goto(-turtle.window_width()/num,-square/2)
pen.up()

for x in range(0,num):
    for p in range(0,2):
        pen.fillcolor(carcolors[i])
        pen.begin_fill()
        pen.forward(square *1/6)
        pen.right(90)
        pen.forward(square * 1/12)
        pen.right(90)
        pen.end_fill()
    pen.forward(square)

pen.goto(-turtle.window_width()/num,-square + square/3)

for v in range(0,num):
    for l in range(0,2):
        pen.fillcolor("black")
        pen.begin_fill()
        pen.circle(square * 1/25)
        pen.end_fill()
        pen.forward(square * 1/6)
    pen.backward(square * 1/6)
    pen.backward(square * 1/6)
    pen.forward(square)

pen.goto(-turtle.window_width()/num,-square + square/2)
for w in range(0,num):
    for g in range(num):
        nombre = str(turtle.textinput("name", "Enter the name: "))
        carname.append(nombre)
        pen.write(nombre)
        pen.forward(square)






turtle.done()