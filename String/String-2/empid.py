'''
4.
Employee ID Validator
A company wants to validate employee IDs before storing them in the database.
Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only
Input:
Enter Employee ID: EMP10234
Output:
Valid Employee ID
'''

a = input("Enter Employee ID: ")
b = a[3:]
if len(a)==8  and a[0]=="E" and a[1] == "M" and a[2] == "P" :
    c=1
    for i in b:
        if  i < "0" or i>"9":
            c=0
            break
    if c==1:
        print("Valid Employee")
    else:
        print("Not Valid")        
        
else:
    print("Invalid Employee ID")