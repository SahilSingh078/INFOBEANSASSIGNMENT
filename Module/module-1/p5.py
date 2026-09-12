'''
ASSIGNMENT 5 – MENU-DRIVEN PAST DATE & TIME CALCULATOR
Create a menu-driven Python program that allows the user to calculate a date/time in the past by subtracting days, weeks, hours, or minutes.
Menu
========== PAST DATE & TIME CALCULATOR ==========
1. subtract Days
2. subtract Weeks
3. subtract Hours
4. subtract Minutes
5. Exit

Enter your choice:
CASE 1 – subtract Days
Input
Enter your choice: 1
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of days to subtract: 100
Output
Starting Date : 10-09-2026
Days subtracted : 100
Past Date : 02-06-2026
CASE 2 – subtract Weeks
Input
Enter your choice: 2
Enter starting date (DD-MM-YYYY): 10-09-2026
Enter number of weeks to subtract: 6
Output
Starting Date : 10-09-2026
Weeks subtracted : 6
Past Date : 30-07-2026
CASE 3 – subtract Hours
Here the student must read both date and time.
Input
Enter your choice: 3
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 10:30
Enter number of hours to subtract: 15
Output
Starting Date & Time : 10-09-2026 10:30
Hours subtracted     : 15
Past Date & Time     : 09-09-2026 19:30
CASE 4 – subtract Minutes
Input
Enter your choice: 4
Enter date and time (DD-MM-YYYY HH:MM): 10-09-2026 01:00
Enter number of minutes to subtract: 90
Output
Starting Date & Time : 10-09-2026 01:00
Minutes subtracted   : 90
Past Date & Time     : 09-09-2026 23:30
CASE 5 – Exit
Enter your choice: 5
Thank you for using Past Date & Time Calculator!
'''

from datetime import date,datetime,timedelta
while True:
    print('''========== PAST DATE & TIME CALCULATOR ==========
    
    1. subtract Days
    2. subtract Weeks
    3. subtract Hours
    4. subtract Minutes
    5. Exit''')
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            current = input("Enter the date [DD-MM-YYYY]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y").date()
            days_subtract = int(input("Enter NO. of days to subtract:  "))
            d = c_date - timedelta(days=days_subtract)
            d=d.strftime("%d-%m-%Y")
            print(d)
        case 2:
            current = input("Enter the date [DD-MM-YYYY]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y").date()
            week_subtract = int(input("Enter number of weeks to subtract: "))
            w= c_date - timedelta(weeks = week_subtract)
            w = w.strftime("%d-%m-%Y")
            print(w)
        case 3:
            current = input("Enter the date [DD-MM-YYYY and HH-MM]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y %H:%M")
            hour_subtract = int(input("Enter number of Hours to subtract: "))
            h = c_date - timedelta(hours = hour_subtract)
            h = h.strftime("%d-%m-%Y %H:%M")
            print(h)
        case 4:
            current = input("Enter the date [DD-MM-YYYY and HH-MM]: ")
            c_date = datetime.strptime(current, "%d-%m-%Y %H:%M")
            min_subtract = int(input("Enter number of minutes to subtract: "))
            m = c_date - timedelta(minutes = min_subtract)
            m = m.strftime("%d-%m-%Y %H:%M")
            print(m)
        case 5:
            print("Thanks for using 🙏🙏")
            break
        case _:
            print("Please choose appropriate option")
