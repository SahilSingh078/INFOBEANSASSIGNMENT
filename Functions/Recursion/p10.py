'''
6.
 Mobile Recharge System

A telecom company issues lucky recharge coupons only if the coupon number is prime.

Task

Write a recursive function to determine whether a given number is prime.

Input
Enter Coupon Number:
29
Output
Prime Number
'''
def prime(n, i):
    if i==n:
        return True
    if n%i== 0:
        return False
    return prime(n, i + 1)
n = int(input("Enter Coupon Number: "))
if n<=1:
    print("Not a Prime Number")
elif prime(n, 2):
    print("Prime Number")
else:
    print("Not a Prime Number")