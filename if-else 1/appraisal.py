a = int(input("Enter Salary: "))
b = int(input("Enter Rating (1-5): "))

if b == 5:
    hike = a * 0.25
elif b == 4:
    hike = a * 0.20
elif b == 3:
    hike = a * 0.10
elif b == 2:
    hike = a * 0.05
else:
    hike = 0

if a < 20000 and b >= 4:
    hike += 2000

final_salary = a + hike 

print("Revised Salary: ₹", int(final_salary))