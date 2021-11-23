#Author Brenden Wade

from tree import Tree
import turtle
import random

turtle.setup(1000,1000)
turtle.bgcolor("skyblue")
pen = turtle.Turtle()
pen.speed(0)
pen.pensize(2)
pen.hideturtle()

x = random.randint(0,500)
y = random.randint(0,500)
treesize = random.randint(20,100)
trees = Tree(x,y,treesize)

for i in range(20):
    trees.draw(pen)



turtle.done()