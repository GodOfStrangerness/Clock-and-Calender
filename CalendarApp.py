from datetime import *
from time import *
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
import PySimpleGUI as sg
from datetime import datetime
from time import sleep

# Funktion zur Formatierung der DateTime-Variable
def datetime_func(i):
    current_datetime_string = str(i)
    parsed_datetime = datetime.strptime(current_datetime_string, '%Y-%m-%d %H:%M:%S.%f').strftime('%a %d %b %Y, %I:%M:%S%p')
    return parsed_datetime

# Erstelle das GUI-Fenster
layout = [[sg.Text('', key='xxx')]]
window = sg.Window(title="Hello World", layout=layout, finalize=True)

kms = True

while kms:
    num = datetime_func(datetime.now())
    window['xxx'].update(num)  # Aktualisiere das Text-Element im GUI
    sleep(1)

    event, values = window.read(timeout=100)  # Verarbeitung von GUI-Ereignissen

    if event == sg.WIN_CLOSED:
        break

window.close()


'''
while True:
    global num
    kms = True
    def datetime_func(i):
        current_datetime_string = str(i)
        parsed_datetime = i.strptime(current_datetime_string, '%Y-%m-%d %H:%M:%S.%f').strftime('%a %d %b %Y, %I:%M:%S%p')
        #print(parsed_datetime)
        return parsed_datetime
    while kms == True:
        num = datetime_func(datetime.now())
        sleep(1)
        
    print (num)
    layout = [[sg.Text(num, key = 'xxx')]]
    window = sg.Window(title="Hello World",layout=layout)
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

window.close()'''


