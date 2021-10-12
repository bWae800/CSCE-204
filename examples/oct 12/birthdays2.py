#Author Brenden Wade

from datetime import date, time, datetime

birthdays = {
    "Amy": date(2022, 11, 1),
    "Bobby": date(2022 ,9, 1),
    "Carl": date(2022, 3, 27),
    "Dave": date(2022, 12, 3),
    "Erin": date(2022, 6, 15),
    "Frank": date(2022, 5, 6)
                }
for key in birthdays :
    numdays = (birthdays[key] - date.today()).days
    print(f"{key} - {birthdays[key]}- in {numdays} days")
