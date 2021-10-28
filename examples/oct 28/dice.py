import random

def roll():
    num = random.randint(1,6)
    print(f"{num} was rolled")
    return num

while True:
    #User rolling
    print("You are rolling the dice....")
    UserRoll = roll() + roll()
    print(f"You rolled a {UserRoll}")

    print("Computer is rolling the dice....")
    computerRoll = roll() +roll()

    if UserRoll > computerRoll:
        print("YOu get to play first")
        break
    elif computerRoll > UserRoll:
        print("Computer goes first")
        break
