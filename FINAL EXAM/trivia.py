#Author Brenden Wade
from question import Question
import turtle
import random
from turtle import Turtle, Screen, xcor, ycor
import time

screen = Screen()
turtle.bgcolor("skyblue")
turtle.setup(1000,1000)

pen = turtle.Turtle()
pen.hideturtle()

def get_questions():
    question = []
    


    with open("Assignments/FINAL EXAM/trivia.txt") as file:
        for line in file:
            data = line.split(',')
            questions = data[0].strip()
            answer1 = data[1].strip()
            answer2 = data[2].strip()
            answer3 = data[3].strip()
            answer4 = data[4].strip()
            canswer = data[5].strip()
            questione = Question(questions, answer1, answer2, answer3, answer4, canswer)
            question.append(questione)
            
            
    return question
    
def click2(x,y):
    global wclick
    wclick = True
    screen.onscreenclick(None)
    screen.clearscreen()
    screen.onscreenclick(click2,2)
        




def click(x,y):
    
    userinput = (turtle.textinput("Trivia","Enter answer letter.").lower())
    
    if userinput == "c":
        pen.up()
        turtle.goto(-300,-200)
        pen.up()
        turtle.write("Yay! You got it right!",False,"left",font=("Arial", 18, "normal"))
        pen.up()
        turtle.goto(-300,-300)
        pen.up()
        turtle.write("Right click to go to the next question.",False,"left",font=("Arial", 13, "normal"))
    

        
    else: 
        pen.up()
        turtle.goto(-300,-200)
        pen.up()
        turtle.write("Sorry! You got it wrong.",False,"left",font=("Arial", 18, "normal"))
        pen.up()
        turtle.goto(-300,-300)
        pen.up()
        turtle.write("Right click to go to the next question.",False,"left",font=("Arial", 13, "normal"))
    
    
    
wclick = False

def wait():
    global wclick
    turtle.update()
    wclick = False

    while not wclick:
        turtle.update()   
        
    

def play():
    
   
        
        turtle.write(question[0].displayquestions())
    
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[1].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[2].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[3].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[4].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[5].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[6].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[7].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[8].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[9].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        turtle.write(question[10].displayquestions())
        screen.onscreenclick(click,1,True)
        screen.onscreenclick(click2,2)
        wait()
        
        

        
    
    

    

        
        

   
    


question = get_questions()


play()






turtle.done()
































   




            
    