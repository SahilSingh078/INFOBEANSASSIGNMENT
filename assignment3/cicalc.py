p, r, t = map(int, input("Enter Principle, Rate, Time(In years) [with space]: ").split())

amount =int( p * (1 + r/100)**t)

ci = amount - p

print(f"Principle: {p}, Rate: {r}, Time: {t} \nAmount = {amount} \nCompound interest: {ci}")