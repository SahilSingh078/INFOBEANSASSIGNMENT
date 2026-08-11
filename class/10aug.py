# find maximum in matrix
# rows= int(input("Enter teh size of rows: "))
# cols= int(input("Enter teh size of columns: "))
# matrix = []
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input("enter element: ")))
#     matrix.append(row)
# max = matrix[0][0]
# for i in matrix:
#     for v in i:
#         if v>max:
#             max = v
# print("max element: ", max)

#sum of main diagonal
# rows= int(input("Enter teh size of rows: "))
# cols= int(input("Enter teh size of columns: "))
# matrix = []
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input("enter element: ")))
#     matrix.append(row)
# sum = 0
# for i in range(len(matrix)):
#     sum+= matrix[i][i]
# print("sum is: ", sum)
    

#multiply two matrices
print("\n================ Multiply Two Matrices ================ ")
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
if c1!=r2:
    print("Multiplication not possible ")
else:
    result = []
    for i in range(r1):
        row=[]
        for j in range(c1):
            row.append(0)
        result.append(row)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] = result[i][j] +(A[i][k]*B[k][j])
    print("result is:\n ", result)
    for row in result: 
        print(*row)