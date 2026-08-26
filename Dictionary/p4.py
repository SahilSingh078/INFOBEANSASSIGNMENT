'''
4.
=========================================
STUDENT GRADE ANALYSIS
======================
Store student marks in a dictionary.
students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}
Write a program to:
* Find the student with highest marks.
* Find the student with lowest marks.
Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65
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
highest = 0
lowest = 101
name1 = ""
name2 = ""
for name, mark in d.items():
    if mark > highest:
        highest = mark
        name1 = name
    if mark < lowest:
        lowest = mark
        name2 = name
print("Highest Marks :", name1, highest)
print("Lowest Marks :", name2, lowest)