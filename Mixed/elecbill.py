n = int(input("Enter Number of Houses: "))

total = 0
highest = 0

for i in range(1, n + 1):

    units = int(input("Enter Units Consumed: "))

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + (units - 100) * 7

    else:
        bill = (100 * 5) + (100 * 7) + (units - 200) * 10

    if bill > 2000:
        bill = bill + (bill * 10 / 100)

    if units < 50:
        bill = bill - 100

    print("House", i, "Bill =", bill)

    total = total + bill

    if bill > highest:
        highest = bill

print("\nTotal Collection =", total)
print("Highest Bill =", highest)