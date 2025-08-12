def leap_year(year):
    return True if (year % 4 == 0 and not year % 100 == 0) or (year % 100 == 0 and year % 400 == 0) else False

