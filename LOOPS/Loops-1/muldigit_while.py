a = int(input("Enter Your Number "))
prod = 1
while a>0:
   b = a%10
   prod = prod * b
   a //= 10
print(prod)
   