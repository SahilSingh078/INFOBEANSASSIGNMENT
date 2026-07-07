'''
n = int(input("Enter a Number: "))

if n % 7 == 0 or n % 10 == 7:
    print("Buzz Number")
else:
    print("Not a Buzz Number")
'''

n = int(input("Enter a Number: "))

temp = n
while temp >= 10:
    temp = temp // 10

d = n % 10

if n % 7 == 0 or d == 7:
    print("Buzz Number")
else:
    print("Not a Buzz Number")