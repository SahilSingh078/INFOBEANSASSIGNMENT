# from collections import namedtuple
# Account = namedtuple("Account", ["accno", "holdername","balance"])
# accno = int(input("acc no. daal : "))
# name = input("Naam daal: ")
# bal = int(input("KItna h khaate me: "))
# acc = Account(accno,name,bal)
# print(acc.accno)
# print(acc.holdername)
# print(acc.balance)

# from collections import namedtuple
# student = namedtuple("student",["rollno", "name","marks"])
# n = int(input("Enter number of student: "))
# stu = []
# for i in range(n):
#     print("Enter details: ")
#     r = int(input("Enter roll no, : "))
#     name =(input("Enter name : "))
#     m = float(input("Enter marks : "))
#     s = student(r, name, m)
#     stu.append(s)
# print("details: ")
# print(stu)
# for x in stu:
#     print(x.rollno, "->", x.name, "and", x.marks)

from collections import namedtuple
student = namedtuple("student", ["name","rollno","school", "city"])
st = student("sahil","15","gyanasthali vidyalaya","Rewa")
print("Name: ",st.name, "school: ",st.school,"Roll no: ", st.rollno, "City is : ", st.city, end ="\n")