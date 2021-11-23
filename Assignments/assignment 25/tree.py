#Author Brenden Wade

import turtle
import random



class Tree:
    def __init__(self,x,y,height):
        self.x = x
        self.y = y
        self.height = height
        
        


    def draw(self,pen):
        colors = ["dark green","white"]
        self.x = random.randint(0,900)
        self.y = random.randint(0,900)
        pen.up()
        pen.setpos(self.x,self.y)
        pen.down()
        pen.color("black")
        pen.fillcolor(random.choice(colors))
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.height)
            pen.left(120)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x + 6 , self.y + 20)
        pen.down()
        pen.color("black")
        pen.fillcolor(random.choice(colors))
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.height * .8)
            pen.left(120)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x + 17, self.y + 45)
        pen.down()
        pen.color("black")
        pen.fillcolor(random.choice(colors))
        pen.begin_fill()
        for i in range(3):
            pen.forward(self.height * .6)
            pen.left(120)
        pen.end_fill()
        pen.up()
        pen.setpos(self.x + 25, self.y - 20)
        pen.down()
        pen.color("black")
        pen.fillcolor("brown")
        pen.begin_fill()
        for i in range(4):
            pen.forward(self.height * .4 )
            pen.left(90)
        pen.end_fill()