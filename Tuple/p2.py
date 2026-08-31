'''
QUESTION 2: STUDENT RESULT PROCESSING
=====================================
A training institute wants to manage student records using NamedTuple.
Fields:
roll_no, name, course, marks

Requirements:
1. Read N student records from the user and store them in a list of NamedTuples.
---
2. Display all student details.
---
3. Find and display the topper of the class.
---
4. Count and display the number of students scoring above 80 marks.
---
5. Calculate and display the average marks.
---
6. Accept a course name from the user and display all students enrolled in that course.
---
Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92
'''
from collections import namedtuple
Student = namedtuple("Student", ["roll_no", "name", "course", "marks"])
students = []
n = int(input("Enter number of students: "))
for i in range(n):
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))
    student = Student(roll_no, name, course, marks)
    students.append(student)

print("\nAll Student Details:")
for s in students:
    print(s.roll_no, s.name, s.course, s.marks)

topper = students[0]
for s in students:
    if s.marks > topper.marks:
        topper = s

print("\nTopper:")
print(topper.roll_no, topper.name, topper.course, topper.marks)

count = 0
for s in students:
    if s.marks > 80:
        count = count + 1
print("\nStudents Above 80:")
print(count)

total = 0
for s in students:
    total = total + s.marks
average = total / n
print("\nAverage Marks:")
print(average)

course_name = input("\nEnter course: ")
print("\nStudents in", course_name, "Course:")
for s in students:
    if s.course == course_name:
        print(s.roll_no, s.name, s.course, s.marks)