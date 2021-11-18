#Author Brenden Wade

from job import Job




job_list = [
    Job("Software Developer" , "Create super fun and interesting python programs", "Python, Self motivation, Text Parsing", "8 Months", "25/hr"),
    Job("Software Tester" , "Develop and run tests on python programs.", "Python, Unit testing, SQL", "2 years", "$50,000 yearly"),
    Job("IT technician" , "Fix technical issues", "Networking, Hardware", "1 Year", "$48,000 yearly"),
    Job("Website Dev" , "Develop code for websites", "Javascript, HTML, CSS, Photoshop", "6 Months", "$55,000 yearly")
]


while True:
    
    command = input("(L)ist all jobs, get a jobs (D)etails, or (Q)uit: ").strip().lower()

    if command == "q":
        
        break
    elif command == "l":
        for item in job_list:
            item.display()
    elif command == "d":
        title = input("Enter job name: ").strip().lower()
        for job in job_list:
            if job.is_match(title):
                job.display()

    else:
        print("Invalid command.")

print("Goodbye.")
         
