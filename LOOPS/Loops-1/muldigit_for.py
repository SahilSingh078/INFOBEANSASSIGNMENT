n = int(input("Enter Your Number : "))
x = len(str(n))
prod = 1
for i in range(x):
    b = n%10
    prod = b *prod
    n//=10

print(prod)
    