'''
Assignment 1: Smart Street Lights (Fibonacci Series)
A smart city installs street lights in a newly developed area. The number of lights installed each month follows the Fibonacci pattern.
Month 1 → 0 lights
Month 2 → 1 light
Every following month, the number of lights installed is the sum of the previous two months.
As a software developer, your task is to help the city planning department generate the installation schedule.
Task
Write a recursive function to print the first N Fibonacci numbers.

Input
Enter the number of months:
7
Output
0 1 1 2 3 5 8
'''

#sum of 1st n natural number
# def sums(n):
#     if n==0:
#         return n
#     return n+sums(n-1)
# print(sums(5))

# recursive to print all element in list
# def lis(n, idx):
#     if idx==len(n):
#         return 
#     print( n[idx])
#     lis(n,idx+1)

# name = ["sahil", "singh", "patel"]
# lis(name,0)

def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)
for i in range(10):
    print(fibo(i), end=" ")