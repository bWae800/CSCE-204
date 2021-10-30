#Author Brenden Wade

import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
turtle.setup(1000,1000)

pen.pensize(5)
pen.speed(0)
pen.hideturtle()


def sun(x,y):
    
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.fillcolor("yellow")
    pen.begin_fill()
    pen.circle(90)
    pen.end_fill()



def clouds(x,y):
    pen.up()
    pen.setpos(x, y)
    pen.down()
    pen.color("blue")
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(40)
    pen.end_fill()
    pen.up()
    pen.setpos(x-30, y)
    pen.down()
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    pen.setpos(x+30, y)
    pen.begin_fill()
    pen.circle(30)
    pen.end_fill()
    
def trees(x,y):
    pen.up()
    pen.setpos(x+20, y+20)
    pen.down()
    pen.color("green")
    pen.fillcolor("green")
    pen.begin_fill()
    for i in range(3):
        pen.forward(50)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x+10, y-20)
    pen.down()
    pen.begin_fill()
    for v in range(3):
        pen.forward(70)
        pen.left(120)
    pen.end_fill()
    pen.up()
    pen.setpos(x, y-60)
    pen.down()
    pen.begin_fill()
    for b in range(3):
        pen.forward(90)
        pen.left(120)
    pen.end_fill()
    pen.color("brown")
    pen.fillcolor("brown")
    pen.begin_fill()
    pen.up()
    pen.setpos(x+30, y-80)
    pen.down()
    for n in range(4):
        pen.forward(30)
        pen.left(90)
    pen.end_fill()

turtle.onscreenclick(trees)








turtle.done()