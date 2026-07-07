a,b,c=map(int,input("Enter your salary, working days and working hrs perday [with space]: ").split())
spd = a/b
sph = a/(b*c)
print(f"Salary Per day {spd} Salary per hour {sph}")