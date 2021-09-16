#Author Brenden Wade

sum = 0
for 1 in range (1,10):
    sum = 1
    print(sum)


#Loop 1 to 10, and present the sum.

sum = 0
for 1 in range (1,10):
    sum = 1
    print(sum)

#ask the user for a number, if it is <1
#give them an error
#then loop through and calculate the sum 1 ... usernum
userNum = int(input("Enter a number: "))

if userNum < 1:
    print("Sorry, your number must be greater than 1")
else:
    sum = 0

    for i in range (1, userNum + 1):
        sum +=i

    print(sum)
