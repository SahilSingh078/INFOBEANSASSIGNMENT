'''

3.

MATRIX PERFORMANCE EVALUATION SYSTEM

A company records the monthly performance scores of employees in a matrix format. Each row represents an employee and each column represents a month.

The HR department wants a menu-driven application to analyze employee performance.

Menu
1. Find Employee with Highest Total Score
2. Find Month with Lowest Average Score
3. Display Employee-wise Maximum Score
4. Exit
Requirements
Choice 1 – Find Employee with Highest Total Score
Calculate the sum of each row.
Display the employee number having the highest total score.
Choice 2 – Find Month with Lowest Average Score
Calculate the average of each column.
Display the month having the lowest average score.
Choice 3 – Display Employee-wise Maximum Score
Find and display the maximum value present in each row.
Sample Input
10 20 30
40 50 60
25 35 45
Output
Employee 2 has Highest Total Score = 150

Month 1 Average = 25
Month 2 Average = 35
Month 3 Average = 45

Employee 1 Max Score = 30
Employee 2 Max Score = 60
Employee 3 Max Score = 45
'''

rows = int(input("Enter number of employees: "))
cols = int(input("Enter number of months: "))
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        x = int(input("Enter score: "))
        row.append(x)
    matrix.append(row)
while True:
    print("\nMENU")
    print("1. Find Employee with Highest Total Score")
    print("2. Find Month with Lowest Average Score")
    print("3. Display Employee-wise Maximum Score")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            highest = 0
            employee = 0
            for i in range(rows):
                total = 0
                for j in range(cols):
                    total = total + matrix[i][j]
                if total > highest:
                    highest = total
                    employee = i + 1
            print("Employee", employee ," has Highest Total Score =", highest)
        case 2:
            lowest = 10**50
            month = 0
            for j in range(cols):
                total = 0           
                # apne ko jo iterate krana h
                # usko andar rkhna h jaise average column wise ke liye column ko 
                # constant rkhna h row ko krna h iterate to row ko andar rkhenge
                for i in range(rows):
                    total = total + matrix[i][j]
                average = total / rows
                if average < lowest:
                    lowest = average
                    month = j + 1
            print("Month", month,"has Lowest Average Score =", lowest)
        case 3:
            for i in range(rows):
                maximum = matrix[i][0]
                for j in range(1, cols):
                    if matrix[i][j] > maximum:
                        maximum = matrix[i][j]
                print("Employee", i + 1, "Max Score =", maximum)
        case 4:
            print("Thanks for visiting")
            break
        case _:
            print("Invalid Choice")