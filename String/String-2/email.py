'''
1.
Email Username Validator
A company wants to check whether an employee email username is valid before creating an official account.
Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters
Input:
Enter username: aja
123
Output:
Valid Username
'''
a = input("Enter the Username: ")
flag = True

if 5 <= len(a) <= 12:
    ch = a[0]

    if ((ch >= "A" and ch <= "Z") or (ch >= "a" and ch <= "z")):

        for i in range(len(a)):
            ch = a[i]

            if ((ch>= "A" and ch<="Z") or
                (ch >="a" and ch<= "z") or
                (ch>= "0" and ch<="9") or
                ch == "_"):
                pass
            else:
                flag = False
                break

        if flag == True:
            print("Valid Username")
        else:
            print("Invalid Username")

    else:
        print("Invalid Username")

else:
    print("Invalid Username")