'''
ASSIGNMENT 6 – EMPLOYEE WORKING DATE & DEADLINE CALCULATOR
You are developing a small HR/Project Management utility.
The HR department wants to calculate important dates related to an employee or project.
Create a menu-driven program that provides the following operations:
========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit

Enter your choice:
CASE 1 – Calculate Probation End Date
An employee joins an organization on a particular date.
The company has a probation period of a specified number of months/days.
For this assignment, take probation period in days.
Input

Enter your choice: 1
Enter employee joining date (DD-MM-YYYY): 15-07-2026
Enter probation period in days: 90
Output
Joining Date       : 15-07-2026
Probation Period   : 90 days
Probation End Date : 13-10-2026

Students should use:
timedelta(days=...)

CASE 2 – Calculate Project Deadline
A software company starts a project on a particular date.
The project manager gives a deadline in terms of number of days.
Calculate the final deadline.

Input
Enter your choice: 2
Enter project start date (DD-MM-YYYY): 10-09-2026
Enter project duration in days: 120
Output
Project Start Date : 10-09-2026
Project Duration   : 120 days
Project Deadline   : 08-01-2027

Important
The program must correctly handle:
Month changes
Year changes
Leap years

Students should not manually calculate these.

CASE 3 – Calculate Notice Period End Date
An employee resigns from a company.
The employee's notice period is given in days.
Calculate the date on which the notice period ends.

Input
Enter your choice: 3
Enter resignation date (DD-MM-YYYY): 20-09-2026
Enter notice period in days: 60
Output
Resignation Date : 20-09-2026
Notice Period    : 60 days
Last Working Date: 19-11-2026
Additional Test

Students should test:

Resignation Date : 15-12-2026
Notice Period    : 60 days

The program must correctly move into 2027.
CASE 4 – Calculate Days Remaining for Deadline
A project has a deadline.
The program should take:
Current date
Project deadline
and calculate how many days are remaining.
Input
Enter your choice: 4
Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 25-09-2026
Output
Current Date     : 10-09-2026
Project Deadline : 25-09-2026
Days Remaining   : 15 days
If deadline has already passed

Input:

Enter current date (DD-MM-YYYY): 10-09-2026
Enter project deadline (DD-MM-YYYY): 01-09-2026

Output:

Current Date     : 10-09-2026
Project Deadline : 01-09-2026
Deadline Status  : Deadline has already passed
Days Overdue     : 9 days
CASE 5 – Check Employee Work Anniversary

The HR department wants to check whether an employee's work anniversary is today.

Take:

Employee joining date
Current date
Input
Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 10-09-2020
Enter current date (DD-MM-YYYY): 10-09-2026
Output
Joining Date : 10-09-2020
Current Date : 10-09-2026

Work Anniversary: YES
Completed Years  : 6 years
If anniversary is not today

Input:

Enter your choice: 5

Enter employee joining date (DD-MM-YYYY): 15-05-2022
Enter current date (DD-MM-YYYY): 10-09-2026

Output:

Joining Date : 15-05-2022
Current Date : 10-09-2026

Work Anniversary: NO
Completed Years  : 4 years
CASE 6 – Exit
Enter your choice: 6
Thank you for using Employee & Project Date Calculator!
'''


from datetime import date,timedelta,datetime
while True:
    print('''========== EMPLOYEE & PROJECT DATE CALCULATOR ==========

1. Calculate Probation End Date
2. Calculate Project Deadline
3. Calculate Notice Period End Date
4. Calculate Days Remaining for Deadline
5. Check Employee Work Anniversary
6. Exit''')
    choice = int(input("Enter your choice: "))
    match choice:

        case 1:
            joining_date = input("Enter Joining Date [DD-MM-YYYY]: ")
            probation = int(input("Enter probabtion Period [In days]: "))
            j_date = datetime.strptime(joining_date,"%d-%m-%Y").date()
            j = j_date + timedelta(days=probation)
            j = j.strftime("%d-%m-%Y")
            print("Joining Date       : ",joining_date)
            print("Probation Period   : ",probation)
            print("Probation End Date : ",j)

        case 2:
            start_date = input("Enter Project Start Date [DD-MM-YYYY]: ")
            duration = int(input("Enter duration in days "))
            s_date = datetime.strptime(start_date,"%d-%m-%Y").date()
            s = s_date + timedelta(days= duration)
            s = s.strftime("%d-%m-%Y")
            print("Project Start Date :",start_date)
            print("Project Duration   :",duration)
            print("Project Deadline   :",s)

        case 3:
            resign_date = input("Enter Resignation Date [DD-MM-YYYY]: ")
            notice = int(input("Enter notice period in days:  "))
            r_date = datetime.strptime(resign_date,"%d-%m-%Y").date()
            r = r_date + timedelta(days = notice)
            r = r.strftime("%d-%m-%Y")
            print("Resignation Date :",resign_date)
            print("Notice Period    :",notice)
            print("Last Working Date:",r)

        case 4:
            current_date = input("Enter Current date [DD-MM-YYYY]: ")
            p_deadline = input("Enter Project Deadline Date [DD-MM-YYYY]: ")
            c_date = datetime.strptime(current_date, "%d-%m-%Y").date()
            p_date = datetime.strptime(p_deadline, "%d-%m-%Y").date()
            diff = (p_date - c_date).days
            print("Current Date     :", current_date)
            print("Project Deadline :", p_deadline)
            if diff >= 0:
                print("Days Remaining   :", diff, "days")
            else:
                print("Deadline Status  : Deadline has already passed")
                print("Days Overdue     :", abs(diff), "days")

        case 5:
            joining_date = input("Enter Employee Joining Date [DD-MM-YYYY]: ")
            current_date = input("Enter Current Date [DD-MM-YYYY]: ")
            j_date = datetime.strptime(joining_date, "%d-%m-%Y").date()
            c_date = datetime.strptime(current_date, "%d-%m-%Y").date()
            print("Joining Date :", joining_date)
            print("Current Date :", current_date)

            if j_date.day == c_date.day and j_date.month == c_date.month:
                print("Work Anniversary: YES")
            else:
                print("Work Anniversary: NO")

            completed_years = (c_date.year - j_date.year)
            print("Completed Years  :", completed_years, "years")
        case 6:
            print("Thank you for using Employee & Project Date Calculator!")
            break
        case _:
            print("Invalid choice! Please enter a number between 1 and 6.")
            