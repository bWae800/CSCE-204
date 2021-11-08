#Author Brenden Wade
import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
pen.hideturtle()


def get_scene():
    scene = []
    
    
    with open("scene.txt") as file:
        for line in file:
            scener = line.replace("\n", "").strip.lower
            scene.append(scene)

    return scene



def draw_star(x,width):
    starwidth = 90
    y= 30
    pen.up()
    pen.setpos(x,y)
    pen.down()
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

def draw_rainbow(x,width):
    colors = ("violet", "purple", "blue", "green", "yellow", "orange", "red")
    width = 200
    y = 0
    x=0
    pen.pensize(10)
    for color in colors:
        pen.up()
        pen.setpos(x,y)
        pen.down()
        pen.color(color)
        pen.setheading(60)
        pen.circle(-width, 120)
        y += 15

def draw_cloud(x,width):
    width = 60
    pen.up()
    pen.setpos(x, 0)
    pen.down()
    pen.color("blue")
    pen.fillcolor("blue")
    pen.begin_fill()
    pen.circle(width)
    pen.end_fill()
    pen.up()
    pen.setpos(x-30, 0)
    pen.down()
    pen.begin_fill()
    pen.circle(width)
    pen.end_fill()
    pen.setpos(x+30, 0)
    pen.begin_fill()
    pen.circle(width)
    pen.end_fill()


def drawuptri(x,y,size):
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    for i in range(3):
        pen.forward(90)
        pen.left(120)
    pen.end_fill()

def drawdowntri(x,y,size):
    pen.color("yellow")
    pen.fillcolor("yellow")
    pen.begin_fill()
    for i in range(3):
        pen.forward(90)
        pen.right(120)
    pen.end_fill()


get_scene()


for stuff in get_scene():
    x = turtle.xcor
    draw_cloud(20,20)
    x +30
    draw_rainbow(20,20)
    x +30
    draw_cloud(20,20)
    x +30
    draw_star(20,20)
    x +30
    draw_rainbow(20,20)
    x +30
    draw_star(20,20)
    


turtle.done()
