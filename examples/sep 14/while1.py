#Author Brenden Wade

move = input("Do you want to say hello (y or n): ").lower().strip()

while move == "y":
    print("hello")
    move = input("Do you want to say hello again? ").lower().strip()

print("Goodbye")