#Author Brenden Wade
import random
print("Fortune Teller")

while True:
    question = input("Enter question: ")
    num = random.randint(1,3)

    if num == 1:
        print("Yes")
    elif num == 2:
        print("No")
    elif num == 3:
        print("Maybe")

    playagain = input("Do you want to play again? (Y)es or (N)o: ").strip().lower()

    if playagain != "y":
        break

print("Goodbye")