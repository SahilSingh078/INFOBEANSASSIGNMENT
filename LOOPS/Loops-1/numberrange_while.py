'''
13. Number Range Display System (if-elif with loops)*
A number analysis tool processes two input values and displays numbers between them based on their relationship.

* If the first number is less than the second, display numbers in ascending order
* If the first number is greater than the second, display numbers in descending order
* If both numbers are equal, display "Both numbers are same"

Write a program using *if-elif-else and loops* to implement this logic.

Input: 5, 10
Output: 5 6 7 8 9 10

Input: 10, 5
Output: 10 9 8 7 6 5

Input: 7, 7
Output: Both numbers are same

'''
a = int(input("Enter first number:"))
b = int(input("Enter second number: "))
if a<b:
	while b>=a:
		print(a,end=" ")
		a=a+1
elif a>b:
	while a>=b:
		print(a,end =" ")
		a=a-1
   