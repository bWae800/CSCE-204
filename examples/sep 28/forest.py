import turtle
import random
turtle.setup(1000,1000)
turtle.bgcolor("white")
pen = turtle.Turtle()
pen.speed(0)
pen.width(5)
pen.color("black")

gridsize = int(turtle.numinput("Size", "Enter Size", 5, 1, 10))
square = turtle.window_width()/gridsize
paddingleft = square * .4
paddingbottom = square * .1
trunkwidth = square * .2
trunkheight = square * .4
leafradius = square * .15 

for row in range(gridsize):
    x = -turtle.window_width()/2 + paddingleft
    y = turtle.window_height()/2 - square * .9 - square * row
    pen.up()
    pen.setpos(x,y)
    pen.down()
    

    for col in range(gridsize):
        pen.up()
        pen.setpos(x,y)
        pen.down()

        pen.color("sienna")
        pen.fillcolor("sienna")

        pen.begin_fill()
        

        for i in range(4):
            if i % 2 == 0:
                pen.forward(trunkwidth)
            else:
                pen.forward(trunkheight)
            pen.forward(trunkwidth)
            pen.left(90)
        pen.end_fill()


        pen.color("forest green")
        pen.fillcolor("forest green")
        pen.up()
        pen.setpos(x+trunkwidth*.5, y + trunkheight * .9)
        pen.down()
        pen.begin_fill()
        pen.circle(leafradius)
        pen.end_fill()


        x += square




turtle.done()