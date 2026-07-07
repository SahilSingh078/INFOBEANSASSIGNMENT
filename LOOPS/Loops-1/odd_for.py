a = int(input("Enter Your Number: "))
count = 0

for i in str(a):
    if int(i) % 2 != 0:
        count += 1

print( "odd digits", count
)