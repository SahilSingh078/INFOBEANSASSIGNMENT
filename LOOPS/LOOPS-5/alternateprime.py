'''
Alternate Digit Prime Checker
A math lab adds alternate digits from right side.
Write a program to:
- Find sum of alternate digits
- Check whether sum is Prime or Not
Input:
12345
Output:
Alternate Sum = 9
Not Prime
'''

n = int(input("Enter Your number: "))

sum = 0
count = 0

while n > 0:
    digit = n% 10

    if count % 2 == 0:      
        sum += digit

    count += 1
    n = n // 10

print("Alternate Sum =", sum)

b = 0
for i in range(1, sum + 1):
    if sum % i == 0:
        b += 1

if b == 2:
    print("Prime")
else:
    print("Not Prime")