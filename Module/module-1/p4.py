'''
Assignment 4 – Menu-Driven Future Date Calculator

Develop a menu-driven Python program using the datetime module to calculate a future date.

The program should allow the user to add days, weeks, hours, or minutes to a given date/time.

Use timedelta for all date and time calculations.

Menu
========== FUTURE DATE CALCULATOR ==========

1. Add Days
2. Add Weeks
3. Add Hours
4. Add Minutes
5. Exit

Enter your choice:
Case 1 – Add Days

Read:

Starting date
Number of days
Input
Enter your choice: 1

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to add: 100
Output
Starting Date : 10-09-2026
Days Added    : 100
Future Date   : 19-12-2026
Case 2 – Add Weeks

Read:

Starting date
Number of weeks
Input
Enter your choice: 2

Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to add: 4
Output
Starting Date : 10-09-2026
Weeks Added   : 4
Future Date   : 08-10-2026
Case 3 – Add Hours

For this case, the student should take date and time as input.

Input
Enter your choice: 3

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to add: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours Added          : 15
Future Date & Time   : 11-09-2026 01:30

This case should test whether students understand that adding hours can change the date.

Case 4 – Add Minutes

Take date/time and number of minutes.

Input
Enter your choice: 4

Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 23:30
Enter number of minutes to add: 90
Output
Starting Date & Time : 10-09-2026 23:30
Minutes Added        : 90
Future Date & Time   : 11-09-2026 01:00
Students must correctly handle the change from 10 September → 11 September.
'''
from datetime import date,datetime,timedelta
while True:
    print('''========== FUTURE DATE CALCULATOR ==========
    
    1. Add Days
    2. Add Weeks
    3. Add Hours
    4. Add Minutes
    5. Exit''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            current = input("Enter the date [DD-MM-YYYY]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y").date()
            days_add = int(input("Enter NO. of days to add:  "))
            d = c_date + timedelta(days=days_add)
            d=d.strftime("%d-%m-%Y")
            print(d)
        case 2:
            current = input("Enter the date [DD-MM-YYYY]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y").date()
            week_add = int(input("Enter number of weeks to add: "))
            w= c_date + timedelta(weeks = week_add)
            w = w.strftime("%d-%m-%Y")
            print(w)
        case 3:
            current = input("Enter the date [DD-MM-YYYY and HH-MM]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y %H:%M")
            hour_add = int(input("Enter number of Hours to add: "))
            h = c_date + timedelta(hours = hour_add)
            h = h.strftime("%d-%m-%Y %H:%M")
            print(h)
        case 4:
            current = input("Enter the date [DD-MM-YYYY and HH-MM]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y %H:%M")
            min_add = int(input("Enter number of minutes to add: "))
            m = c_date + timedelta(minutes = min_add)
            m = m.strftime("%d-%m-%Y %H:%M")
            print(m)
        case 5:
            print("Thanks for using 🙏🙏")
            break
        case _:
            print("Please choose appropriate option")
