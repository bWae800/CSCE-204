import random
def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number = number //10


    return sum
#returns true if they win, annd false if they lose
def play_round():
    randnum = random.randint(1000,9999)
    answer = sum_digits(randnum)

    useranswer = int(input(f"Sum of digits in {randnum}: "))

    if answer == useranswer:
        print("Yay! you got it right!")
        return True
    else:
        print(f"Sorry, the correct answer is {answer}. ")
        return False

    
play_round()

def load_score():
    with open("examples/nov 9/score.txt") as file:
        lines = file.readlines()
        if not lines:
            return 0
        else:
            return int(lines.pop()) #gets the first line of the file


def save_score(score):
    with open("examples/nov 9/score.txt", "w") as file:
        file.write(f"{score}")

#Play the game

print("Welcome to our Addition Game!")
score = load_score()
while True:
    command = input("(P)lay or (Q)uit: ").strip().lower()

    if command == "q":
        break
    if play_round():
        score += 1
print(f"Your score is {score}. ")
print("Goodbye.")

save_score(score)