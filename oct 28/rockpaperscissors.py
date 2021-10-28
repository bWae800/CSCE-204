#Author Brenden Wade

import random

def get_user_play():
    while True:
        command = input("Enter Rock Paper, or Scissors: ").lower().strip()

        if command == "rock" or command == "paper" or command == "scissors":
            return command

        print("Invalid command")
def get_comp_pick():
    choices = ("rock", "paper", "scissors")
    return random.choice(choices)
def who_wins(userpick, compPick):
    if userpick == compPick:
        print("Tie game")
    elif userpick == "rock" and compPick == "scissors":
        print( "You win")
    elif userpick == "rock" and compPick == "paper":
        print("You lose")
    elif userpick == "scissors" and compPick == "rock":
        print("You lose")
    elif userpick == "scissors" and compPick == "paper":
        print("You win")
    elif userpick == "paper" and compPick == "scissors":
        print("You lose")
    elif userpick == "paper" and compPick == "rock":
        print("You win")
userpick = get_user_play()


compPick = get_comp_pick()
print(f"Computer picked {compPick}")
who_wins(userpick,compPick)