# Random Date Around
# Get a random date around a given input

from random import *

Months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December');

def IsBissextile(Year: int) :
    return Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0

def GetIndexMonth(Month: str) :
    for i in range(12) :
        if Months[i].lower() == Month.lower() :
            Index = i
    return Index

def GetParity(Month: str, Year: int):
    Index = GetIndexMonth(Month)
    if Index == 2 :
        return 1 if IsBissextile(Year) else 0
    elif Index < 7 :
        return (Index + 1) % 2
    else :
        return Index % 2

def RandomDatesAround(Date: str, DeltaDay: int, DeltaMonth: int, DeltaYear: int) :
    Day, Month, Year = tuple(Date.split())
    Year = int(Year)
    Day = int(Day)
    Year += randint(-DeltaYear, DeltaYear)
    Index = GetIndexMonth(Month)
    Month = Months[(Index + randint(-DeltaMonth, DeltaMonth)) % 12]
    Day += randint(-DeltaDay, DeltaDay)
    Day %= 27 + GetParity(Month, Year)
    Day += 1
    return "%d %s %d" % (Day, Month.lower(), Year)

print(RandomDatesAround("28 January 1933", DeltaDay = 5, DeltaMonth = 2, DeltaYear = 5))
