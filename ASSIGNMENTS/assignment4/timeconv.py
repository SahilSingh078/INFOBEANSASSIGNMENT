a=int(input("Enter Total seconds : "))
hrs = a//3600
b = a%3600
min = b // 60
second = b%60
print(f"HOURS=  {hrs} Minutes= {min} Seconds= {second}")