def is_valid(isbn):
    total_sum = 0
    lst = []

    for i in range(len(isbn)):
        if isbn[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'X'):
            if isbn[i] == 'X':
                lst.append(10)
            else:
                lst.append(int(isbn[i]))
        else:
            if isbn[i] != '-':
                return False
    if len(lst) != 10:
        return False
    for i in range(len(lst)):
        if lst[i] == 10:
            total_sum += 10
        else:
            total_sum += (lst[i] * (10 - i))

    if total_sum % 11 == 0:
        return True
    else:
        return False