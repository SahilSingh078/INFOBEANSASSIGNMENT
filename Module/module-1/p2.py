'''
2.
 Employee Joining & Experience System

Create an employee experience calculator.

Read:
Employee name
Joining date
Current date

Calculate:

Total days worked
Total years worked
Total months approximately
Experience in Years Months Days
Whether employee has completed 1 year
Whether employee has completed 5 years

Example:

Enter employee name: Rahul
Enter joining date: 10-06-2021
Enter current date: 10-09-2026

Output:
Employee: Rahul
Joining Date: 10-06-2021
Experience: 5 Years 3 Months 0 Days
Total Days Worked: 1918
5 Years Completed: Yes
'''
from datetime import date,datetime
name = input("Enter your name: ")
joining_date = input("Joing date [dd-m-yyyy]: ")
current_date = input("current date [dd-m-yyyy]: ")

j_date = datetime.strptime(joining_date, "%d-%m-%Y").date()
c_date = datetime.strptime(current_date, "%d-%m-%Y").date()

total_worked = (c_date - j_date)
print("Total days worked: ",total_worked.days)

total_year = (c_date.year - j_date.year)
print("Total years worked: ", total_year)

total_month = (c_date.month - j_date.month)
print("Total month worked: ",(total_year)*12  + total_month)

experience= (c_date.day - j_date.day)
print("Experience: ", total_year, "Years", total_month,"Months", experience , "Days")

if total_year >=1:
    print("1 Year Completed  ")
else:
    print("Not Completed")


if total_year>=5:
    print("5 year Completed")
else:
    print("Not Completed 5year")

