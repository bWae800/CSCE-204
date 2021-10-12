#Author Brenden Wade

from datetime import date, time, datetime

todaysDate = date.today()

print(todaysDate)
print(todaysDate.strftime("%A, %B %d, Year - %Y"))

halloween = date(2021, 10 ,31)
meetingtime = time(14,30)
appointment = datetime(2022, 3, 14, 13, 59)

birthdaytest = input("Enter birthday (MM/DD/YYYY):  ").strip()
birthday = datetime.strptime(birthdaytest, "%m/%d/%Y")

print("Your birthday is " + birthday.strftime("%B %d %Y"))