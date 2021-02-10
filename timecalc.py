import math
print("Jwsoat Maths Calc")
print("This Calculator works out time conversion")
question = int(input("What is the number you want to convert "))
duration = str(input("What is the duration "))
time = str(input("What do you want to convert to "))
if time == "seconds" or "secs":
    seconds = question / 60
    secround = round(seconds,2)
    print(secround,time)
if time == "mins" or "minutes":
    minutes = question * 60
    minround = round(minutes,2)
    print(minround,time)
else:
    print("Acceptable answers are Seconds or Secs Mins or minutes hours days weeks months years decides and centrys")
