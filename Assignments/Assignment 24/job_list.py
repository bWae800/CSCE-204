#Author Brenden Wade

from job import Job
import re




def get_jobs():
    job_list = []

    with open("Assignments/Assignment 23/jobs.txt") as file:
        for line in file:
            data = line.split(',')
            title = data[0].strip()
            description = data[1].strip()
            skills = data[2].strip().split("*")
            
            length = data[3].strip()
            pay = data[4].strip()
            job = Job(title, description,skills,length,pay)
            job_list.append(job)
    
    return job_list


def get_bool(data):
    if data.lower() == "true":
        return True
    else:
        return False

job_list = get_jobs()
while True:
    
    command = input("(L)ist all jobs, get a jobs (D)etails, or (Q)uit: ").strip().lower()

    if command == "q":
        
        break
    elif command == "l":
        for item in job_list:
            item.display()
    elif command == "d":
        title = input("Enter job name: ")
        for job in job_list:
            if job.is_match(title):
                job.display()

    else:
        print("Invalid command.")

print("Goodbye.")
         
