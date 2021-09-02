#Author Brenden Wade
print("Let's calculate your grade. ")
assignmentsGrade = float(input("Assignments: "))
exercisesgrade = float(input("Exercises: "))
midterm = float(input("Midterm Project: "))
finalproj = float(input("Final project: "))

finalgrade = assignmentsGrade * .55 + exercisesgrade * .15 + midterm * .15 + finalproj * .15

print(f"Your grade is {round(finalgrade, 1)}")