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
            while True:
                gender = input("Enter Gender (Male/Female): ").lower()
                if gender == "male" or gender == "female":
                    break
                else:
                    print("Invalid gender. Please enter Male or Female.")
            score_12 = int(input("Enter 12th Percentage: "))
            while True:
                category = input("Enter Category (general/obc/sc/st): ").lower()
                if category == "general" or category == "obc" or category == "sc" or category == "st":
                    break
                else:
                    print("Invalid category. Please enter general, obc, sc, or st.")
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
                        while True:
                            stream = input("Enter Stream (science/commerce/arts): ").lower()
                            if stream == "science" or stream == "commerce" or stream == "arts":
                                break
                            else:
                                print("Invalid stream. Please enter science, commerce, or arts.")
                        if stream != "science":
                            print("Only Science students are eligible.")
                            continue
                        if score_12 >= 75:
                            eligible = True
                        elif score_12 >= 60:
                            print("Partially Eligible.")
                            while True:
                                entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()
                                if entrance == "yes" or entrance == "no":
                                    break
                                else:
                                    print("Invalid input. Please enter yes or no.")
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
                        while True:
                            domain = input("Choose Domain (finance/marketing): ").lower()
                            if domain == "finance" or domain == "marketing":
                                break
                            else:
                                print("Invalid domain. Please enter finance or marketing.")
                        if score_12 >= 75:
                            if domain == "finance":
                                fees = 30000
                            else:
                                fees = 35000
                        elif score_12 >= 60:
                                print("Partially Eligible.")
                                while True:
                                    entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()
                                    if entrance == "yes" or entrance == "no":
                                        break
                                    else:
                                        print("Invalid input. Please enter yes or no.")
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
                            while True:
                                entrance = input("Have you appeared for Entrance Test? (yes/no): ").lower()
                                if entrance == "yes" or entrance == "no":
                                    break
                                else:
                                    print("Invalid input. Please enter yes or no.")
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
                while True:
                    hostel = input("Hostel Required? (yes/no)-> Rs. 60000:   ").lower()
                    if hostel == "yes" or hostel == "no":
                        break
                    else:
                        print("Invalid input. Please enter yes or no.")
                if hostel == "yes":
                    payable += 60000
                while True:
                    bus = input("Bus Facility Required? (yes/no)-> Rs. 18000:   ").lower()
                    if bus == "yes" or bus == "no":
                        break
                    else:
                        print("Invalid input. Please enter yes or no.")
                if bus == "yes":
                    payable += 18000
                while True:
                    mess = input("mess Plan Required? (yes/no)-> Rs. 12000:   ").lower()
                    if mess == "yes" or mess == "no":
                        break
                    else:
                        print("Invalid input. Please enter yes or no.")
                if mess == "yes":
                    payable += 12000
                print("\nTotal Payable =", payable)
                while True:
                    confirm = input("Confirm Admission? (yes/no): ").lower()
                    if confirm == "yes" or confirm == "no":
                        break
                    else:
                        print("Invalid input. Please enter yes or no.")
                if confirm == "yes":
                    print("\n===== PAYMENT SECTION =====")
                    print("1. Cash")
                    print("2. UPI")
                    print("3. Card")
                    method = int(input("Choose Payment Method: "))
                    match method:
                        case 1:
                            print("You selected Cash Payment.")
                            payment = int(input("Enter Cash Amount: Rs "))

                            if payment == payable:
                                print("Payment Successful.")
                            elif payment > payable:
                                print("Payment Successful.")
                                print("Return Change: Rs", payment - payable)
                            else:
                                print("Insufficient Cash.")
                                print("Need Rs", payable - payment, "more.")
                        case 2:
                            print("You selected UPI Payment.")
                            payment = int(input("Enter UPI Amount: Rs "))

                            if payment == payable:
                                    print("UPI Payment Successful.")
                            else:
                                    print("UPI Payment Failed.")
                                    print("Amount should be exactly Rs", payable)
                        case 3:
                            print("You selected Card Payment.")
                            payment = int(input("Enter Card Payment Amount: Rs "))
                            if payment == payable:
                                print("Card Payment Successful.")
                            else:
                                print("Card Payment Failed.")
                                print("Amount should be exactly Rs", payable)
                        case _:
                            print("Invalid Payment Method.")
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