#Author Brenden Wade

toys = []

print("Welcome to our toy store")

while True:
    command = input("(V)iew, (A)dd, (R)emove, (Q)uit: ").strip().lower()

    if command == "v":
        for toy in toys:
            print(f"- {toy}")
    elif command == "a":
        toy = input("Enter toy name: ")
        toys.append(toy)
    elif command == "r":
        toy = input("Enter toy name: ")
        toys.remove(toy)
    elif command == 'q':
        break
    else:
        print("Invalid command")

print("Goodbye.")