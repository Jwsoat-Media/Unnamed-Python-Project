import math
math1 = int(input("First Number? "))
math2 = int(input("Second Number? "))
mathsymbol = int(input("1= Plus 2= Minus 3= times 4=divide 5 = More options "))

if mathsymbol == 1:
    plusans= math1 + math2
    print (plusans)
if mathsymbol == 2:
    minusans = math1 - math2
    print("Answer is:", minusans)
if mathsymbol == 3:
    timesans = math1 * math2
    print(timesans)
if mathsymbol == 4:
    divideans = math1 / math2
    print(divideans)
if mathsymbol == 5:
    moremath = int(input("1 = Half it 2 = Double it 3 = square root of 4 = to the power of  "))

    if moremath ==1:
        half = int(input("Pick first or second number or 3 for both "))
        if half == 1:
            half1 = math1 / 2
            print(half1)

        if half == 2:
            half2 = math2 / 2
            print(half2)

        if half == 3:
            half1 = math1 / 2
            half2 = math2 / 2
            print(half1)
            print(half2)


    if moremath == 2:
        double = int(input("Pick first or second number or 3 for both "))
        if double == 1:
            double1 = math1 * 2
            print(double1)
        if double == 2:
            double2 = math2 * 2
            print(double2)
        if double == 3:
            double1 = math1 * 2
            double2 = math2 * 2
            print(double1)
            print(double2)

    if moremath == 4:
        powerof = int(input("Pick first or second number or 3 for both "))
        if powerof == 1:
            powerof1 = math1 * math1
            print(powerof1)
        if powerof == 2:
            powerof2 = math2 * math2
            print(powerof2)
        if powerof == 3:
            powerof1 = math1 * math1
            powerof2 = math2 * math2
            print(powerof1)
            print(powerof2)








print("©2021 Jwsoat Media")