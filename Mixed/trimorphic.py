a = int(input("Enter Your Number: "))
l = len(str(a))

cube = a ** 3
d = cube % (10 ** l)

if a == d:
    print("Trimorphic Number")
else:
    print("Not Trimorphic Number")
