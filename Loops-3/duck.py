n = input("num : ")
rev = ""
m = n
for i in m :
    rev = i + rev
n = int(n)
num = int(rev) % 10

while n>0 :
    if num == 0:
        print("reject")
        break
    else:
        d = n%10
        n = n//10
        if d == 0 :
            print("duck number")
            break
else :
    print("Not a duck number")