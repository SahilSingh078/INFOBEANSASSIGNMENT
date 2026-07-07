a = input("Enter course category(Programming/Design/Marketing): " ).lower()
b = input("Enter User type(Student/Working Professional/Others): ").lower()

course = input("Enter course category(Programming/Design/Marketing):  ").lower()
user = input("Enter User type(Student/Working Professional/Others): ").lower()

if course == "programming":
    fee = 5000
else:
    if course == "design":
        fee = 4000
    else:
        if course == "marketing":
            fee = 3000
        else:
            print("Invalid course")

if user == "student":
    discount = fee * 0.20
else:
    if user == "working professional":
        discount = fee * 0.10
    else:
        discount = 0

final_fee = fee - discount

print("Final Course Fee: ₹", int(final_fee))