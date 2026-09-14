import pck
while True:
    print('''
    ========================================
       NUMBER ANALYSIS SYSTEM
    ========================================

        1. Check Perfect Number
        2. Check Palindrome Number
        3. Check Strong Number
        4. Check Armstrong Number
        5. Check Prime Number
        6. Check Even or Odd
        7. Find Factorial
        8. Find Sum of Digits
        9. Reverse a Number
        10. Find Number of Digits
        11. Check Automorphic Number
        12. Check Neon Number
        13. Check Spy Number
        14. Check Harshad Number
        15. Exit'''
          )
    choice = int(input("Enter Your Choice: "))
    match choice:

        case 1:
            x = int(input("Enter your number: "))
            print(pck.is_perfect(x))

        case 2:
            x = int(input("Enter your number: "))
            print(pck.is_pall(x))

        case 3:
            x = int(input("Enter your number: "))
            print(pck.is_strong(x))

        case 4:
            x = int(input("Enter your number: "))
            print(pck.is_armstrong(x))

        case 5:
            x = int(input("Enter your number: "))
            print(pck.is_prime(x))

        case 6:
            x = int(input("Enter your number: "))
            print(pck.even_odd(x))

        case 7:
            x = int(input("Enter your number: "))
            print(pck.is_fact(x))

        case 8:
            x = int(input("Enter your number: "))
            print(pck.is_sum(x))

        case 9:
            x = int(input("Enter your number: "))
            print(pck.is_reverse(x))

        case 10:
            x = int(input("Enter your number: "))
            print(pck.number_digits(x))

        case 11:
            x = int(input("Enter your number: "))
            print(pck.is_automorphic(x))

        case 12:
            x = int(input("Enter your number: "))
            print(pck.is_neon(x))

        case 13:
            x = int(input("Enter your number: "))
            print(pck.is_spy(x))

        case 14:
            x = int(input("Enter your number: "))
            print(pck.is_harshad(x))

        case 15:
            print("Thank you for using Number Analysis System!")
            break

        case _:
            print("Please select a choice between 1 and 15.")


