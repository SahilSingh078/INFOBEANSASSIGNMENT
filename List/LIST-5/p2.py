'''

2.
Secure Password Analysis

A cybersecurity team wants to identify pairs of passwords having no common characters.

Problem Statement:

Given N strings, count the number of pairs that do not share any common character.

Example:

Input

N = 4
passwords[] = {"a, "fg", "adbc", "de""}

Output

3

Explanation

("abc","de")
("abc","fg")
("de","fg")

'''
n = int(input("Enter the size of array: "))
passwords = []
for i in range(n):
    x = input("Enter password: ")
    passwords.append(x)
count = 0
for i in range(n):
    for j in range(i + 1, n):
        common = False
        for char in passwords[i]:
            if char in passwords[j]:
                common = True
                break
        if common == False:
            print("Pair:", passwords[i], passwords[j])
            count += 1
print("Number of pairs:", count)