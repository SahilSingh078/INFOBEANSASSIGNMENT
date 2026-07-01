
Lift Mode Operation – Advanced Smart Elevator System


'''
A smart building elevator works in multiple intelligent modes based on the mode number entered by the control panel.  
The system must automatically execute floor movement instructions using loops.
Write a program:
- If mode = 1  
  Normal Up Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in ascending order.
- Else if mode = 2  
  Down Mode activated.  
  Read current floor and destination floor.  
  Print all floors from current to destination in descending order.
- Else if mode = 3  
  Energy Saving Mode activated.  
  Read destination floor.  
  Lift starts from ground floor (0) and stops only on alternate floors till destination.
- Else  
  Emergency Mode activated.  
  Print "Emergency Alarm" 4 times using loop.
Input:
3
6
Output:
0 2 4 6
Input:
1
2
7
Output:
2 3 4 5 6 7
Input:
2
8
3
Output:
8 7 6 5 4 3
Input:
5
Output:
Emergency Alarm
Emergency Alarm
Emergency Alarm
Emergency Alarm
'''

''
n=input("Enter number = ")
l=len(n)
m=int(n)
sum=0
count=0
smallest=9
for i in n:
	if i=="0":
		count=count+1
print("Zero Count = ",count)
while m>0:
	r=m%10
	sum=sum+r
	if smallest>r:
		smallest=r
	m=m//10
print(f"Sum = {sum}")
print("Smallest Digit= {}".format(smallest))
new=sum*smallest
print("Final Result = ",new)
i=2
while i<=new:
	if new%i==0:
		count=count+1
	i=i+1
if count==0:
	print("Prime Number")
else:
	print("Not Prime Number")