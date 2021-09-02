#Author: Brenden Wade
import math

age = float(input("Enter Age:  "))
decade = 10
futureAge = age + decade


print(f"Your future age is {futureAge}.")

#Pizza Party
print("We're having a pizza party")
numGuests = int(input("Enter Number of Guests: "))
slicesPer = float(input("Enter average slices per guest: "))
totalSlices = numGuests * slicesPer
numPizzas = math.ceil(totalSlices / 8)
print(f"You will need {numPizzas} pizzas.")

# Chickens and Eggs
numEggs = int(input("How many Eggs: "))
numCartons = numEggs // 12
extraEggs = numEggs % 12 

print(f"You need {numCartons} cartons of eggs, and have {extraEggs} eggs left over. ")

#Hourly Pay
hourlyRate = float(input("Hourly Rate: "))
hourlyRate *= 1.5
print(f"Overtime rate: {hourlyRate} ")


