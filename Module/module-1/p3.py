'''
Assignment 3 — Date Difference Calculator

Create a program that accepts two dates and displays:

Enter first date: 10-09-2026
Enter second date: 25-12-2026

Display:

Difference in days
Difference in weeks
Difference in hours
Difference in minutes

Example:

Days Difference: 106
Weeks Difference: 15
Hours Difference: 2544
Minutes Difference: 152640
'''
from datetime import date,datetime
f_date = input("Enter First Date: ")
s_date = input("Enter Second Date: ")

first_date = datetime.strptime(f_date,"%d-%m-%Y").date()
second_date = datetime.strptime(s_date,"%d-%m-%Y").date()

day = (second_date - first_date).days
print("Days Difference: ", day)

week = day//7
print("No. Of Weeks: ",week)

print("Hours Difference: ", day*24)
print("Minutes Difference: ",day*24*60 )

