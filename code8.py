
from datetime import datetime
import time
import math

today = datetime.today()
def user_birthday():
    year = int(input('When is your birthday? [YY] '))
    month = int(input('When is your birthday? [MM] '))
    day = int(input('When is your birthday? [DD] '))

    birthday = datetime(year, month, day)
    return birthday

def calculate_dates(birthyday):
    now = datetime.now()
    birthday = datetime(now.year, birthyday.month, birthyday.day)
    if birthday < today:
        birthday = birthday.replace(year=today.year + 1)
        return (birthday - now.today()).days
    else:
        return (birthday - now.today()).days + 1


bd = user_birthday()
c = calculate_dates(bd)
print(c)

hours = c*24
print(hours)

minutes = hours*60
print(minutes)



'''When is your birthday? [MM] 2
When is your birthday? [DD] 21
days-124
hours-2976
minutes-178560'''
