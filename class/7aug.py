# a = [
#     [1,2,3],
#     [32,4,8],
#     [9,66,77]
# ]
# #print elements row wise
# # for i in a:
# #     print(i)
# #     # print(*i)

# #print element of matrix
# # for i in a:
# #     for j in i:
# #         print(j, end = " ")
# #     print()

# #only even elements
# for i in a:
#     for j in i:
#         if j%2==0:
#             print(j, end = " ")
#         else:
#             print("ram", end = "")
#     print()


#read row and columns from user and print the values of resultant matrix

# rows= int(input("Enter teh size of rows"))
# cols= int(input("Enter teh size of columns"))
# matrix = []
# for i in range(rows):
#     row=[]
#     for j in range(cols):
#         row.append(int(input("enter element: ")))
#     matrix.append(row)
# print("matrix elements are: ")
# for row in matrix:
#     for value in row:
#         print(value, end =" ")
#     print()

#read matrix from user and print sum of all elements
rows= int(input("Enter teh size of rows"))
cols= int(input("Enter teh size of columns"))
matrix = []
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input("enter element: ")))
    matrix.append(row)
print("matrix elements are: ")
sum =0
for row in matrix:
    for value in row:
        sum+=value
    print()
print("sum is; ", sum)

