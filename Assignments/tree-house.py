#Author Brenden Wade

print(f"Lets make a tree house!")

width = float(input("What is the width of the tree house? "))
Length = float(input("What is the length of the tree house? "))
height = float(input("What is the height of the tree house? "))
Height2 = float(input("What is the height of the ladder? "))

flooring = width * Length * 1.75
wall = (Length * height *2 + width * height*2) * .8
roof = Length * width * 1.2
ladder = Height2 * 4

price = flooring + wall + roof + ladder

(print(f"The price of your treehouse is {price}"))