def equilateral(sides):
    return True if sides[0] == sides[1] and sides[0] == sides[2] and not sides[0] == 0 else False


def isosceles(sides):
    return True if (((sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0])) and ((sides[0] == sides[1]) or (sides[0] == sides[2]) or (sides[1] == sides[2]))) else False

def scalene(sides):
    return True if ((sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0])) and (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]) else False
