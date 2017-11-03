def isLeapYear(year):
    """Take any int year and return True or False depending upon if year is a leap year"""
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        retun False

def daySuffix(n):
    """Take any int n and return the ordinal suffix of the int."""
    if str(n)[-1] == "1":
        return "st"
    elif str(n)[-1] == "2":
        return "nd"
    elif str(n)[-1] == "3":
        return "rd"
    else:
        return "th"

def formattedDates(day, month, year):
    """Take day, month, and year as ints and return the formatted date."""
    months = ["""January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    if day < 1:
        raise ValueError("The amount of days in a month is always at least 1.")
    
    if month < 1 or month > 12:
        raise ValueError("There are 12 months.")
    
    if month == 2:
        if isLeapYear(year) and (day > 29 or day < 1):
            raise ValueError("There are only 29 days in February during a leap year.")
        elif not isLeapYear(year) and (day > 28 or day < 1):
            raise ValueError("There are only 28 days in February when it is not a leap year.")
    elif month in [4, 6, 9, 11]:
        if day > 30:
            raise ValueError("There are only 30 days in %s." % months[month])
    else:
        if day > 31:
            raise ValueError("There are only 31 days in %s." % months[month])
        
    if type(year) is not int:
        raise TypeError("year must be int")
    
    return str(day) + daySuffix(day) + " " + months[month] + " " + str(year)
    
print(formattedDates(31, 4, 1908))
