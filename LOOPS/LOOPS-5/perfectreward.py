'''
3 Perfect Number Reward System
A gaming company rewards users if entered number is a Perfect Number.
(Perfect Number = sum of proper factors equals number)
Write a program using for-else loop to:
- Find sum of proper factors
- If sum equals number print Reward Unlocked
- Else print Try Again
Input:
6
Output:
Reward Unlocked
'''

a = int(input("Enter a number: "))

sum = 0

for i in range(1, a):
    if  a % i == 0:
        sum += i
else:
    if sum == a:
        print("Reward Unlocked")
    else:
        print("Try Again")