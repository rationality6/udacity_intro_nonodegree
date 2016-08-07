def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return true
    return False

def daysOfMonthes(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year)
                return 29
            else:
                return 28
        else:
            return 30

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    y1, m1,
    return

daysBetweenDates(1986,11,19,2016,5,8)



###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    day +=1
    if day == 31:
        month += 1
        day = 1
    if month == 13:
        year += 1
        month = 1
    return year, month, day

print nextDay(1894,12,30)
print nextDay(2012,4,30)
print nextDay(1999,12,30)

def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    if day<30:
        return year, month, day +1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1
print nextDay(1894,12,29)
print nextDay(2012,4,30)
print nextDay(1999,12,30)
