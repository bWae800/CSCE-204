import turtle
turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.width(9)
pen.hideturtle()

colors = ("violet", "indigo", "blue", "green", "yellow", "orange", "red")
family = []

#gather fam members

while True:
    response = turtle.textinput("Family" , "Enter Family Members Name: ")
    if response is None:
        break
    family.append(response)

if len(family) > 0:
    for i in range(100):
        pen.color(colors[i%len(colors)-1])
        pen.up()
        pen.forward(i*4)
        pen.down()
        style = ("Arial" , int((i+4)/4), "bold")
        pen.write(family[i%len(family)],font = style)
        pen.left(360/len(family)+2)


turtle.done()