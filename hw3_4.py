import datetime as dt
from datetime import datetime as dtdt

users = [
    {"name": "John Doe", "birthday": "1985.02.10"},
    {"name": "Jane Smith", "birthday": "1990.02.14"}
]

def get_upcoming_birthdays(users_birth=None):
    tdate=dtdt.today().date()
    tdate.toordinal()
    bdays=[]
    for user in users_birth:
        bdate=user["birthday"] 
        bdate=str(tdate.year)+bdate[4:]
        bdate=dtdt.strptime(bdate, "%Y.%m.%d").date()
        week_day=bdate.isoweekday()
        bdo=bdate.toordinal()
        days_between=bdo-tdate.toordinal()
        if 0<=days_between<7:
            if week_day<6: 
                bdays.append({'name':user['name'], 'birthday':bdate.isoformat().replace('-','.')[:10]}) 
            else:
                if dtdt.fromordinal(bdo+1).weekday()==0:
                    bdays.strftime("%d-%m-%Y")
                    
                elif dtdt.fromordinal(bdo+2).weekday()==0:
                    bdays.strftime("%d-%m-%Y")
                    
    return bdays

print(get_upcoming_birthdays(users))