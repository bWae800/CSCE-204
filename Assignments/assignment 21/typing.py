#Author Brenden Wade

import random
import string



#returns true if they win, annd false if they lose
def play_round():
    score = 0
    for i in range(10):
        
        randLetter = random.choice(string.ascii_letters)
        answer = input(f"{randLetter}: ")
        if answer == randLetter:
            score +=1
        else:
            print(f"You got {score} letters correct.")
            return score
            
            
    print("You won this round!")
    return score
       
    


    


def get_score():
    with open("CSCE-204/Assignments/assignment 21/scores.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        else:
            return (lines.pop()) #gets the first line of the file


def save_score(score):
    with open("CSCE-204/Assignments/assignment 21/scores.txt", "a") as file:
        file.write(f"game{count}: {score}\n")
            
def displayscores(scores):
    with open("CSCE-204/Assignments/assignment 21/scores.txt") as file:
        for scores in file:
            print(scores, end="")
        


#Play the game

print("Lets learn to type!")


count = 1
while True:
    
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        
        break
    if command == "p":
        score = play_round()
        save_score(score)
        count +=1 
        
        
        
displayscores(score)        

print("Goodbye.")

