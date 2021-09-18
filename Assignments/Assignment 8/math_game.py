#Author Brenden Wade

import random

print("Welcome to our simple math game!")

rand1 = random.randint(10,99)
rand2 = random.randint(10,99)
rand3 = random.randint(10,99)
rand4 = random.randint(10,99)


answer = rand1 + rand2
answer3 = rand3 + rand4

while True:
    answer1 = int(input(f"{rand1} + {rand2} = "))
    if answer1 == answer:
         b = input("""
Correct!
Would you like to play again? (Y)es or (N)o: """).lower().strip()
    else:
        print(f"Sorry, the correct answer was {answer}.") 
    if b == "n":
        break
    if b == "y":
        answer2 = int(input(f"{rand3} + {rand4} = "))
    else:
            print(f"Sorry the answer was {answer3}.")
    if answer2 == answer3:
         b = input("""
Correct!
Would you like to play again? (Y)es or (N)o: """).lower().strip()
    if b == "n":
        break
print("Goodbye")
        




    
                

    






