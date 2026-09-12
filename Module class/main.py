# normal function
# import module
# print(module.add(10,20))
# print(module.sub(10,20))
# print(module.mul(10,20))


# import all function
# from module import add,sub,mul
# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))


# short name
# import module
# import myvariable as mv
# print(module.add(10,20))
# print(module.sub(10,20))
# print(module.mul(10,20))
# print(mv.pi)
# print(mv.person)


# Based on user input
# import emp
# basic = int(input("Enter your basic: "))
# print(emp.calc_salary(basic))


# import module
# import myvariable
# print(module.add(10,20))
# print(myvariable.add(10,20))

# ❤️‍🔥
# from module import add
# from myvariable import add 
# print(add(10,20))
# print(add(10,20))



# print(mypackage.add(10,20))  error(without importing mathop and stringop

# import mypackage 
# print(mypackage.add(10,20))
# print(mypackage.reverse("sahil"))

# from mypackage import mathop,stringop
# print("addition is: ", mathop.add(10,20))
# print("reverse is: ", stringop.reverse("sahil"))


from mypackage.mathop import add,sub,mul
from mypackage.stringop import reverse,uppercase

print(add(10,29))
print(reverse("Sahil"))
