'''
1.
Multiplication Table Generator

Scenario:
A school learning app helps students practice multiplication tables.
The user enters a number n, and the system prints multiplication tables from 1 to n using nested loops.

Input:
Enter limit: 3

Output:
1 x 1 = 1	2 x 1 = 2	3 x 1 = 3
1 x 2 = 2	2 x 2 = 4	3 x 2 = 6
1 x 3 = 3	2 x 3 = 6	3 x 3 = 9
'''


a= int(input("Enter the Limit: "))
for i in range(1,a+1):
	for j in range(1,a+1):
		print(f"{i} x {j} = {i*j}")
	print()




