a = int(input("enter experience: "))
b = int(input("enter rating: "))
c = int(input("enter salary: "))

if a >= 5:
    
    if b >= 4:
        
        if c < 50000:
            bonus = c * 0.20
        else:
            bonus = c * 0.10
            
    else:
        bonus = c * 0.05

else:
    bonus = 0

print("Bonus =", bonus)