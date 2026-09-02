'''
1.
STUDENT RESULT MANAGEMENT SYSTEM
Scenario:
A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.
Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.
MENU
1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit
Functional Requirements
1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8
Thank You. Program Terminated.

Important Instructions
1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.
'''
def add_student():
    name = input("Enter Student Name : ")
    roll_number = input("Enter Roll Number : ")
    marks = []
    for i in range(1, 6):
        mark = int(input("Enter Mark " + str(i) + " : "))
        while mark < 0 or mark > 100:
            print("Invalid marks! Marks should be between 0 and 100.")
            mark = int(input("Enter Mark " + str(i) + " : "))
        marks.append(mark)
    print("\nStudent details added successfully.")
    return name, roll_number, marks
def calculate_total(marks):
    total_marks = 0
    for mark in marks:
        total_marks += mark
    return total_marks

def calculate_percentage(total_marks):
    percentage = total_marks / 5
    return percentage

# def grade(percentage):
#     # if percentage >= 90:
#     #     return "A+"
#     # elif percentage >= 80:
#     #     return "A"
#     # elif percentage >= 70:
#     #     return "B"
#     # elif percentage >= 60:
#     #     return "C"
#     # elif percentage >= 50:
#     #     return "D"
#     # else:
#     #     return "FAIL"

def highest(marks):
    return max(marks)

def lowest(marks):
    return min(marks)

def result(name, roll_number, marks):
    total_marks = calculate_total(marks)
    percentage = calculate_percentage(total_marks)
    grade_value = grade(percentage)
    highest_mark = highest(marks)
    lowest_mark = lowest(marks)

    print("\n----------- RESULT CARD -----------")
    print("\nName        :", name)
    print("Roll Number :", roll_number)
    print("\nMarks")
    for i in range(5):
        print("Subject", i + 1, ":", marks[i])

    print("\nTotal Marks :", total_marks)
    print("Percentage  :", percentage)
    print("Grade       :", grade_value)
    print("Highest Mark:", highest_mark)
    print("Lowest Mark :", lowest_mark)

name = ""
roll_number = ""
marks = []
while True:
    print("\n******** STUDENT RESULT MANAGEMENT ********")
    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Result")
    print("6. Find Highest Mark")
    print("7. Find Lowest Mark")
    print("8. Exit")
    choice = int(input("\nEnter Choice : "))
    match choice:
        case 1:
            name, roll_number, marks = add_student()
        case 2:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                total_marks = calculate_total(marks)
                print("Total Marks =", total_marks)

        case 3:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                total_marks = calculate_total(marks)
                percentage = calculate_percentage(total_marks)
                print("Percentage =", percentage)

        case 4:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                percentage=[]
                total_marks = calculate_total(marks)
                percentage.append(calculate_percentage(total_marks))
                percentage=list(percentage)
                result = map(lambda x:"A+" if x>=90 else "A" if x>=80 else "B" if x>=70 else "C" if x>=60 else "D" if x>=50 else "",percentage)
                result = list(result)
                for i in range(len(result)):
                    print(result[i])
        case 5:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                result(name, roll_number, marks)

        case 6:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                print("Highest Mark =", highest(marks))

        case 7:
            if len(marks) == 0:
                print("Please add student details first.")
            else:
                print("Lowest Mark =", lowest(marks))

        case 8:
            print("Thank You. Program Terminated.")
            break

        case _:
            print("Invalid choice.")