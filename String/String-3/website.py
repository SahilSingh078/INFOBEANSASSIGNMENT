'''
5. Website URL Verification System

A software company is developing an automated website registration
portal. Before saving a website address, the system must verify whether
the URL follows the required company format.

Conditions: - Must start with www - Must end with .com

Input: Enter website: www.amazon.com

Output: Valid Website
'''
# a = input("Enter Website Name: ").lower()
# for i in range (len(a)):
#     if a[:4]== "www." and a[-4:] == ".com":
#         ch = a[i]
#         if ch>="a" and ch<="z":

s = input("Enter the string: ").lower()
last = ""
if s[0] == "w" and s[1] == "w" and s[2] == "w" and s[3] == ".":
    last = s[len(s)-4:]
    if last == ".com":
        print("Valid Website")
    else:
        print("Invalid Website")
else:
    print("Invalid Website")