#sum numbers
#print result
def sum(num):
    total = 0

    for i in range(num+1):
        total += i 

    print(f"Sum 1...{num} = {total}")

#writing math game 
def prime(num):
    ans = 1
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number") 

def power(base, exp):
    ans = 1
    
    for i in range(exp):
        ans *= base 
        
    print(f"{base}^{exp} = {ans}")

def factorial(num):
    ans = 1
    for i in range(1, num+1):
        ans *= i 
    print(f"{num}! = {ans}")
print("Welcome to my math program!")

while True:
    command = input("(S)um, (P)ower, (F)actorial, P(R)ime or (Q)uit: ").strip().lower()

    if command == "q":
        break
    elif command == "s":
        number = int(input("Enter number: "))
        sum(number)
    elif command == "p":
        base = int(input("Enter base: "))
        exp =  int(input("Enter exponent: "))
        power(base,exp)
    elif command == "f":
        number = int(input("Enter number: "))
        factorial(number)
    elif command == "r":
        number = int(input("Enter number: "))
        prime(number)


    else:
        print("Invalid command")

print("Goodbye")