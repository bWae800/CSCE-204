#Author Brenden Wade

import turtle
turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.fillcolor("red")

drawingSize = turtle.numinput("U-Haul", "Size (1,5)" , 3, 1, 5)
truckSize = turtle.window_width() * drawingSize / 5
truckHeight = truckSize / 2
cabheight = truckHeight * 2/3
cabwidth = cabheight * 2/3
wheelwidth = truckSize /5


pen.up()
pen.setpos(-truckSize/2, -truckSize * 3/8)
pen.down()

pen.begin_fill()
pen.forward(truckSize)
pen.left(90)
pen.forward(cabheight)
pen.left(90)
pen.forward(cabwidth)
pen.right(90)
pen.forward(truckHeight - cabheight)
pen.left(90)
pen.forward(truckSize - cabwidth)
pen.left(90)
pen.forward(truckHeight)
pen.end_fill()

pen.up()
pen.forward(wheelwidth/2)
pen.left(90)
pen.forward(truckSize/3)
pen.fillcolor("black")
pen.begin_fill()
pen.circle(wheelwidth /2)
pen.end_fill()

pen.up()
pen.left(90)
pen.setheading(0)
pen.forward(truckSize/3)
pen.fillcolor("black")
pen.begin_fill()
pen.circle(wheelwidth /2)
pen.end_fill()





turtle.done()