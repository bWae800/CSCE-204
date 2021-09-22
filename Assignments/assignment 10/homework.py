#Author Brenden Wade

homework = [""]

wurk = ""
print("Lets configure your homework list!")
works = input("Enter Homework Item: ")
homework.append(works)


while True:
    work = input("Would you like to add another item (Y)es or (N)o: ").lower().strip()
    if work == "y":
        works = input("Enter Homework Item: ")
        homework.append(works)
    elif work == "n":
        break
    else:
        print(f"Sorry {work} was not a valid command.")
print("Heres Your Homework List: ")
print(f"{homework}")