a  = int(input("Enter Your Attendance percentage : "))
if a >=75:
	print("Status : Eligible ")
elif 60<=a<=74:
	print("Status : Eligible With Warning ")
else:
	print("Status : Not Eligible")