#i am definately just going to bruteforce this lol, also im manually editing the data, i cannot be bothered to parse this shit
import math

def game1():
    possibilities = 0
    m = int(0)
    totalTime = 54817088
    y = 0
    x = 54817088
    while m <= 54817088:
        y = m * (x - m)

        #print (m)
        #print (y)
        m = m + 1
        if y > 446129210351007:
            possibilities = possibilities + 1
    return possibilities


answer = game1()
print(answer)
