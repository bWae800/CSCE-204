
 
 
 
 
 
def get_courses():
    courses = {}
    
    
    with open("Assignments/Assignment19/courses.txt") as file:
        for line in file:
            data = line.split(":")
            number = data[0].strip().lower()
            clas = data[1].strip()
            courses[number] = clas

            

    return courses


def get_description(courses):
    x = input("Enter Course Code: ")
    if x in courses:
        print(f"{x}")
    else:
        print(f"Sorry, {x} is not in the Course Catalog.")


        
def display_courses(courses):
    for x in courses:
        print(f"{x}: {courses[x]}")


while True:
    courseslist = get_courses()

    command = input("What would you like to do? (V)iew, (L)ookup or (Q)uit:  ").lower().strip()
    if command == "v":
        display_courses(courseslist)
    elif command == "l":
        get_description(courseslist)
    elif command == "q":
        break
    else: 
        print("Invalid command")

