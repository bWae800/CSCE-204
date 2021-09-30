#Author brenden Wade

num = int(input("Enter a number: "))

for row in range(1, num+1):
    for col in range(1, num+1):
        if row * col <= 9:
            print(f"{row*col}", end=" ")
        else:
            print(f"{row*col}", end=" ")
    print()     #goto next line



