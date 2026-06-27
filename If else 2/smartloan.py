'''
Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%

'''


salary, age, credscore = map(int, input("ENTER YOUR salary, age, credscore,: ").split())

if salary >= 40000:
    if 60 >= age >= 21:
        if credscore >= 750:
            if emi <= 0.40 * salary:
                print("APPROVED AT 8%")
            else:
                print("APPROVED AT 10%")
        elif credscore >= 650:
            print("APPROVED AT 12%")
        else:
            print("REJECTED")
    else:
        print("UNDER AGE")

else:  
    if salary >= 25000 and credscore >= 700:
        print("APPROVED AT 13%")
    else:
        print("REJECTED")