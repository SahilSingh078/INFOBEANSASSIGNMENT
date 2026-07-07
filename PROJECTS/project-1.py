print("\n===== WELCOME TO SPCTM ADMISSION PORTAL =====")

student_id = 1000


while True:
    print("\n========== MAIN MENU ==========")
    print("1. New Admission")
    print("2. Exit")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:

            student_id += 1

            print("\n===== STUDENT REGISTRATION =====")

            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender (M/F): ").lower()
            score_12 = int(input("Enter 12th Percentage: "))
            category = input("Enter Category (general/obc/sc/st): ").lower()

            while True:

                print("\n===== CHOOSE COURSE =====")
                print("1. B.Tech")
                print("2. BBA")
                print("3. B.Com")
                print("4. Back")

                course = int(input("Enter Choice: "))

                if course == 4:
                    break

                fees = 0
                payable = 0

                match course:

                    case 1:
                        print("\n--- B.TECH ---")
                        stream = input("Enter Stream (science/commerce/arts): ").lower()

                        if stream != "science":
                            print("Only Science students are eligible.")
                            continue

                        if score_12 >= 75:
                            eligible = True

                        elif score_12 >= 60:
                            print("Partially Eligible.")
                            entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()

                            if entrance == "yes":
                                marks = int(input("Enter Entrance Marks (0-100): "))
                                if marks >= 50:
                                    eligible = True
                                else:
                                    eligible = False
                            else:
                                eligible = False
                        else:
                            eligible = False

                        if eligible == False:
                            print("Admission Rejected.")
                            continue

                        if score_12 >= 75:
                            if category == "general":
                                fees = 140000
                            elif category == "obc":
                                fees = 125000
                            else:
                                fees = 95000
                        else:
                            if category == "general":
                                fees = 150000
                            elif category == "obc":
                                fees = 135000
                            else:
                                fees = 110000

                    case 2:
                        print("\n--- BBA ---")
                        domain = input("Choose Domain (finance/marketing): ").lower()

                        if score_12 >= 75:
                             
                            if domain == "finance":
                                fees = 30000
                            else:
                                fees = 35000

                        elif score_12 >= 60:
                                print("Partially Eligible.")
                                entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()
                                if entrance == "yes":
                                    marks = int(input("Enter Entrance Marks: "))
                                    if marks >= 50:
                                        if domain == "finance":

                                            fees = 33000  
                                        else:
                                            fees = 38000
                                    else:
                                        print("Admission Rejected.")
                                        continue
                                else:
                                    print("Admission Rejected.")
                                    continue
                        else:
                                print("Not Eligible.")
                                continue

                    case 3:
                        print("\n--- B.COM ---")

                        if score_12 >= 75:
                            fees = 40000
                        elif score_12 >= 60:
                            print("Partially Eligible.")
                            entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()
                            if entrance == "yes":
                                marks = int(input("Enter Entrance Marks: "))
                                if marks >= 50:
                                    fees = 42000
                                else:
                                    print("Admission Rejected.")
                                    continue
                            else:
                                print("Admission Rejected.")
                                continue
                        else:
                            print("Not Eligible.")
                            continue

                    case _:
                        print("Invalid Course.")
                        continue

                if category == "obc":
                    payable = fees - (fees * 0.30)
                    scholarship = "30%"
                elif category == "sc":
                    payable = fees - (fees * 0.70)
                    scholarship = "70%"
                elif category == "st":
                    payable = fees - (fees * 0.70)
                    scholarship = "70%"
                else:
                    payable = fees
                    scholarship = "0%"

                print("\n===== SCHOLARSHIP =====")
                print("Original Fees :", fees)
                print("Scholarship :", scholarship)
                print("Payable Fees :", payable)

                hostel = input("Hostel Required? (yes/no): ").lower()
                if hostel == "yes":
                    payable += 60000

                bus = input("Bus Facility Required? (yes/no): ").lower()
                if bus == "yes":
                    payable += 18000

                mess = input("mess Plan Required? (yes/no): ").lower()
                if mess == "yes":
                    payable += 12000

                print("\nTotal Payable =", payable)

                confirm = input("Confirm Admission? (yes/no): ").lower()

                if confirm == "yes":
                    print("\n========== ADMISSION RECEIPT ==========")
                    print("Student ID :", student_id)
                    print("Name :", name)
                    print("Age :", age)
                    print("Gender :", gender.upper())
                    print("12th % :", score_12)
                    print("Category :", category.upper())

                    if course == 1:
                        print("Course : B.Tech")
                    elif course == 2:
                        print("Course : BBA")
                    else:
                        print("Course : B.Com")

                    print("Scholarship :", scholarship)
                    print("Final Fees :", payable)
                    print("Admission Status : CONFIRMED")
                    print("======================================")
                else:
                    print("Admission Cancelled.")

                break

        case 2:
            print("Thank you for visiting.")
            break

        case _:
            print("Invalid Choice.")
