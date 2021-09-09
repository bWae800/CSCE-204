#Author Brenden Wade

temp = int(input("Enter the Temperature. "))
prec = input("Enter precipitation. ").lower().strip()

if temp <=32 and prec == "s":
    print("You should wear a snowsuit")
elif temp <= 70 and prec == "r":
    print("You should wear a rain jacket! ")
elif temp <=80 and prec == "r":
    print("You should wear a swimsuit! ")
else:
    print("Pick your own outfit. ")