import random
print("\n===== WELCOME TO THE CITADEL MALL  =====")
choice = input("How did you come here? (1. car/2. bike/3. walk): ").lower()
parking_fee = 0
match choice:
    case "1":
        print("PARKING FEE -> 50.")
        parking_fee = 50
    case "2":
        print("PARKING FEE -> 20.")
        parking_fee = 20
    case "3":
        print("NO PARKING FEE FOR WALKING IN.")
        parking_fee = 0
    case _:
        print("INVALID CHOICE. DEFAULTING TO NO PARKING FEE.")
while True:
    print("\n========== MAIN MENU ==========")
    print("1. ENTER THE MALL")
    print("2. EXIT")
    choice = int(input("Enter Your Choice: "))
    match choice:
        case 1:
            print("\n===== ENTERING THE MALL =====")
            choice = input("DO YOU WANT TO GO SHOPPING OR PLAY GAMES? (1. SHOPPING/2. GAMES): ").lower()
            match choice:
                case "1":
                    print("\n===== SHOPPING SECTION =====")
                    age_group = input("ARE YOU A CHILD OR AN ADULT? (1. CHILD/2. ADULT): ").lower()
                    match age_group:
                        case "2":
                            print("YOU ARE AN ADULT.")
                            choice = int(input("ARE YOU A MAN OR A WOMAN? (1.MAN/2.WOMAN): "))
                            match choice:
                                # ============================================================
                                #                       MEN'S SECTION
                                # ============================================================
                                case 1:
                                    print("\n--- MEN'S SECTION ---")
                                    shirt_value = 0
                                    pant_value = 0
                                    jacket_value = 0
                                    while True:
                                        choice = input("WHAT DO YOU WANT TO BUY? (1. SHIRT/2. PANT/3. JACKET): ").lower()
                                        match choice:
                                            case "1":
                                                print("YOU CHOSE TO BUY A SHIRT.")
                                                while True:
                                                    brand = input("WHICH BRAND DO YOU PREFER? (1. VASTRADO /2. ALLEN SOLLY /3. SNITCH): ").lower()
                                                    match brand:
                                                        case "1":
                                                            print("YOU CHOSE VASTRADO BRAND FOR THE SHIRT.")
                                                            print("1. Vastrado - Casual Shirt - Rs700")
                                                            print("2. Vastrado - Formal Shirt - Rs800")
                                                            print("3. Vastrado - Designer Shirt - Rs1400")
                                                            print("4. Vastrado - Floral Shirt - Rs900")
                                                            print("5. Vastrado - Linen Shirt - Rs1100")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    shirt_value+=700
                                                                case 2: 
                                                                    shirt_value+=800
                                                                case 3: 
                                                                    shirt_value +=1400
                                                                case 4: 
                                                                    shirt_value +=900
                                                                case 5: 
                                                                    shirt_value +=1100
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case "2":
                                                            print("YOU CHOSE ALLEN SOLLY BRAND FOR THE SHIRT.")
                                                            print("1. Allen Solly - Casual Shirt - Rs1100")
                                                            print("2. Allen Solly - Formal Shirt - Rs1400")
                                                            print("3. Allen Solly - Designer Shirt - Rs1600")
                                                            print("4. Allen Solly - Floral Shirt - Rs1200")
                                                            print("5. Allen Solly - Linen Shirt - Rs1150")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    shirt_value += 1100
                                                                case 2: 
                                                                    shirt_value += 1400
                                                                case 3: 
                                                                    shirt_value += 1600
                                                                case 4: 
                                                                    shirt_value += 1200
                                                                case 5: 
                                                                    shirt_value += 1150
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case "3":
                                                            print("YOU CHOSE SNITCH BRAND FOR THE SHIRT.")
                                                            print("1. Snitch - Casual Shirt - Rs900")
                                                            print("2. Snitch - Formal Shirt - Rs1000")
                                                            print("3. Snitch - Designer Shirt - Rs1300")
                                                            print("4. Snitch - Floral Shirt - Rs950")
                                                            print("5. Snitch - Linen Shirt - Rs1050")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    shirt_value += 900
                                                                case 2: 
                                                                    shirt_value += 1000
                                                                case 3: 
                                                                    shirt_value += 1300
                                                                case 4: 
                                                                    shirt_value += 950
                                                                case 5: 
                                                                    shirt_value += 1050
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue
                                                    print("Total Shirt Cart Value =", shirt_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER SHIRT? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                            case "2":
                                                print("YOU CHOSE TO BUY A PANT.")
                                                while True:
                                                    brand = input("WHICH BRAND DO YOU PREFER? (1. LEVI'S /2. BALENCIAGA /3. PETER ENGLAND): ").lower()
                                                    match brand:
                                                        case "1":
                                                            print("YOU CHOSE LEVI'S BRAND FOR THE PANT.")
                                                            print("1. Levi's - Casual Pant - Rs1200")
                                                            print("2. Levi's - Formal Pant - Rs900")
                                                            print("3. Levi's - Straight Fit Pant - Rs1100")
                                                            print("4. Levi's - Jeans Pant - Rs1300")
                                                            print("5. Levi's - Baggy Pant - Rs1500")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    pant_value += 1200
                                                                case 2: 
                                                                    pant_value += 900
                                                                case 3: 
                                                                    pant_value += 1100
                                                                case 4: 
                                                                    pant_value += 1300
                                                                case 5: 
                                                                    pant_value += 1500
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case "2":
                                                            print("YOU CHOSE BALENCIAGA BRAND FOR THE PANT.")
                                                            print("1. Balenciaga - Casual Pant - Rs2100")
                                                            print("2. Balenciaga - Formal Pant - Rs2500")
                                                            print("3. Balenciaga - Straight Fit Pant - Rs3000")
                                                            print("4. Balenciaga - Jeans Pant - Rs3500")
                                                            print("5. Balenciaga - Baggy Pant - Rs4000")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    pant_value += 2100
                                                                case 2: 
                                                                    pant_value += 2500
                                                                case 3: 
                                                                    pant_value += 3000
                                                                case 4: 
                                                                    pant_value += 3500
                                                                case 5: 
                                                                    pant_value += 4000
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case "3":
                                                            print("YOU CHOSE PETER ENGLAND BRAND FOR THE PANT.")
                                                            print("1. Peter England - Casual Pant - Rs1050")
                                                            print("2. Peter England - Formal Pant - Rs900")
                                                            print("3. Peter England - Straight Fit Pant - Rs1200")
                                                            print("4. Peter England - Jeans Pant - Rs1100")
                                                            print("5. Peter England - Baggy Pant - Rs1000")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    pant_value += 1050
                                                                case 2: 
                                                                    pant_value += 900
                                                                case 3: 
                                                                    pant_value += 1200
                                                                case 4: 
                                                                    pant_value += 1100
                                                                case 5: 
                                                                    pant_value += 1000
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue
                                                    print("Current Pant Cart Value =", pant_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER PANT? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                                print("TOTAL PANT CART VALUE =", pant_value)
                                            case "3":
                                                print("YOU CHOSE TO BUY A JACKET.")
                                                while True:
                                                    brand = input("WHICH BRAND DO YOU PREFER? (1. VAN HEUSEN/2. JACK & JONES/3. PUMA): ").lower()
                                                    match brand:
                                                        case "1":
                                                            print("YOU CHOSE VAN HEUSEN BRAND FOR THE JACKET.")
                                                            print("1. Van Heusen - Casual Jacket - Rs2500")
                                                            print("2. Van Heusen - Formal Jacket - Rs3000")
                                                            print("3. Van Heusen - Leather Jacket - Rs4000")
                                                            print("4. Van Heusen - Bomber Jacket - Rs3500")
                                                            print("5. Van Heusen - Denim Jacket - Rs2800")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    jacket_value += 2500
                                                                case 2: 
                                                                    jacket_value += 3000
                                                                case 3: 
                                                                    jacket_value += 4000
                                                                case 4: 
                                                                    jacket_value += 3500
                                                                case 5: 
                                                                    jacket_value += 2800
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case "2":
                                                            print("YOU CHOSE JACK & JONES BRAND FOR THE JACKET.")
                                                            print("1. Jack & Jones - Casual Jacket - Rs2200")
                                                            print("2. Jack & Jones - Formal Jacket - Rs2700")
                                                            print("3. Jack & Jones - Leather Jacket - Rs3500")
                                                            print("4. Jack & Jones - Bomber Jacket - Rs3000")
                                                            print("5. Jack & Jones - Denim Jacket - Rs2500")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    jacket_value += 2200
                                                                case 2: 
                                                                    jacket_value += 2700
                                                                case 3: 
                                                                    jacket_value += 3500
                                                                case 4: 
                                                                    jacket_value += 3000
                                                                case 5: 
                                                                    jacket_value += 2500
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case "3":
                                                            print("YOU CHOSE PUMA BRAND FOR THE JACKET.")
                                                            print("1. Puma - Casual Jacket - Rs2200")
                                                            print("2. Puma - Formal Jacket - Rs2700")
                                                            print("3. Puma - Leather Jacket - Rs3500")
                                                            print("4. Puma - Bomber Jacket - Rs3000")
                                                            print("5. Puma - Denim Jacket - Rs2500")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    jacket_value += 2200
                                                                case 2: 
                                                                    jacket_value += 2700
                                                                case 3: 
                                                                    jacket_value += 3500
                                                                case 4: 
                                                                    jacket_value += 3000
                                                                case 5: 
                                                                    jacket_value += 2500
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue
                                                    print("CURRENT JACKET CART VALUE  =", jacket_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER JACKET? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                                print("TOTAL JACKET CART VALUE =", jacket_value)
                                            case _:
                                                print("Invalid choice.")
                                                continue
                                        again = input("\nDO YOU WANT TO BUY ANOTHER CATEGORY? (yes/no): ").lower()
                                        if again == "yes":
                                            continue   
                                        else:
                                            break      

                                    print("\n----- BILL -----")
                                    print("Parking Fee  :", parking_fee)
                                    print("Shirt Total  :", shirt_value)
                                    print("Pant Total   :", pant_value)
                                    print("Jacket Total :", jacket_value)
                                    grand_total = parking_fee + shirt_value + pant_value + jacket_value
                                    print("GRAND TOTAL      :", grand_total)

                                    print("\n===== PAYMENT SECTION =====")
                                    print("1. Cash")
                                    print("2. UPI")
                                    print("3. Card")
                                    method = int(input("Choose Payment Method: "))
                                    match method:
                                        case 1:
                                            print("You selected Cash Payment.")
                                            payment = int(input("Enter Cash Amount: Rs "))

                                            if payment == grand_total:
                                                print("Payment Successful.")
                                            elif payment > grand_total:
                                                print("Payment Successful.")
                                                print("Return Change: Rs", payment - grand_total)
                                            else:
                                                print("Insufficient Cash.")
                                                print("Need Rs", grand_total - payment, "more.")
                                        case 2:
                                            print("You selected UPI Payment.")
                                            payment = int(input("Enter UPI Amount: Rs "))
                                            if payment == grand_total:
                                                    print("UPI Payment Successful.")
                                            else:
                                                    print("UPI Payment Failed.")
                                                    print("Amount should be exactly Rs", grand_total)
                                        case 3:
                                            print("You selected Card Payment.")
                                            payment = int(input("Enter Card Payment Amount: Rs "))
                                            if payment == grand_total:
                                                print("Card Payment Successful.")
                                            else:
                                                print("Card Payment Failed.")
                                                print("Amount should be exactly Rs", grand_total)
                                        case _:
                                            print("Invalid Payment Method.")
                                # ============================================================
                                #                       WOMEN'S SECTION
                                # ============================================================
                                case 2:
                                    print("\n--- WOMEN'S SECTION ---")
                                    tops_value = 0
                                    perfume_value = 0
                                    beauty_value = 0
                                    while True:
                                        choice = int(input("WHAT DO YOU WANT TO BUY? (1. TOPS/2. PERFUME /3. BEAUTY ACCESSORIES): "))
                                        match choice:
                                            case 1:
                                                print("YOU CHOSE TO BUY TOPS.")
                                                while True:
                                                    brand = int(input("WHICH BRAND DO YOU PREFER? (1. H&M /2. WESTSIDE /3. LOCAL): "))
                                                    match brand:
                                                        case 1:
                                                            print("YOU CHOSE H&M BRAND FOR THE TOPS.")
                                                            print("1. H&M - Peplum  - Rs700")
                                                            print("2. H&M - Cossack - Rs800")
                                                            print("3. H&M - Sailor - Rs1400")
                                                            print("4. H&M - Princess vest - Rs2100")
                                                            print("5. H&M - Smock - Rs1100")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    tops_value += 700
                                                                case 2: 
                                                                    tops_value += 800
                                                                case 3: 
                                                                    tops_value += 1400
                                                                case 4: 
                                                                    tops_value += 2100
                                                                case 5: 
                                                                    tops_value += 1100
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case 2:
                                                            print("YOU CHOSE WESTSIDE BRAND FOR THE TOPS.")
                                                            print("1. WestSide - Peplum  - Rs650")
                                                            print("2. WestSide - Cossack - Rs500")
                                                            print("3. WestSide - Sailor - Rs900")
                                                            print("4. WestSide - Princess vest - Rs1100")
                                                            print("5. WestSide - Smock - Rs850")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    tops_value += 650
                                                                case 2: 
                                                                    tops_value += 500
                                                                case 3: 
                                                                    tops_value += 900
                                                                case 4: 
                                                                    tops_value += 1100
                                                                case 5: 
                                                                    tops_value += 850
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case 3:
                                                            print("YOU CHOSE LOCAL BRAND FOR THE TOPS.")
                                                            print("1. Local - Ramesh Cut Top  - Rs150")
                                                            print("2. Local - Rajwada Special - Rs300")
                                                            print("3. Local - Indori Special - Rs400")
                                                            print("4. Local - Shalimar Tops - Rs350")
                                                            print("5. Local - Rewari Chinkari - Rs550")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    tops_value += 150
                                                                case 2: 
                                                                    tops_value += 300
                                                                case 3: 
                                                                    tops_value += 400
                                                                case 4: 
                                                                    tops_value += 350
                                                                case 5: 
                                                                    tops_value += 550
                                                                case _: 
                                                                    print("Invalid choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue

                                                    print("Current Tops Cart Value =", tops_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER TOP? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                            case 2:
                                                print("YOU CHOSE TO BUY A PERFUME.")
                                                while True:
                                                    brand = int(input("WHICH BRAND DO YOU PREFER? (1. GUCCI /2. BALENCIAGA /3. DIOR): "))
                                                    match brand:
                                                        case 1:
                                                            print("YOU CHOSE GUCCI BRAND FOR THE PERFUME.")
                                                            print("1. Gucci - Eau de Parfum - Rs2500")
                                                            print("2. Gucci - Floral Perfume - Rs2000")
                                                            print("3. Gucci - Citrus Perfume - Rs1800")
                                                            print("4. Gucci - Woodsy Perfume - Rs2200")
                                                            print("5. Gucci - Oriental Perfume - Rs2800")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    perfume_value += 2500
                                                                case 2: 
                                                                    perfume_value += 2000
                                                                case 3: 
                                                                    perfume_value += 1800
                                                                case 4: 
                                                                    perfume_value += 2200
                                                                case 5: 
                                                                    perfume_value += 2800
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case 2:
                                                            print("YOU CHOSE BALENCIAGA BRAND FOR THE PERFUME.")
                                                            print("1. Balenciaga - Eau de Parfum - Rs2100")
                                                            print("2. Balenciaga - Floral Perfume - Rs2500")
                                                            print("3. Balenciaga - Citrus Perfume - Rs3000")
                                                            print("4. Balenciaga - Woodsy Perfume - Rs3500")
                                                            print("5. Balenciaga - Oriental Perfume - Rs4000")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    perfume_value += 2100
                                                                case 2: 
                                                                    perfume_value += 2500
                                                                case 3: 
                                                                    perfume_value += 3000
                                                                case 4: 
                                                                    perfume_value += 3500
                                                                case 5: 
                                                                    perfume_value += 4000
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case 3:
                                                            print("YOU CHOSE DIOR BRAND FOR THE PERFUME.")
                                                            print("1. Dior - Sauvage - Rs2100")
                                                            print("2. Dior - Miss Dior - Rs2500")
                                                            print("3. Dior - Lady Dior - Rs3000")
                                                            print("4. Dior - Christian Dior - Rs3500")
                                                            print("5. Dior - Diorissimo - Rs4000")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    perfume_value += 2100
                                                                case 2: 
                                                                    perfume_value += 2500
                                                                case 3: 
                                                                    perfume_value += 3000
                                                                case 4: 
                                                                    perfume_value += 3500
                                                                case 5: 
                                                                    perfume_value += 4000
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue
                                                    print("Current Perfume Cart Value =", perfume_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER PERFUME? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                                print("TOTAL PERFUME CART VALUE =", perfume_value)
                                            case 3:
                                                print("YOU CHOSE TO BUY BEAUTY ACCESSORIES.")
                                                while True:
                                                    brand = int(input("WHICH BRAND DO YOU PREFER? (1. RENEE/2. GIVA /3. SWISS BEAUTY): "))
                                                    match brand:
                                                        case 1:
                                                            print("YOU CHOSE RENEE BRAND FOR THE BEAUTY ACCESSORY.")
                                                            print("1. Renee - Moisturizer - Rs1500")
                                                            print("2. Renee - Serum - Rs1200")
                                                            print("3. Renee - Face Wash - Rs900")
                                                            print("4. Renee - Sunscreen(SPF-50++) - Rs1500")
                                                            print("5. Renee - Lip Balm - Rs400")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    beauty_value += 1500
                                                                case 2: 
                                                                    beauty_value += 1200
                                                                case 3: 
                                                                    beauty_value += 900
                                                                case 4: 
                                                                    beauty_value += 1500
                                                                case 5: 
                                                                    beauty_value += 400
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case 2:
                                                            print("YOU CHOSE GIVA BRAND FOR BEAUTY ACCESSORIES.")
                                                            print("1. Giva - Diamond Ring - Rs3500")
                                                            print("2. Giva - Anklets - Rs2000")
                                                            print("3. Giva - Necklace - Rs2500")
                                                            print("4. Giva - Earrings - Rs1500")
                                                            print("5. Giva - Mystery Gift (up to Rs10000) - Rs5000")
                                                            item = int(input("ENTER YOUR CHOICE: "))
                                                            match item:
                                                                case 1: 
                                                                    beauty_value += 3500
                                                                case 2: 
                                                                    beauty_value += 2000
                                                                case 3: 
                                                                    beauty_value += 2500
                                                                case 4: 
                                                                    beauty_value += 1500
                                                                case 5: 
                                                                    beauty_value += 5000
                                                                case _: 
                                                                    print("Invalid Choice.")
                                                        case _:
                                                            print("SORRY! BRAND NOT AVAILABLE.")
                                                            continue

                                                    print("Current Beauty Cart Value =", beauty_value)
                                                    again = input("DO YOU WANT TO BUY ANOTHER BEAUTY PRODUCT? (yes/no): ").lower()
                                                    if again == "yes":
                                                        continue
                                                    else:
                                                        break
                                                print("TOTAL BEAUTY CART VALUE =", beauty_value)
                                            case _:
                                                print("Invalid choice.")
                                                continue
                                        again = input("\nDO YOU WANT TO BUY ANOTHER CATEGORY? (yes/no): ").lower()
                                        if again == "yes":
                                            continue
                                        else:
                                            break
                                    print("\n----- BILL -----")
                                    print("Parking Fee    :", parking_fee)
                                    print("Tops Total     :", tops_value)
                                    print("Perfume Total  :", perfume_value)
                                    print("Beauty Total   :", beauty_value)
                                    grand_total = parking_fee + tops_value + perfume_value + beauty_value
                                    print("GRAND TOTAL    :", grand_total)
                                    print("\n===== PAYMENT SECTION =====")
                                    print("1. Cash")
                                    print("2. UPI")
                                    print("3. Card")
                                    method = int(input("Choose Payment Method: "))
                                    match method:
                                        case 1:
                                            print("You selected Cash Payment.")
                                            payment = int(input("Enter Cash Amount: Rs "))
                                            if payment == grand_total:
                                                print("Payment Successful.")
                                            elif payment > grand_total:
                                                print("Payment Successful.")
                                                print("Return Change: Rs", payment - grand_total)
                                            else:
                                                print("Insufficient Cash.")
                                                print("Need Rs", grand_total - payment, "more.")
                                        case 2:
                                            print("You selected UPI Payment.")
                                            payment = int(input("Enter UPI Amount: Rs "))
                                            if payment == grand_total:
                                                    print("UPI Payment Successful.")
                                            else:
                                                    print("UPI Payment Failed.")
                                                    print("Amount should be exactly Rs", grand_total)
                                        case 3:
                                            print("You selected Card Payment.")
                                            payment = int(input("Enter Card Payment Amount: Rs "))
                                            if payment == grand_total:
                                                print("Card Payment Successful.")
                                            else:
                                                print("Card Payment Failed.")
                                                print("Amount should be exactly Rs", grand_total)
                                        case _:
                                            print("Invalid Payment Method.")
                        case "1":
                            print("\n--- CHILD SECTION ---")
                            kidswear_value = 0
                            toys_value = 0
                            footwear_value = 0
                            while True:
                                choice = input("WHAT DO YOU WANT TO BUY? (1. KIDWEAR/2. TOYS/3. FOOTWEAR): ").lower()
                                match choice:
                                    case "1":
                                        print("YOU CHOSE TO BUY KIDWEAR.")
                                        while True:
                                            brand = input("WHICH BRAND DO YOU PREFER? (1. H&M KIDS /2. HOPSCOTCH /3. LOCAL): ").lower()
                                            match brand:
                                                case "1":
                                                    print("YOU CHOSE H&M KIDS BRAND FOR THE KIDWEAR.")
                                                    print("1. H&M Kids - T-Shirt - Rs450")
                                                    print("2. H&M Kids - Shorts - Rs500")
                                                    print("3. H&M Kids - Trouser - Rs900")
                                                    print("4. H&M Kids - Frock - Rs700")
                                                    print("5. H&M Kids - Winter Jacket - Rs1200")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            kidswear_value += 450
                                                        case 2: 
                                                            kidswear_value += 500
                                                        case 3:
                                                            kidswear_value += 900
                                                        case 4: 
                                                            kidswear_value += 700
                                                        case 5:
                                                            kidswear_value += 1200
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "2":
                                                    print("YOU CHOSE HOPSCOTCH BRAND FOR THE KIDWEAR.")
                                                    print("1. Hopscotch - T-Shirt - Rs550")
                                                    print("2. Hopscotch - Shorts - Rs600")
                                                    print("3. Hopscotch - Trouser - Rs1000")
                                                    print("4. Hopscotch - Frock - Rs850")
                                                    print("5. Hopscotch - Winter Jacket - Rs1400")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            kidswear_value += 550
                                                        case 2: 
                                                            kidswear_value += 600
                                                        case 3: 
                                                            kidswear_value += 1000
                                                        case 4: 
                                                            kidswear_value += 850
                                                        case 5: 
                                                            kidswear_value += 1400
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "3":
                                                    print("YOU CHOSE LOCAL BRAND FOR THE KIDWEAR.")
                                                    print("1. Ramesh Clothing     - T-Shirt  - Rs200")
                                                    print("2. Lallan Wears        - Shorts   - Rs250")
                                                    print("3. Rewa Collections    - Trouser  - Rs450")
                                                    print("4. Supriya Collections - Frock    - Rs350")
                                                    print("5. Manyavar Collection - Jacket   x- Rs600")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            kidswear_value += 200
                                                        case 2: 
                                                            kidswear_value += 250
                                                        case 3: 
                                                            kidswear_value += 450
                                                        case 4: 
                                                            kidswear_value += 350
                                                        case 5: 
                                                            kidswear_value += 600
                                                        case _: 
                                                            print("Invalid choice.")
                                                case _:
                                                    print("SORRY! BRAND NOT AVAILABLE.")
                                                    continue
                                            print("Current Kidswear Cart Value =", kidswear_value)
                                            again = input("DO YOU WANT TO BUY ANOTHER KIDWEAR ITEM? (yes/no): ").lower()
                                            if again == "yes":
                                                continue
                                            else:
                                                break
                                        print("TOTAL KIDSWEAR CART VALUE =", kidswear_value)
                                    case "2":
                                        print("YOU CHOSE TO BUY TOYS.")
                                        while True:
                                            brand = input("WHICH BRAND DO YOU PREFER? (1. LEGO /2. HOT WHEELS /3. HAMLEYS): ").lower()
                                            match brand:
                                                case "1":
                                                    print("YOU CHOSE LEGO BRAND FOR THE TOYS.")
                                                    print("1. LEGO - City Set         - Rs1500")
                                                    print("2. LEGO - Classic Bricks   - Rs900")
                                                    print("3. LEGO - Mechanic Set     - Rs2500")
                                                    print("4. LEGO - Dragon Set       - Rs1800")
                                                    print("5. LEGO - Star Wars Set    - Rs3200")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            toys_value += 1500
                                                        case 2: 
                                                            toys_value += 900
                                                        case 3: 
                                                            toys_value += 2500
                                                        case 4: 
                                                            toys_value += 1800
                                                        case 5: 
                                                            toys_value += 3200
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "2":
                                                    print("YOU CHOSE HOT WHEELS BRAND FOR THE TOYS.")
                                                    print("1. Hot Wheels - Single Car       - Rs150")
                                                    print("2. Hot Wheels - 5-Car Pack       - Rs700")
                                                    print("3. Hot Wheels - Track Set        - Rs1400")
                                                    print("4. Hot Wheels - Garage Playset   - Rs2200")
                                                    print("5. Hot Wheels - Monster Truck    - Rs800")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            toys_value += 150
                                                        case 2: 
                                                            toys_value += 700
                                                        case 3: 
                                                            toys_value += 1400
                                                        case 4: 
                                                            toys_value += 2200
                                                        case 5: 
                                                            toys_value += 800
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "3":
                                                    print("YOU CHOSE HAMLEYS BRAND FOR THE TOYS.")
                                                    print("1. HAMLEYS - PUZZLE SET      - Rs4000")
                                                    print("2. HAMLEYS - BOARD GAME      - Rs1500")
                                                    print("3. HAMLEYS - SOFT TOY        - Rs1750")
                                                    print("4. HAMLEYS - ACTION FIGURE   - Rs4500")
                                                    print("5. HAMLEYS - BUILDING BLOCKS - Rs1500")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            toys_value += 400
                                                        case 2: 
                                                            toys_value += 700
                                                        case 3: 
                                                            toys_value += 550
                                                        case 4: 
                                                            toys_value += 450
                                                        case 5: 
                                                            toys_value += 900
                                                        case _: 
                                                            print("Invalid choice.")
                                                case _:
                                                    print("SORRY! BRAND NOT AVAILABLE.")
                                                    continue

                                            print("Current Toys Cart Value =", toys_value)
                                            again = input("DO YOU WANT TO BUY ANOTHER TOY? (YES/NO): ").lower()
                                            if again == "yes":
                                                continue
                                            else:
                                                break
                                        print("TOTAL TOYS CART VALUE =", toys_value)
                                    case "3":
                                        print("YOU CHOSE TO BUY FOOTWEAR.")
                                        while True:
                                            brand = input("WHICH BRAND DO YOU PREFER? (1. BATA /2. SKECHERS KIDS /3. RAMESH SHOES HOUSE): ").lower()
                                            match brand:
                                                case "1":
                                                    print("YOU CHOSE BATA BRAND FOR THE FOOTWEAR.")
                                                    print("1. Bata - School Shoes      - Rs800")
                                                    print("2. Bata - Sandals           - Rs500")
                                                    print("3. Bata - Sneakers          - Rs900")
                                                    print("4. Bata - Sports Shoes      - Rs1100")
                                                    print("5. Bata - Slippers          - Rs300")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            footwear_value += 800
                                                        case 2: 
                                                            footwear_value += 500
                                                        case 3: 
                                                            footwear_value += 900
                                                        case 4: 
                                                            footwear_value += 1100
                                                        case 5: 
                                                            footwear_value += 300
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "2":
                                                    print("YOU CHOSE SKECHERS KIDS BRAND FOR THE FOOTWEAR.")
                                                    print("1. SKECHERS KIDS - SCHOOL SHOES      - Rs1400")
                                                    print("2. SKECHERS KIDS - SANDALS           - Rs900")
                                                    print("3. SKECHERS KIDS - SNEAKERS          - Rs1600")
                                                    print("4. SKECHERS KIDS - SPORTS SHOES      - Rs1800")
                                                    print("5. SKECHERS KIDS - SLIPPERS          - Rs600")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            footwear_value += 1400
                                                        case 2: 
                                                            footwear_value += 900
                                                        case 3: 
                                                            footwear_value += 1600
                                                        case 4: 
                                                            footwear_value += 1800
                                                        case 5: 
                                                            footwear_value += 600
                                                        case _: 
                                                            print("Invalid choice.")
                                                case "3":
                                                    print("YOU CHOSE RAMESH SHOES HOUSE BRAND FOR THE FOOTWEAR.")
                                                    print("1. RAMESH SHOES HOUSE - SCHOOL SHOES      - Rs350")
                                                    print("2. RAMESH SHOES HOUSE - SANDALS           - Rs200")
                                                    print("3. RAMESH SHOES HOUSE - SNEAKERS          - Rs400")
                                                    print("4. RAMESH SHOES HOUSE - SPORTS SHOES      - Rs500")
                                                    print("5. RAMESH SHOES HOUSE - SLIPPERS          - Rs120")
                                                    item = int(input("ENTER YOUR CHOICE: "))
                                                    match item:
                                                        case 1: 
                                                            footwear_value += 350
                                                        case 2: 
                                                            footwear_value += 200
                                                        case 3: 
                                                            footwear_value += 400
                                                        case 4: 
                                                            footwear_value += 500
                                                        case 5: 
                                                            footwear_value += 120
                                                        case _: 
                                                            print("Invalid choice.")
                                                case _:
                                                    print("SORRY! BRAND NOT AVAILABLE.")
                                                    continue
                                            print("Current Footwear Cart Value =", footwear_value)
                                            again = input("DO YOU WANT TO BUY ANOTHER FOOTWEAR ITEM? (YES/NO): ").lower()
                                            if again == "yes":
                                                continue
                                            else:
                                                break
                                        print("TOTAL FOOTWEAR CART VALUE =", footwear_value)
                                    case _:
                                        print("Invalid choice.")
                                        continue

                                again = input("\nDO YOU WANT TO BUY ANOTHER CATEGORY? (YES/NO): ").lower()
                                if again == "yes":
                                    continue
                                else:
                                    break

                            print("\n----- BILL -----")
                            print("Parking Fee     :", parking_fee)
                            print("Kidswear Total  :", kidswear_value)
                            print("Toys Total      :", toys_value)
                            print("Footwear Total  :", footwear_value)
                            grand_total = parking_fee + kidswear_value + toys_value + footwear_value
                            print("GRAND TOTAL     :", grand_total)
                            
                            print("\n===== PAYMENT SECTION =====")
                            print("1. Cash")
                            print("2. UPI")
                            print("3. Card")
                            method = int(input("Choose Payment Method: "))
                            match method:
                                case 1:
                                    print("You selected Cash Payment.")
                                    payment = int(input("Enter Cash Amount: Rs "))
                                    if payment == grand_total:
                                        print("Payment Successful.")
                                    elif payment > grand_total:
                                        print("Payment Successful.")
                                        print("Return Change: Rs", payment - grand_total)
                                    else:
                                        print("Insufficient Cash.")
                                        print("Need Rs", grand_total - payment, "more.")
                                case 2:
                                    print("You selected UPI Payment.")
                                    payment = int(input("Enter UPI Amount: Rs "))
                                    if payment == grand_total:
                                            print("UPI Payment Successful.")
                                    else:
                                            print("UPI Payment Failed.")
                                            print("Amount should be exactly Rs", grand_total)
                                case 3:
                                    print("You selected Card Payment.")
                                    payment = int(input("Enter Card Payment Amount: Rs "))
                                
                                    if payment == grand_total:
                                        print("Card Payment Successful.")
                                    else:
                                        print("Card Payment Failed.")
                                        print("Amount should be exactly Rs", grand_total)
                                case _:
                                    print("Invalid Payment Method.")

                        case _:
                            print("Invalid choice.")
                case "2":
                    print("\n===== GAMES SECTION =====")
                    while True:
                        print("1. Number Guessing Game")
                        game_choice = int(input("Which game do you want to play? "))
                        match game_choice: 
                            case 1:
                                print("==============================================")
                                print("Welcome to number guessing game ")
                                print("Guess the number between 0 to 100")
                                num = random.randint(1, 100)
                                print("Start guessing number\n ")
                                c = 1
                                while True:
                                    print("Attempt :", c)
                                    value = int(input("Enter Number :"))

                                    if value < 0 or value > 100:
                                        print("please Enter number between 0 to 100")
                                        continue
                                    elif num == value:
                                        print(" ===========================================")
                                        print("|| Congratulations you won in", c, "Attempts ||")
                                        print("===========================================\n")
                                        break
                                    elif num > value:
                                        print("Number is Greater!\n")
                                    else:
                                        print("Number is Smaller!\n")
                                    c = c + 1
                            case _:
                                print("Invalid choice.")
                        again = input("\nDo you want to play another game? (yes/no): ").lower()
                        if again == "yes":
                            continue
                        else:
                            break
                case _:
                    print("Invalid choice.")
        case 2:
            print("\nThank you for visiting THE CITADEL MALL. Have a great day!")
            break
        case _: 
            print("Invalid choice. Please enter 1 or 2.")