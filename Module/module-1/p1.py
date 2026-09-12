'''
Assignment 1 — Age Calculator

Create a program that accepts the user's date of birth and calculates:

Current age in years
Completed months
Total number of days lived
Next birthday date
Number of days remaining for the next birthday

Input:

Enter DOB (DD-MM-YYYY): 15-08-1998

Expected Output:

Age: 28 years
Total Days Lived: XXXXX days
Next Birthday: 15-08-2027
Days Remaining: XX days
'''
from datetime import datetime,timedelta,date
current_dates = date.today()
current = input("Enter Your Dob [DD-MM-YYYY]: ")
dob = datetime.strptime(current, "%d-%m-%Y").date()
diff = (current_dates.year - dob.year)

if (current_dates.month,current_dates.day) < (dob.month,dob.day):
    diff-=1
    print("Age: ",diff)
else:
    print("Age",diff)

month = (current_dates.year - dob.year)*12 + (current_dates.month - dob.month)
if current_dates.day < dob.day:
    month -=1
    print("No. of months: ",month)
else:
    print("No. of months: ",month)

days_lived = (current_dates - dob).days +1  
print("Days Lived: ",days_lived)


if (current_dates.month, current_dates.day) < (dob.month, dob.day):
    ans = date(current_dates.year,dob.month,dob.day)
    print("Next Birthday:",datetime.strftime(ans,"%d-%m-%Y"))  
else:
    ans = date(current_dates.year+1,dob.month,dob.day)
    print("Next Birthday:",datetime.strftime(ans,"%d-%m-%Y")) 


days_remaining = (ans-current_dates).days
print("Days Remaining: ",days_remaining)