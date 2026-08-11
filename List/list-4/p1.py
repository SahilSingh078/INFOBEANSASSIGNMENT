'''1.
=========================================================
        MATRIX OPERATIONS MANAGEMENT SYSTEM
=========================================================


A data analysis company stores numerical information in matrix form.
To help employees perform matrix-related operations efficiently,
the company wants a menu-driven application.

The application should allow the user to:

1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

The user must enter the number of rows, columns, and all matrix
elements. The program should perform the selected operation and
display the result.

---------------------------------------------------------
Requirements
---------------------------------------------------------

1. Display the following menu repeatedly until the user chooses Exit.

   1. Add Two Matrices
   2. Subtract Two Matrices
   3. Compare Two Matrices
   4. Exit

2. Read the number of rows and columns from the user.

3. Read all elements of Matrix A and Matrix B from the user whenever
   required.

4. Based on the user's choice:

   Choice 1 - Add Two Matrices
   --------------------------------
   Add corresponding elements of both matrices and display
   the resultant matrix.

5. Choice 2 - Subtract Two Matrices
   --------------------------------
   Subtract corresponding elements of Matrix B from Matrix A
   and display the resultant matrix.

6. Choice 3 - Compare Two Matrices
   --------------------------------
   Check whether both matrices are equal.

   Two matrices are considered equal if:
   - They have the same dimensions.
   - Corresponding elements are equal.

   Display:
   "Matrices are Equal"
   or
   "Matrices are Not Equal"

7. Choice 4 - Exit
   --------------------------------
   Display:
   "Thank You for Using Matrix Operations Management System"

---------------------------------------------------------
Sample Input/Output
---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 1

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
5 6
7 8

Result Matrix:
6 8
10 12

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 3

Enter number of rows: 2
Enter number of columns: 2

Enter Matrix A:
1 2
3 4

Enter Matrix B:
1 2
3 4

Output:
Matrices are Equal

---------------------------------------------------------

Menu
1. Add Two Matrices
2. Subtract Two Matrices
3. Compare Two Matrices
4. Exit

Enter your choice: 4

Output:
Thank You for Using Matrix Operations Management System

=========================================================

'''

print("============== MATRIX OPERATIONS MANAGEMENT SYSTEM ==============")
while True:
    print("\n1. Add Two Matrices")
    print("2. Subtract Two Matrices")
    print("3. Compare Two Matrices")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    match choice:
        case 1:
            print("\n================ ADD TWO MATRICES================ ")
            r1 = int(input("Enter the no. of rows in first matrix: "))
            c1 = int(input("Enter the no. of columns in first matrix: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            r2 = int(input("\nEnter the no. of rows in second matrix: "))
            c2 = int(input("Enter the no. of columns in second matrix: "))
            B = []
            print("\nEnter Matrix B:")
            for i in range(r2):
                row = []
                for j in range(c2):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                B.append(row)
            print("\nMatrix B:")
            print(*B)
            if r1 != r2 or c1 != c2:
                print("\n====Matrix addition is not possible.====")
                print("======Both matrices must have the same dimensions=====")
            else:
                C = []
                for i in range(len(A)):
                    row = []
                    for j in range(len(A[i])):
                        row.append(A[i][j] + B[i][j])
                    C.append(row)
                print("\nResult Matrix:")
                print(*C)

        case 2:
            print("\n================  SUBTRACT TWO MATRICES ================ ")
            r1 = int(input("Enter the no. of rows in first matrix: "))
            c1 = int(input("Enter the no. of columns in first matrix: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            r2 = int(input("\nEnter the no. of rows in second matrix: "))
            c2 = int(input("Enter the no. of columns in second matrix: "))
            B = []
            print("\nEnter Matrix B:")
            for i in range(r2):
                row = []
                for j in range(c2):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                B.append(row)
            print("\nMatrix B:")
            print(*B)
            if r1 != r2 or c1 != c2:
                print("\n====Matrix subtraction is not possible.======")
                print("======Both matrices must have the same dimensions.===========")
            else:
                C = []
                for i in range(len(A)):
                    row = []
                    for j in range(len(A[i])):
                        row.append(A[i][j] - B[i][j])
                    C.append(row)
                print("\nResult Matrix:")
                print(*C)

        case 3:
            print("\n================ COMPARE TWO MATRICES ================ ")
            r1 = int(input("Enter the no. of rows in first matrix: "))
            c1 = int(input("Enter the no. of columns in first matrix: "))
            A = []
            print("\nEnter Matrix A:")
            for i in range(r1):
                row = []
                for j in range(c1):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                A.append(row)
            print("\nMatrix A:")
            print(*A)
            r2 = int(input("\n=======Enter the no. of rows in second matrix:====== "))
            c2 = int(input("=======Enter the no. of columns in second matrix:======= "))
            B = []
            print("\nEnter Matrix B:")
            for i in range(r2):
                row = []
                for j in range(c2):
                    row.append(int(input(f"Enter element [{i+1}]: ")))
                B.append(row)
            print("\nMatrix B:")
            print(*B)
            if r1 != r2 or c1 != c2:
                print("\nMatrices are Not Equal")
            else:
                equal = True
                for i in range(len(A)):
                    for j in range(len(A[i])):
                        if A[i][j] != B[i][j]:
                            equal = False
                if equal:
                    print("\nMatrices are Equal")
                else:
                    print("\nMatrices are Not Equal")
        case 4:
            print("\nThank You for Using Matrix Operations Management System")
            break
        case _:
            print("\nInvalid Choice! Please enter a choice between 1 and 4.")
