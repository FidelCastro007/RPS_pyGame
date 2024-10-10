""" import pytz
from datetime import time,datetime,timedelta

data = time(hour=12,minute=34,second=27)
print('userDefined Time:',data)

data = datetime.now()
print("Date & time:", data)
print("Year:", data.year)
print("Month:", data.month)
print("Hour:", data.hour)
print("Day:", data.day)
print("Minutes:", data.minute)
print("MicroSeconds:", data.microsecond)

#Using timeZone
#All timeZones

for i in pytz.all_timezones:
    print(i)

#localTimeZone

data = datetime.now()
print('Local Time:',data.strftime('%d/%m/%Y, %H:%M:%S,%p'))

#America / Jamaica

a1 = pytz.timezone('America/Jamaica')
b1 = datetime.now(a1)
print('America/Jamaica:',b1.strftime('%d/%m/%Y, %H:%M:%S,%p'))

#using timeDelta
data = timedelta(days=1)
yesterday_date = datetime.now() - data
TOmmorow_date = datetime.now() + data

print("Yesterday:",yesterday_date)
print("Tomorrow:",TOmmorow_date) """

from datetime import datetime
import pytz

# List of 10 different timezones
timezones = [
    'America/Jamaica',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney',
    'Africa/Cairo',
    'America/New_York',
    'Asia/Dubai',
    'Europe/Berlin',
    'America/Los_Angeles',
    'Asia/Kolkata'
]

# Loop through each timezone and print the current time
for tz in timezones:
    timezone = pytz.timezone(tz)
    current_time = datetime.now(timezone)
    print(f'{tz}: {current_time.strftime("%d/%m/%Y, %H:%M:%S, %p")}')
