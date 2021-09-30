#Author

import turtle
import random
turtle.setup(1000,1000)
turtle.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.width(9)
pen.hideturtle()

colors = ("purple" , "gold", "white", "orange", "blue")

for i in range(100):
    x = random.randint(-turtle.window_width()/2, turtle.window_width()/2)
    y = random.randint(-turtle.window_height()/2, turtle.window_height()/2)

    pen.up()
    pen.setpos(x,y)
    pen.down()

    pen.color(random.choice(colors))
    pen.fillcolor(random.choice(colors))
    
    starwidth = random.randint(20,100)

    pen.begin_fill()
    for i in range(3):
        pen.forward(starwidth)
        pen.left(120)
    pen.end_fill()

    pen.up()
    pen.setpos(x,y + starwidth * .5)
    pen.down()

    pen.begin_fill()
    for i in range(3):
        pen.forward(starwidth)
        pen.left(-120)
    pen.end_fill()

   # for b in range(6):
   #     pen.forward(100)
   #     pen.left(144)
#pen.end_fill()

    



turtle.done()