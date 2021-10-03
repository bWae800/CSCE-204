import turtle
import random
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)


colors = []

var = 1
line = int(turtle.numinput("Num", "Enter Number of stars: ",5, 1, 10))

for x in range(0,line):
    color = turtle.textinput("title", f"Enter color of row {var}")
    colors.append(color)
    var += 1

square = turtle.window_width()/line

padding = square * .1
radius = square * .4

colors = []

x = -turtle.window_width()/2 
y = turtle.window_height()/2 
pen.setpos(x,y)
for i in range (line):
    pen.color(color)
    pen.up()
    pen.down()
    



    for col in range(5):
        pen.forward(100)
        pen.left(144)

    pen.up()
    pen.setpos(pen.xcor()+square,pen.ycor()-square)
        

       




turtle.done()









turtle.done()