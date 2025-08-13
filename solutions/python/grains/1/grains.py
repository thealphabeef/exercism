def square(number):
    if (64 >= number >= 1):
        if number == 1:
            number_wheat = 1
        else:
            number_wheat = 2 ** (number - 1)
        return number_wheat
    else:
        raise ValueError('square must be between 1 and 64')
    
def total():
    number_total = 0
    for i in range(64):
        number_add = (2 ** i)
        number_total += number_add
    return number_total
        