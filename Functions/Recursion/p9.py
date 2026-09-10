'''
5.
 Hospital Record System (Search Digit)
A hospital stores patient IDs as numbers. The administrator wants to verify whether a specific digit exists in a patient ID.
Task
Write a recursive function to determine whether a given digit is present.

Input
Enter Patient ID:
5837264
Enter Digit:
7
Output
Digit Found
'''
def digi(n, d):
    if n==0:
        return "Digit Not Found"
    if n%10==d:
        return "Digit Found"
    return digi(n//10, d)
n = int(input("Enter Patient ID: "))
d = int(input("Enter Digit: "))
print(digi(n, d))