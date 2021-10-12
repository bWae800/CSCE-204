#Author Brenden Wade

from datetime import date, time, datetime

birthdays = [date(2021,11,1), date(2022, 9,1), date(2022, 3, 27),
                date(2021, 12 , 3), date(2022, 6, 15), date(2022, 5, 6)]

#display birthday
for birthday in birthdays:
    daysTill = (birthday - date.today()).days

    print(f"{birthday.strftime('%B %d')} - {daysTill} days away! ")