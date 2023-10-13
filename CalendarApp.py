from datetime import datetime, date
from enum import Enum, IntEnum

#class CalendarApp:


class Months (IntEnum):
    January = 1
    February = 2
    March = 3
    April = 4
    May = 5
    June = 6
    July = 7
    August = 8
    September = 9
    Ocober = 10
    November = 11
    December = 12

class Day(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


date1 =datetime.now().ctime()
print(date1)