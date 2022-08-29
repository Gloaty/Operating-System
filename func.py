import datetime
import sys

#Global Variables
present_year = datetime.datetime.now().year

#Leap Year Checker
def leap_check():
    for i in range (0, 5):
        #check if year is leap year
        if present_year % 400 == 0:
            if  present_year % 100 != 0 and present_year % 4 == 0:
                i = True
            else:
                i = False
        else:
            i = False
    return i

#Clock
def clock_time():
    for i in range (0, 1000):
        #get current time and display it as hours:minutes:seconds
        present_time = datetime.datetime.now().strftime("%H:%M:%S")
        #am or pm?
        am_pm = datetime.datetime.now().strftime("%p")
    return present_time + " " + am_pm
def clock_date():
    for i in range (0, 10):
        #get current date and display it as YYYY-MM-DD
        present_date = datetime.datetime.now().strftime("%Y-%m-%d")
        leap_check()
        if i == True:
            pass
    return present_date