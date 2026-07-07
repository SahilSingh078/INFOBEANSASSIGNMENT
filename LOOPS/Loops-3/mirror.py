a = int(input("Enter Your Transaction Number: "))

temp = a
rev = 0

while a > 0:
    digit = a % 10
    rev = rev * 10 + digit
    a = a // 10

print("Reverse =", rev)

diff = abs(temp - rev)
print("Difference =", diff)

count = 0
temp2 = diff

if temp2 == 0:
    count = 1
else:
    while temp2 > 0:
        count += 1
        temp2 = temp2 // 10

print("Digits =", count)


if diff == 0:
    print("Perfect Match")
elif diff % 9 == 0:
    print("Verified")
else:
    print("Rejected")