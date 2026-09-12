from perfect import is_perfect
from pallindrome import is_pall
from strong import is_strong
from armstrong import is_armstrong
from prime import is_prime
from evenodd import even_odd
from factorial import is_fact
from sum import is_sum
from reverse import is_reverse
from number_digits import number_digits
from automorphic import is_automorphic
from neon import is_neon
from spy import is_spy
from harshad import is_harshad

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
            print(is_perfect(x))
    
        case 2:
            x = int(input("Enter your number: "))
            print(is_pall(x))
    
        case 3:
            x = int(input("Enter your number: "))
            print(is_strong(x))
    
        case 4:
            x = int(input("Enter your number: "))
            print(is_armstrong(x))
    
        case 5:
            x = int(input("Enter your number: "))
            print(is_prime(x))
    
        case 6:
            x = int(input("Enter your number: "))
            print(even_odd(x))
    
        case 7:
            x = int(input("Enter your number: "))
            print(is_fact(x))
    
        case 8:
            x = int(input("Enter your number: "))
            print(is_sum(x))
    
        case 9:
            x = int(input("Enter your number: "))
            print(is_reverse(x))
    
        case 10:
            x = int(input("Enter your number: "))
            print(number_digits(x))
    
        case 11:
            x = int(input("Enter your number: "))
            print(is_automorphic(x))
    
        case 12:
            x = int(input("Enter your number: "))
            print(is_neon(x))
    
        case 13:
            x = int(input("Enter your number: "))
            print(is_spy(x))
    
        case 14:
            x = int(input("Enter your number: "))
            print(is_harshad(x))
    
        case 15:
            print("Thank you for using Number Analysis System!")
            print("Program terminated.")
            break
        
        case _:
            print("Invalid Choice!")
            print("Please select a choice between 1 and 15.")