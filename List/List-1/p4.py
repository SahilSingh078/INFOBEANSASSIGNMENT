'''
4.
Palindrome Number List Checker
Scenario
A system checks lucky numbers which are palindromes.
Requirements
Check palindrome numbers
Store palindrome numbers in list
Count palindrome numbers
Find largest palindrome
Sort palindrome list
Test Cases
Input:
[121, 131, 20, 44, 55, 100]
Output:
Palindromes: [121, 131, 44, 55]
Count: 4
Largest: 131
Sorted: [44, 55, 121, 131]
'''
a =int(input("Enter the Size of List: "))
nums = []
for i in range(a):
	x = int(input("Enter Numbers: "))
	nums.append(x)
print("Numbers are: ",nums)
pall =[]

for i in nums:
	s = str(i)
	if s==s[::-1]:
		pall.append(i)
print("Pallindrome: ",pall)
print("Count: ",len(pall))
print("largest: ", max(pall))
print("sorted: ", sorted(pall))
