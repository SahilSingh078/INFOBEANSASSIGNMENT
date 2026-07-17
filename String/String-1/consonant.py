'''
4.
Consonant Counter in Student Name Record

A school management system wants to count how many consonants are present in student names.

Input: Enter student name: Ajay Singh Thakur

Output: Total consonants: 11
'''

a = input("Enter student name: ").lower()

vowels = "aeiou"
count = 0

for i in a:
    if i.isalpha() and i not in vowels:
        count += 1

print("Total Consonants =", count)