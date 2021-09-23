import turtle
turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(9)

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
diameter = 200
y = 0
for color in colors:
    pen.up()
    pen.setpos(0,y)
    pen.down()
    pen.color(color)
    pen.setheading(60)
    pen.circle(-diameter, 120)
    y += 15
 





turtle.done()