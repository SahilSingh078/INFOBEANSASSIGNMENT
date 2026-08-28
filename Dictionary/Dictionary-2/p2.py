'''
2.
ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM
A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.
Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.
The system should store student records in a nested dictionary where:
Key → Student ID
Value → Dictionary containing student information
Each student record should contain:
Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program
Display the following menu repeatedly until the user chooses Exit.
=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================
1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student
Accept the following details:
Student ID
Student Name
Course Name
Mobile Number
Fees
City
Store the information in the nested dictionary.
Validation
If Student ID already exists:
Student ID Already Exists
2. Search Student
Accept Student ID from the user.
If found, display complete student information.
Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore
If not found:
Student Not Found
3. Update Course
Accept Student ID.
If found:
Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Studen
Accept Student ID.
If found:
Delete the record.
Sample Output
Student Deleted Successfully
Otherwise:
Student Not Found
5. Display All Students
Display all student records in a proper format.
Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------
Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students
Display total number of students enrolled.
Sample Output
Total Students : 45
7. Display Students By Course
Accept a course name from the user.
Display all students enrolled in that course.
Sample Output
Enter Course : Python
101  Ajay
105  Neha
112  Aman
If no students are found:
No Students Found
8. Display Students By City
Accept city name from the user.
Display all students belonging to that city.
Sample Output
Enter City : Indore
101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees
Display complete details of the student who has paid the highest fees.
Sample Output
Highest Fee Paying Student
Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees
Display complete details of the student who has paid the lowest fees.
Sample Output
Lowest Fee Paying Student
Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit
Terminate the application.
Sample Output
Thank You For Using Student Management System
'''

students = {}
while True:
    print()
    print("1. ADD NEW STUDENT")
    print("2. SEARCH STUDENT")
    print("3. UPDATE COURSE")
    print("4. DELETE STUDENT")
    print("5. DISPLAY ALL STUDENTS")
    print("6. COUNT TOTAL STUDENTS")
    print("7. DISPLAY STUDENTS BY COURSE")
    print("8. DISPLAY STUDENTS BY CITY")
    print("9. FIND STUDENT PAYING HIGHEST FEES")
    print("10. FIND STUDENT PAYING LOWEST FEES")
    print("11. EXIT")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("\n1. ADD NEW STUDENT")
            a = int(input("Enter number of students: "))
            for i in range(a):
                student_id = int(input("Enter Student ID: "))
                while student_id in students:
                    print("Student ID Already Exists")
                    student_id = int(input("Enter Student ID again: "))
                name = input("Enter Student Name: ")
                course = input("Enter Course Name: ")
                mobile = input("Enter Mobile Number: ")
                fees = int(input("Enter Fees: "))
                city = input("Enter City: ")
                students[student_id] = {"Name": name, "Course": course,"Mobile": mobile,"Fees": fees,"City": city}
                print("Student Added Successfully")
        case 2:
            print("\n2. SEARCH STUDENT")
            if len(students)==0:
                print("Please Add Student First")
            else:
                student_id = int(input("Enter Student ID to search: "))
                found = False
                for k, v in students.items():
                    if student_id == k:
                        print("Student ID :", k)
                        print("Name       :", v["Name"])
                        print("Course     :", v["Course"])
                        print("Mobile     :", v["Mobile"])
                        print("Fees       :", v["Fees"])
                        print("City       :", v["City"])
                        found = True
                if found == False:
                    print("Student Not Found")
        case 3:
            print("\n3. UPDATE COURSE")
            if len(students)==0:
                print("Please Add Student First")
            else:
                student_id = int(input("Enter Student ID: "))
                while student_id not in students:
                    print("Student Not Found")
                    student_id = int(input("Enter Student ID again: "))
                print("Student's current course:", students[student_id]["Course"])
                course_new = input("Enter New Course: ")
                students[student_id].update({"Course": course_new})
                print("Course Updated Successfully")
        case 4:
            print("\n4. DELETE STUDENT")
            if len(students)==0:
                print("Please Add Student First")
            else:
                student_id = int(input("Enter Student ID: "))
                while student_id not in students:
                    print("Student Not Found")
                    student_id = int(input("Enter Student ID again: "))
                del students[student_id]
                print("Student Deleted Successfully")
        case 5:
            print("\n5. DISPLAY ALL STUDENTS")
            if len(students) == 0:
                print("No Student Records Available")
            else:
                for k, v in students.items():
                    print("-----------------------------------")
                    print("Student ID :", k)
                    print("Name       :", v["Name"])
                    print("Course     :", v["Course"])
                    print("Mobile     :", v["Mobile"])
                    print("Fees       :", v["Fees"])
                    print("City       :", v["City"])
                    print("-----------------------------------")
        case 6:
            print("\n6. COUNT TOTAL STUDENTS")
            print("Total Students :", len(students))
        case 7:
            print("\n7. Display Student By Course ")
            if len(students)==0:
                print("Please Add Student First")
            else:
                course_name = input("Enter Course name: ")
                for k, v in students.items():
                    if v["Course"].lower() == course_name.lower():
                        print(k, "  ", v["Name"])
        case 8:
            print("\n8. DISPLAY STUDENTS BY CITY")
            if len(students)==0:
                print("Please Add Student First")
            else:
                city_name = input("Enter city name: ")
                for k, v in students.items():
                    if v["City"].lower() == city_name.lower():
                        print(k, "  ", v["Name"])
        case 9:
            print("\n9.FIND STUDENT PAYING HIGHEST FEES")
            if len(students)==0:
                print("Please Add Student First")
            else:
                old = 0
                for k,v in students.items():
                    if v["Fees"]> old:
                        old = v["Fees"]
                        oldest = k
                print("--------------------------------")
                print("Student ID :", oldest)
                print("Name       :", students[oldest]["Name"])
                print("Course     :", students[oldest]["Course"])
                print("Fees       :", students[oldest]["Fees"])
                print("--------------------------------")   
        case 10:
            print("\10. Find Student Paying Lowest Fees")
            if len(students)==0:
                print("Please Add Student First")
            else:
                lowest = float("inf")
                for k,v in students.items():
                    if v["Fees"]<lowest:
                        young = v["Fees"]
                        lowest = k
                print("--------------------------------")
                print("Patient ID :", lowest)
                print("Name       :", students[lowest]["Name"])
                print("Age        :", students[lowest]["Course"])
                print("Gender     :", students[lowest]["Fees"])
                print("--------------------------------")      
        case 11:
            print("\nThank You For Using Student Management System")   
            break
        case _:
            print("Please Choose Appropriate Option!!!!!!!!!")