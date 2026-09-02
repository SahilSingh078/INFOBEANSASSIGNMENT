a = input("Enter the Number: ")
sum = 0
lar = 0
l = len(a)
print("step differeence: ", end=" ")
for i in range(len(a)-1):
	sd=""
	diff = abs(int(a[i])-int(a[i+1]))
	sd += str(diff)
	sum+=diff
	print(sd, end=" ")
	if diff>lar:
		lar=diff
print("\n sum: ", sum)
print("Largest", lar)

if sum%l==0:
	print("Balanced number")
else:
	print("Unbalanced number")

