a = int(input("Enter Your Usage (In Units): "))

if a <= 100:
    bill = a * 5

elif 101<=a<=200:
    bill =(100 *5)+(a - 100)*7

elif a > 200:
    bill = (100 * 5) + (100 * 7) + (a - 200) * 10

else:
    print("ERROR ---TRY AGAIN!!!!")

print("TOTAL ELECTRICITY BILL:", bill)