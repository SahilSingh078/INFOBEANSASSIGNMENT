a = input("Enter the Transaction id: ")
temp = a
rev = a[::-1]
diff = abs(int(a)-int(rev))
l = len(str(diff))
print("Reverse = ", rev)
print("Diiference = ", diff)
print("Digits= ", l)
if diff == 0:
	print("Perfect match")
elif diff %9==0:
	print("VErified")
else:
	print("rejected")
