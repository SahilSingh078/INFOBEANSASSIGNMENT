# a=input("Enter the string: ").split()
# for i in range(len(a)):
#     w =a[i]
#     rev =""
#     for j in range(len(w)-1,-1,-1):
#         rev += w[j]
#     print(rev, end =" ")

a= input("Enter the string: ").split()
for i in a:
    print(i[::-1], end = " ")