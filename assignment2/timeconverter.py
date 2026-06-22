a=int(input(" Enter The Duration Of The Event: "))

hr = a//3600

remsec = a % 3600

min= remsec // 60

sec = remsec % 60

print("Hours: " ,int(hr), "Minutes: ", int(min), "Seconds: ", int(sec))