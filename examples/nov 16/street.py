from house import House
import turtle
turtle.setup(1000,1000)
pen = turtle.Turtle
pen.pensize(2)
pen.speed(0)
pen.hideturtle()




myhouse = House("211 Harden Street", 50 , 100 , 50, "medium aquamarine", "hot pink",True) 
myhouse.draw(pen)









turtle.done()