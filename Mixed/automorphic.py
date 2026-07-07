a = int(input("Enter The Numeric code: "))
l = len(str(a))
sq = a*a 
rem = sq % (10**l)
if rem == a:
	print("Automorphic Number")
else:
	print("Non automorphic number")