#Author Brenden Wade
print("Let's calculate your grade. ")
assignmentsGrade = float(input("Assignments: "))
exercisesgrade = float(input("Exercises: "))
midterm = float(input("Midterm Project: "))
finalproj = float(input("Final project: "))

finalgrade = assignmentsGrade * .55 + exercisesgrade * .15 + midterm * .15 + finalproj * .15
letter = ""

if finalgrade >=90:
    letter = "A"
elif finalgrade >=80:
    letter = "B"
elif finalgrade >=70:
    letter = "C"
elif finalgrade >=60:
    letter = "D"
else:
    letter = "F"

print(f"You earned a {letter}. ")








