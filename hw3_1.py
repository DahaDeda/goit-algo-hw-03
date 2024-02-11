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