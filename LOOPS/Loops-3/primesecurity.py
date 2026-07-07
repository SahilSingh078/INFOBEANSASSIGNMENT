a = int(input("Enter Your Number: "))

count = 0

for i in range(1, a + 1):
    if a % i == 0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")