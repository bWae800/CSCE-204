#Author Brenden Wade

print("***** Welcome to our college campus! *****")
catalogue = input("What would you like to do? View (C)atalogue, or see class (T)itle: ").lower().strip()

if catalogue == "c":
    print("""
    Our Course Catalogue: 
    -CSCE 101
    -CSCE 102
    -CSCE 145
    -CSCE 146
    -CSCE 204
    """)
elif catalogue == "t":
    clas = input("Enter Course Name: ")
    if clas == "CSCE 101":
        print("Introduction to Computer Concepts.")
    elif clas == "CSCE 102":
        print("General Applications Programming.")
    elif clas == "CSCE 145":
        print("Algorithmic Design 1.")
    elif clas == "CSCE 146":
        print("Algorithmic Design 2.")
    elif clas == "CSCE 204":
        print("Program Design and Development.")
    else:
        print("Have a nice day! ")
else:
    print("Have a nice day!")
print("Have a nice day!")
    
