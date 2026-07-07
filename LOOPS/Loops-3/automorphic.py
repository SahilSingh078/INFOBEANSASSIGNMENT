a = int(input("Enter Your Number: "))

temp = a
sq = a * a

while temp > 0:
    if temp % 10 != sq % 10:
        print("Not an Automorphic Number")
        break

    temp = temp // 10
    sq = sq // 10
else:
    print("Automorphic Number")