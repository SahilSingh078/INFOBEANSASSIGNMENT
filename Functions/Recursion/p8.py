'''
4.
Assignment 10: Cyber Security (Strong Password Check)

A cybersecurity company considers a numeric password to be "strong" if every digit is even.

Task

Write a recursive function to check whether all digits of the given number are even.

Input 1
Enter Password:
248620
Output 1
Strong Password
Input 2
Enter Password:
248621
Output 2
Weak Password
'''

def pas(n):
    if n == 0:
        return "Strong Password"
    if n%2!= 0:
        return "Weak Password"
    return pas(n // 10)
n = int(input("Enter your number: "))
print(pas(n))
