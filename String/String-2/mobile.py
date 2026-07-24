'''
2.
Mobile Number Digit Counter
A telecom company wants to count how many digits are present in a customer contact number entered with spaces or symbols.
Input:
Enter contact number: +91 98765-43210
Output:
Total digits: 12
'''

a = input("Enter Contact Number: ")
count = 0
valid = True

for i in range(len(a)):
    ch = a[i]

    if ch >= "0" and ch <= "9":
        count = count + 1
    elif ch == " " or ch == "+" or ch == "-":
        pass
    else:
        print("ONLY DIGITS ARE LLOWED")
        valid = False
        break

if valid==True:
    print("Total digits:", count)