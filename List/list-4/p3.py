'''

3.

=========================================================
         MATRIX QUALITY CHECK SYSTEM
=========================================================

Scenario

A manufacturing company records quality inspection values in
matrix form. The Quality Control team wants a menu-driven
application to analyze the inspection data and generate reports.

The application should allow the user to:

1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user selects Exit.

   1. Count Armstrong Numbers Row-wise
   2. Count Palindrome Numbers Column-wise
   3. Display Average of Each Row
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all matrix elements from the user.

4. Based on the user's choice:

   Choice 1 - Count Armstrong Numbers Row-wise
   -------------------------------------------
   Count and display the number of Armstrong numbers
   present in each row.

   Examples:
   153, 370, 371, 407

5. Choice 2 - Count Palindrome Numbers Column-wise
   -----------------------------------------------
   Count and display the number of palindrome numbers
   present in each column.

   Examples:
   121, 131, 444, 1221

6. Choice 3 - Display Average of Each Row
   --------------------------------------
   Calculate and display the average of each row.

7. Choice 4 - Exit
   --------------------------------------
   Display:
   "Thank You for Using Matrix Quality Check System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Count Armstrong Numbers Row-wise
2. Count Palindrome Numbers Column-wise
3. Display Average of Each Row
4. Exit

Enter your choice: 1

Enter rows: 3
Enter columns: 3

Enter matrix elements:
153 121 10
370 22 44
407 15 131

Output:
Row 1 Armstrong Count = 1
Row 2 Armstrong Count = 1
Row 3 Armstrong Count = 1

---------------------------------------------------------

Enter your choice: 2

Output:
Column 1 Palindrome Count = 0
Column 2 Palindrome Count = 3
Column 3 Palindrome Count = 2

=========================================================

'''
print("====== MATRIX QUALITY CHECKING SYSTEM ======")
while True:
    print("\n1. Count Armstrong Numbers Row-wise")
    print("2. Count Palindrome Numbers Column-wise")
    print("3. Display Average of Each Row")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("\n====== Count Armstrong Numbers Row-wise ======")
            r1 = int(input("Enter the no. of rows: "))
            c1 = int(input("Enter the no. of columns: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            for i in range(r1):
                count = 0
                for j in range(c1):
                    n = A[i][j]
                    temp = n
                    total = 0
                    digits = len(str(n))
                    while temp > 0:
                        digit = temp % 10
                        total += digit ** digits
                        temp = temp // 10
                    if total == n:
                        count += 1
                print(f"Row {i+1} Armstrong Count = {count}")

        case 2:
            print("\n====== Count Palindrome Numbers Column-wise ======")
            r1 = int(input("Enter the no. of rows: "))
            c1 = int(input("Enter the no. of columns: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            for j in range(c1):
                count = 0
                for i in range(r1):
                    n = A[i][j]
                    if str(n) == str(n)[::-1]:
                        count += 1
                print(f"Column {j+1} Palindrome Count = {count}")

        case 3:
            print("\n====== Average of Each Row ======")
            r1 = int(input("Enter the no. of rows: "))
            c1 = int(input("Enter the no. of columns: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            for i in range(r1):
                total = 0
                for j in range(c1):
                    total += A[i][j]
                average = total / c1
                print(f"Row {i+1} Average = {average}")

        case 4:
            print("\nThank You for Using Matrix Quality Check System")
            break

        case _:
            print("\nInvalid Choice! Please enter a choice between 1 and 4.")