a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for i in range(a, b + 1):
    temp = i
    rev = 0

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    if rev == i:
        print(i)