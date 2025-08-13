def is_armstrong_number(number):
    original_number = number
    num_digits = len(str(number))
    sum = 0
    while number != 0:
        r = number % 10
        sum += r ** num_digits
        number = number//10
    if original_number == sum:
        return True
    else:
        return False
        