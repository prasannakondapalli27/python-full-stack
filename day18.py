# IMPORT, DATE CLASS, TIME CLASS, AND DATETIME CLASS
from datetime import date, time, datetime
#IMPORT - THE FOUNDATION
# Import the complete module
import math
print(math.sqrt(25))
# Import a specific item
from math import factorial
print(factorial(5))
# Import with an alias
import datetime as dt
print(dt.date.today())
#  WORKING WITH DATES - date CLASS
# Current date
today = date.today()
print(today)
# Create a specific date
birthday = date(2005, 8, 15)
print(birthday)
# Get year, month, and day
print(birthday.year)
print(birthday.month)
print(birthday.day)
# Format a date
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A, %d %B %Y"))
#  WORKING WITH TIME - time CLASS
# Create a specific time
current_time = time(10, 30, 45)
print(current_time)
# Get hour, minute, and second
print(current_time.hour)
print(current_time.minute)
print(current_time.second)
# Create time with microseconds
detailed_time = time(14, 25, 30, 500000)
print(detailed_time)
# DATE + TIME TOGETHER - datetime CLASS 
# Current date and time
now = datetime.now()
print(now)
# Create a specific date and time
meeting = datetime(2026, 9, 4, 10, 30, 0)
print(meeting)
# Get date and time separately
print(meeting.date())
print(meeting.time())
# Get individual values
print(meeting.year)
print(meeting.month)
print(meeting.day)
print(meeting.hour)
print(meeting.minute)
print(meeting.second)
# Format date and time
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print(now.strftime("%A, %d %B %Y, %I:%M %p"))