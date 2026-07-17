'''
1.Vowel Counter in Customer Feedback
 A company wants to analyze customer feedback messages by counting how many vowels are present in the feedback.
Input: Enter feedback message: Hello Customer Service
Output: Total vowels: 8
'''

a =input("Enter Your String: ").lower()
s="aeiou"
count=0
for i in  a:
	if i in  s:
		count+=1
print("Total vowels = ", count)