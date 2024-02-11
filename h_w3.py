import datetime as dt
from datetime import datetime as dtdt
date_input = input("Input date: ")
def get_days_from_today(date):
    try:  #виняток
        # x_str = input("\nInput date: ")
        date = dtdt.strptime(date, "%Y-%m-%d") #переводимо стрінгу  в дату
        x_now = dtdt.now()
        days_since = x_now.toordinal() - date.toordinal()
        return days_since
    except ValueError:
        print("Needs Year-Month-Day")
get_days_from_today(date_input)


import random
def get_numbers_tickets(min, max, quanity):
    try:
        rand_list = []
        
        if min >= 1 and max <=1000 and min < max and max - min > quanity:
            while len(rand_list) < quanity:
                rand_elements_un = random.randint(min, max)
                if rand_elements_un not in rand_list:
                    rand_list.append(rand_elements_un)
            rand_list.sort()
            print(rand_list)
        else:
            print("Shit, more than 1 and less than 1000 and min > max")
    except ValueError:
        print("Did you read? Repeat ")
min_input = int(input("\nEnter min: "))
max_input = int(input("Enter max: "))
quanity_input = int(input("Enter quanity: "))
get_numbers_tickets(min_input, max_input, quanity_input)


import re
raw_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    for phone_number in raw_number:
        if phone_number.isalpha() == False:
            if phone_number.strip() == True:
                print(phone_number.strip())
                return phone_number
            phone_number = re.sub(r"[(, ), \-, /, \\, a-z, A-Z]", "", phone_number)
            # print(phone_number)
            if len(phone_number) == 10:
                phone_number = re.sub(r"(\d{10})", r"+38\1", phone_number)
                # print(phone_number)
            elif len(phone_number) == 12:
                phone_number = re.sub(r"(\d{12})", r"+\1", phone_number)
                # print(phone_number)
            print(phone_number)
        else:
            print("We need phone number, try again")
    
# phone_input= input("Enter your phone pls:\n")
normalize_phone(raw_number)  

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
