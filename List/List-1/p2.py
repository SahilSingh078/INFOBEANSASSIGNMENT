'''

2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []
'''
a =int(input("Enter the number of employee: "))
nums = []
for i in range(a):
	x = int(input("Enter Salaries: "))
	nums.append(x)
print("Salaries are: ",nums)
average = (sum(nums)/len(nums))
print("Average Salary: ", average)
rem = []
for i in nums: 
	if i>average:
		print("Salary greater than average: ", i)
	if i>=15000:
		new.append(i)
print("Remaining List: ",rem)	