'''
# 7. Enterprise Password Pattern Strength Analyzer

A cybersecurity company wants to validate advanced passwords.

## Conditions:

* Minimum 10 characters
* At least:

  * 1 uppercase letter
  * 1 lowercase letter
  * 1 digit
  * 1 special character
* No consecutive repeating characters
* No spaces allowed

### Input:

text
Pyth@n1234


### Output:

text
Strong Password


### Input:

text
Paaass@12


### Output:

text
Weak Password

'''
n=input("Enter the string")
lower=0
upper=0
digit=0
special=0
if len(n)<10:
    print("invalid")
else:
    i=0
    while i<len(n):
        ch=n[i]
        cp=n[i-1]
        if ch==" ":
            print("invalid")
            break
        elif ch==cp:
           print("invalid due to consecutive")
           break
        elif 'a'<=ch<='z':
            lower=1
        elif 'A'<=ch<='Z':
            upper=1
        elif ch in '0123456789':
            digit=1
        else:
            special=1
        i+=1
    #print(lower,upper,digit,special)

    if lower==1 and upper==1 and digit==1 and special==1:
        print("strong password")
    else:
        print("weak password")
         