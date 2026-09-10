'''
QNO: 5
Employee Data Processing System
A company stores information about its employees in two forms:

A list of employee ages.
A string containing employee names separated by spaces.

The HR department wants a Python application that can perform different operations on this data through a menu-driven system.
To make the application modular and easy to maintain,
each operation must be implemented using a separate function that accepts data as a parameter and returns the result.
Problem Statement

Develop a menu-driven Python application called Employee Data Processing System.

The program should allow the HR department to perform the following operations:

Functions on Employee Ages (List)
1. find_second_highest_age(age_list)
Accept a list of employee ages.
Return the second highest age.
2. count_senior_employees(age_list)
Accept a list of employee ages.
Consider employees aged 50 years or above as senior employees.
Return the count of senior employees.
3. remove_duplicate_ages(age_list)
Accept a list of employee ages.
Return a new list after removing duplicate ages while maintaining the original order.

Functions on Employee Names (String)
4. count_names_starting_with_vowel(names)
Accept a string containing employee names separated by spaces.
Return the number of names that start with a vowel (A, E, I, O, U).
5. longest_name(names)
Accept a string containing employee names separated by spaces.
Return the employee name having the maximum number of characters.

Menu
========== EMPLOYEE DATA PROCESSING SYSTEM ==========
1. Find Second Highest Employee Age
2. Count Senior Employees
3. Remove Duplicate Ages
4. Count Names Starting with a Vowel
5. Find Longest Employee Name
6. Exit
====================================================
Enter your choice:
Sample Input
Employee Ages:
34 55 29 60 55 42 60 51

Employee Names:
Ajay Rahul Esha Omkar Ishita Neha
Sample Output
Second Highest Age : 55
Senior Employees : 4
Unique Ages : [34, 55, 29, 60, 42, 51]
Names Starting with Vowel : 3
Longest Employee Name : Ishita
Instructions
Implement all operations using separate functions.
Each function must accept parameters and return the result.
Do not print results inside the functions.
The menu should continue to appear until the user selects Exit.
Display an appropriate message for an invalid choice.
Use meaningful function
'''
# Functions on Employee Ages (List)
# 1. find_second_highest_age(age_list)
# Accept a list of employee ages.
# Return the second highest age.
def age(x):
    lis = sorted(set(x))
    if len(lis)<2:
        return None
    return (lis[-2])

# 2. count_senior_employees(age_list)
# Accept a list of employee ages.
# Consider employees aged 50 years or above as senior employees.
# Return the count of senior employees.
def senior(x):
    count = 0
    for i in x:
        if i>=50:
            count+=1
    return count

# 3. remove_duplicate_ages(age_list)
# Accept a list of employee ages.
# Return a new list after removing duplicate ages while maintaining the original order.

def duplicate(x):
    main = []
    for i in x:
        if i not in main:
            main.append(i)
    return main

# 4. count_names_starting_with_vowel(names)
# Accept a string containing employee names separated by spaces.
# Return the number of names that start with a vowel (A, E, I, O, U).

def vowel(name):
    a = name.split()
    count = 0
    for i in a:
        if i.lower().startswith(("a", "e", "i", "o","u")):
            count+=1
    return count

# 5. longest_name(names)
# Accept a string containing employee names separated by spaces.
# Return the employee name having the maximum number of characters.

def longest(name):
    a  = name.split()
    max = 0
    name = ""
    for i in a:
        if len(i)>max:
            max = len(i)
            name = i
    return name

n = int(input("Enter the no. of ages: "))
x = list(map(int,input("Enter your ages[using space]: ").split()))[:n]
name = input("Enter your names [with space]: ")

while True:
        print("\n========== EMPLOYEE DATA PROCESSING SYSTEM ==========")
        print("1. Find Second Highest Employee Age")
        print("2. Count Senior Employees")
        print("3. Remove Duplicate Ages")
        print("4. Count Names Starting with a Vowel")
        print("5. Find Longest Employee Name")
        print("6. Exit")
        print("====================================================")
        choice = input("Enter your choice: ")
        match case:
            case 1:
                print(f"Second Highest Age : {age(x)}")
            case 2:
                print(f"Senior Employees : {senior(x)}")
            case 3:
                print(f"Unique Ages : {duplicate(x)}")
            case 4:
                print(f"Names Starting with Vowel : {vowel(name)}")
            case 5:
                print(f"Longest Employee Name : {longest(name)}")
            case 6:
                print("Exiting system. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select an option between 1 and 6.")