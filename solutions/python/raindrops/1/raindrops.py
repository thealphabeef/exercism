def convert(number):
    endstring = ''

    if number % 3 == 0:
        endstring = endstring + 'Pling'
    if number % 5 == 0:
        endstring = endstring + 'Plang'
    if number % 7 == 0:
        endstring = endstring + 'Plong'
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    else:
        return endstring
        
