from datetime import *
import time
import PySimpleGUI as sg
#from enum import Enum, IntEnum

#class CalendarApp:

month_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

'''
def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def leapdays(y1, y2):
    """Return number of leap years in range [y1, y2).
       Assume y1 <= y2."""
    y1 -= 1
    y2 -= 1
    return (y2//4 - y1//4) - (y2//100 - y1//100) + (y2//400 - y1//400)
'''

'''
date1 = datetime.now().ctime()
print(date1)

month = datetime.now().month
print (month) 

#for i in range :

for i in range (1,len(month_list)):
    if month == month_list[i]:
        month_name = datetime.strptime(str(month), '%m').strftime('%b')
        print (month_name)

year = datetime.now().year
print (year)'''


# Get the current datetime as a string
#current_datetime_string = str(datetime.now())

# Parse the string into a datetime object
def datetime_func(i):
    while True:
        current_datetime_string = str(i)
        parsed_datetime = i.strptime(current_datetime_string, '%Y-%m-%d %H:%M:%S.%f').strftime('%a %d %b %Y, %I:%M:%S%p')
        print(parsed_datetime)
        time.sleep(1)
        return i

num = datetime_func(datetime.now())
window = sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "hi":
        num += 1
        window['xxx'].update(num)

window.close()


