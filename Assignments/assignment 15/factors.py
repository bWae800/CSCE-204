#Author Brenden Wade

def displayFactors(num):
    print("The factors of",num,"are:")
    for i in range(1, num + 1):
       if num % i == 0:
           print(i)

def isFactor(firstnum,secondnum):
    i = 1
    if firstnum % secondnum ==0:
        print(f"original number: {firstnum}, potential factor: {secondnum}, it is a factor! ")
    else:
        print(f"{secondnum} is not a factor.")

while True:
    command = input("(C)heck factor, (L)ist factors, or (Q)uit: ").lower().strip()
    if command == "c":
        firstnum = int(input("Enter number: "))
        secondnum = int(input("Enter potential factor: "))
        isFactor(firstnum,secondnum)
    elif command == "l":
        number = int(input("Enter a number to list its factors: "))
        displayFactors(number)
    elif command == "q":
        break
    else:
        print("Invalid command.")

print("Goodbye.")