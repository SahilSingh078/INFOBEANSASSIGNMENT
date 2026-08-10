# a =[2,3,6,8,9,4,65465,446548,446849,4894894,8446894,89]
# b=sorted(a)
# print(a)
# print(b)

# a =[2,3,6,8,9,4,65465,446548,None,False,8446894,89]
# a.reverse()
# print(a)
# a =[2,3,6,8,9,4,65465,446548,446849,4894894,8446894,89]
# b=a.copy()
# print(a)
# print(b)
# print(id(a))
# print(id(b))

# # a =[2,3,6,8,9,4,65465,446548,446849,4894894,8446894,89]
# a =[0, False, True, 1]
# print(max(a))
# a=[5,4654,484] 
# print(sum(a))
# a = ["abc", "xtx", None, int(False)]
# for i, v in enumerate(a):
#     print(i, ": ", v)

n = int(input("Enter size: "))
prime = []
for i in range(n):
    count = 0
    k = 0
    while k<=n:
        if 