a = int(input("Enter your number: "))

if a % 2 == 0:
    print("EVEN Number")
    
    if a % 5 == 0:
        print("Divisible by 5")
    else:
        print("Even but not divisible by 5")

else:
    print("TRY AGAIN!!!")