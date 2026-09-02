'''
2.
NUMBER ANALYSIS SYSTEM

Scenario:

A software company wants to develop a Number Analysis System. 
The application should be menu-driven and perform different mathematical operations on a given number.

MENU

1. Check Perfect Number
2. Check Prime Number
3. Find Reverse of a Number
4. Calculate Factorial
5. Display Factors of a Number
6. Exit

Requirements

Choice 1 – Check Perfect Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return True if the number is Perfect, otherwise False.
* Display an appropriate message based on the returned value.

Choice 2 – Check Prime Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return a message such as "Prime Number" or "Not a Prime Number".
* Display the returned message.

Choice 3 – Find Reverse of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return the reversed number.
* Display the returned value.

Choice 4 – Calculate Factorial

* Accept a number from the user.
* Pass the number to a function.
* The function should return the factorial value.
* Display the returned value.

Choice 5 – Display Factors of a Number

* Accept a number from the user.
* Pass the number to a function.
* The function should return all factors of the given number.
* Display the returned factors.

Choice 6 – Exit

Sample Output

Enter Choice : 1

Enter Number : 28

28 is a Perfect Number

---

Enter Choice : 2

Enter Number : 17

Prime Number

---

Enter Choice : 3

Enter Number : 1234

Reverse Number : 4321

---

Enter Choice : 4
Enter Number : 5
Factorial : 120

---
Enter Choice : 5
Enter Number : 12
Factors : 1 2 3 4 6 12

---
Important Instructions
1. Create separate functions for each operation.
2. Use parameters to pass values to functions.
3. Use return statements appropriately.
4. Different functions should return different types of values such as Boolean, String, Integer, and Collection/List.
5. Avoid using global variables.
6. Implement the solution using a menu-driven approach.
7. Write meaningful function names and maintain proper code readability.
'''

def perfect(x):
    sum=0
    temp = x
    for i in range(1, (x//2)+1):
        if x%i==0:
            sum+=i
    if temp ==sum:
        # print("NUMBER IS PERFECT")
        return True
    else:
        return False
        # print("NUMBER IS NOT PERFECT")

def prime(x):
    count = 0
    if x<2:
        return "NOT PRIME"
    else:
        for i in range(2,(x//2)+1):
            if x%i==0:
                count+=1
        if count==0:
            return "PRIME"
        else:
            return "NOT PRIME"

def  reverse(x):
    reverse = 0
    while x> 0:
        digit = x % 10
        reverse = reverse*10+digit
        x = x//10
    return reverse

def factorial(x):
    fact =1
    for i in range(1, x+1):
        fact= fact*i
    return fact

def factors(x):
    factor_list = []
    for i in range(1, x + 1):
        if x%i== 0:
            factor_list.append(i)
    return factor_list

while True:

    print("\n******** NUMBER ANALYSIS SYSTEM ********")
    print("1. Check Perfect Number")
    print("2. Check Prime Number")
    print("3. Find Reverse of a Number")
    print("4. Calculate Factorial")
    print("5. Display Factors of a Number")
    print("6. Exit")
    choice = int(input("\nEnter Choice : "))
    match choice:
        case 1:
            x = int(input("Enter the number to check: "))
            print("NUMBER IS PERFECT: ", perfect(x))
        case 2:
            x = int(input("Enter the number to check: "))
            print("NUMBER IS : ", prime(x))
        case 3:
            x = int(input("Enter the number to check: "))
            print("Reversed number is : ", reverse(x))
        case 4:
            x = int(input("Enter the number to check: "))
            print("FACTORIAL IS : ", factorial(x))
        case 5:
            x = int(input("Enter the number to check: "))
            print("Factors Are: ", factors(x))
        case 6:
            print("EXIT")
            break
        case _:
            print("PLEASE CHOOSE APPROPRIATE OPTION")