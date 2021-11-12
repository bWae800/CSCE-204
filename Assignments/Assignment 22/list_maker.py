#Author Brenden Wade

from os import write


def writeToys(toys):
    with open("Assignments/Assignment 22/santas_list.txt", "w") as file:
    #Loop through friends and write them to a file
        for x in toys:
            file.write(f"{x}\n")
    

def readToys():
    toys = []
    with open("Assignments/Assignment 22/santas_list.txt") as file:
        for line in file:
            line = line.replace("\n","").strip()
            toys.append(line)
    return toys



def list_toys(toys):
    for toy in toys:
        print(f" - {toy}")


def addToys(toys):
    toy =  input("Enter toy name: ")
    toys.append(toy)
    writeToys(toys)
    print(f"{toy} was successfully added. ")
    
    return toys

def delete_toy(toys):
    toychoice = input("Enter toy name: ")

    for toy in toys:
        if toychoice.lower().strip() == toy.lower().strip():
            toys.remove(toy)
            print(f"{toychoice} was successfully removed.")
    return writeToys(toys)

toys = readToys()
while True:
    command = input("(L)ist, (A)dd, (D)elete, (Q)uit: ").strip().lower()
    if command == "l":
        writeToys(toys)
        
        list_toys(toys)
    elif command == "a":
        addToys(toys)
        
    elif command == "d":
        delete_toy(toys)
    elif command == "q":
        break
    else:
        print("Invalid command, please try again.")


print("Goodbye.")


