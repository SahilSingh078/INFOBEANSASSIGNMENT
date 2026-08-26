'''
10.
=========================================
EMAIL DOMAIN COUNTER
====================
emails = [
"[ajay@gmail.com](mailto:ajay@gmail.com)",
"[ravi@yahoo.com](mailto:ravi@yahoo.com)",
"[neha@gmail.com](mailto:neha@gmail.com)",
"[aman@outlook.com](mailto:aman@outlook.com)",
"[abc@gmail.com](mailto:abc@gmail.com)"
]
Write a program to:
* Count users belonging to each email domain.
Sample Output:
{
'gmail.com':3,
'yahoo.com':1,
'outlook.com':1
}
'''
n = int(input("enter number of emails: "))
a= []
for i in range(n):
    email = input("Enter your email: ").split("@")
    a.append(email[-1])
d={}
for x in a:
    d[x]=d.get(x,0)+1
print(d)