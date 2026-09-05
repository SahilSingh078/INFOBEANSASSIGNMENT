'''
1.
Employee Record Sorting (Lambda)
A company stores employee details as (Name, Salary). The HR department wants to sort the employees based on salary.
Task
Write a Python program to sort the employee records using a lambda expression.
Input
employees = [("Rahul",45000),("Amit",30000),("Neha",55000),("Priya",40000)]
Output
[('Amit', 30000), ('Priya', 40000), ('Rahul', 45000), ('Neha', 55000)]
'''
n = int(input("Enter number of users: "))
main = []
for i in range(n):
    name = input(f"Enter your name of {i+1} : ")
    salary = int(input(f"enter the salary of {i+1} : "))
    main.append((name, salary))
result = sorted(main, key = lambda x:main[1])
print(result)