from turtle import goto


class Question:
    
    def __init__(self, questions, answer1,answer2,answer3,answer4,canswer):
        self.questions = questions
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.canswer = canswer
    
        
        

      

    def displayquestions(self):
        import turtle
        pen = turtle.Turtle()
        pen.hideturtle()
        turtle.penup()
        goto(-400,300)
        turtle.penup()
        turtle.write(f"{self.questions}",False,"left",font=("Arial", 28, "normal"))
        turtle.penup()
        goto(-400,200)
        pen.up()
        turtle.write(f" A. {self.answer1}",False,"left",font=("Arial", 18, "normal"))
        pen.up()
        goto(-400,100)
        pen.up()
        turtle.write(f" B. {self.answer2}",False,"left",font=("Arial", 18, "normal"))
        pen.up()
        goto(-400,0)
        pen.up()
        turtle.write(f" C. {self.answer3}",False,"left",font=("Arial", 18, "normal"))
        pen.up()
        goto(-400,-100)
        pen.up()
        turtle.write(f" D. {self.answer4}",False,"left",font=("Arial", 18, "normal"))

        
                    
               
        
        



    