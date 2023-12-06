import math

def game1():
    possibilities = 0
    m = int(0)
    totalTime = 54
    y = 0
    x = 54
    while m <= 54:
        y = m * (x - m)
        #print (m)
        #print (y)
        m = m + 1
        if y > 446:
            possibilities = possibilities + 1
    return possibilities

def game2():
    possibilities = 0
    m = int(0)
    totalTime = 81
    y = 0
    x = 81
    while m <= 81:
        y = m * (x - m)
        #print (m)
        #print (y)
        m = m + 1
        if y > 1292:
            possibilities = possibilities + 1
    return possibilities


def game3():
    possibilities = 0
    m = int(0)
    totalTime = 70
    y = 0
    x = 70
    while m <= 70:
        y = m * (x - m)
        #print (m)
        #print (y)
        m = m + 1
        if y > 1035:
            possibilities = possibilities + 1
    return possibilities

def game4():
    possibilities = 0
    m = int(0)
    totalTime = 88
    y = 0
    x = 88
    while m <= 88:
        y = m * (x - m)
        #print (m)
        #print (y)
        m = m + 1
        if y > 1007:
            possibilities = possibilities + 1
    return possibilities
    




answer = game1()*game2()*game3()*game4()
print(answer)
