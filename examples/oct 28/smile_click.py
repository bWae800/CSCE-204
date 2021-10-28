import turtle
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.pensize(5)
pen.speed(0)
pen.hideturtle()


def draw_smiley(x,y):
    radius = 50
    eyeradius= radius/5
    mouthradius = radius /3
    draw_circle(x,y,radius, "yellow")
    draw_circle(x - radius / 3, y, eyeradius, "blue")
    draw_circle(x + radius / 3, y, eyeradius, "blue")
    draw_mouth(x-radius/3, y - radius/3, mouthradius, "red")

def draw_mouth(x, y, radius, color):
    pen.up()
    pen.setpos(x,y)
    pen.down()
    pen.color(color)
    pen.setheading(-60)
    pen.circle(radius,120)
    pen.setheading(0)

def draw_circle(x,y, radius, color):
    pen.up()
    pen.setpos(x, y - radius)
    pen.down()
    pen.fillcolor(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

draw_smiley(0,0)

turtle.onscreenclick(draw_smiley)


turtle.done()