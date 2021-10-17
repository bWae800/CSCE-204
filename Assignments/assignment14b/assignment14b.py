#Author Brenden Wade

from datetime import date, time, datetime

monwed = {
        "ITEC 245": time(12), 
        "SPTE 240": time(2),      
            }

tuesthurs = {
        "CSCE 204": time(11,40), 
        "ITEC 245": time(1,15),
        "SPAN 109": time(4,25),
            }      


weekday = datetime.today().weekday()


if weekday == 0:
    print("Today's Schedule: ")
    for key in monwed :
        numdays = (monwed[key])
        print(f"{key} - "+ numdays.strftime('%I:%M'))
elif weekday == 1:
    print("Today's Schedule: ")
    for key in tuesthurs:
        numdays = (tuesthurs[key])
        print(f"{key} - " + numdays.strftime('%I:%M'))

else:
    print("You have no classes today.")


