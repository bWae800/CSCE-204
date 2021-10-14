#Author Brenden Wade

from datetime import date, time, datetime

birthday = {
        "Classes begin": date(2021, 8, 16), 
        "Add/Drop": date(2021 ,8, 25),      
        "Labor Day Holiday": date(2022, 9, 6),  
        "Fall Break": date(2022, 12, 3),
        "Last Day to Drop": date(2021, 11, 3), 
        "Thanksgiving": date(2021, 11, 25), 
        "Last Day of Class": date(2021, 12, 3),
        "Reading Day": date(2021, 12, 4), 
        "Commencement": date(2021, 12, 13)
        
    }
            
for key in birthday :
    
    numdays = (birthday[key])
    print(f"{key} - "+ numdays.strftime('%b %d, %A'))

    
    