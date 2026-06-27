'''
. E-Learning Course Access System

An online learning platform grants access based on subscription type, course progress, and test score.

If subscription is premium, then check progress. If progress is at least 80, then check test score. If score is at least 70, unlock certificate; otherwise allow retry. If progress is less than 80, ask to complete course. If subscription is basic, then check progress. If progress is at least 50, allow limited access; otherwise lock content. If subscription is neither, deny access.

Input:
Subscription = premium
Progress = 85
Test Score = 65

Output:
Access Status = Retry Test

'''

subscription = input("Enter Your Subscription type(premium / basic): ").lower()
progress = int(input("Enter Your Progress: "))
testscore = int(input("Enter Your test Score: "))

if subscription == "premium":
	if progress >=80:
		if testscore >=70:
			print("ACCESS STATUS : CERTIFICATE UNLOCKED")
		else:
			print("ACCESS STATUS : RETRY TEST ")	
	else:
		print("COMPLETE THE COURSE")
elif  subscription == "basic":
	if progress >=50:
		print("ACCESS STATUS : LIMITED ACCESS ALLOWED")
		 
	else:
		print("ACCESS STATUS : LOCKED ")	
else: 
	print("ACCESS DENIED!!!!!!!!")