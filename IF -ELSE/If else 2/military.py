'''
Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected

'''


age,bmi,running = map(int,input("ENTER YOUR AGE,BMI,RUNNING TIME: ").split())
med = input("ENTER YOUR MEDICAL CONDITION:").lower()
if 25>age>=18:
	if 25>bmi>=18:
		if running <=15:
			if med == "fit":
				print("Selection Status = SELECTED")
			else:
				print("Selection Status = MEDICAL REJECTED")
		else:
			print("Selection Status = PHYSICAL REJECTED")		
	else: 
		print("Selection Status = BMI FAIL")
elif 30>age>=26:
	if running <=14:
		if med == "fit":
			print("Selection Status = CONDITIONAL SELECTED")
		else:
			print("Selection Status = REJECTED ")
else:
	print("Selection Status = NOT ELIGIBLE")