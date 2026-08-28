'''
7.
=========================================
ONLINE EXAM RESULT SYSTEM
=========================
Store student marks in a dictionary.
results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}
Write a program to:
* Display names of students who passed.
  (Passing Marks = 50)
Sample Output:
Ajay
Neha
Ravi
'''
n = int(input("Enter number of students: "))
names = []
marks = []
for i in range(n):
    names.append(input("Enter the name: "))
    mark = int(input("Enter the marks: "))
    while mark < 0 or mark > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        # break
        mark = int(input("Enter the marks: "))
    marks.append(mark)
d = {}
for i in range(len(names)):
    d[names[i]] = marks[i]
print("STU AND MARKS IN DICT. FORMAT:", d)
print("=========Student Passed===========")
for k,v in d.items():
    if v>=50:
        name = k
        print(name)