'''
5.
 Student Grade Classification System (Python List Assignment)
A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
by grouping students into grade categories.

Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
```

---

 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5
'''
a =int(input("Enter the marks of students: "))
nums = []
for i in range(a):
	x = int(input("Enter marks: "))
	nums.append(x)
print("Numbers are: ",nums)
x = []
b = []
c = []
fail=[]
for i in nums: 
	if i >=90:
		x.append(i)
	elif i>=75:
		b.append(i)
	elif i>=50:
		c.append(i)
	else:
		fail.append(i)

print("===== STUDENT GRADE REPORT =====")
print()
print("A GRADE STUDENTS    :  ",a)
print("B GRADE STUDENTS    :  ",b)
print("C GRADE STUDENTS    :  ",c)
print("FAIL STUDENTS       :  ",fail)

print("--------------------------------")
print("A COUNT    :  ",len(x))
print("B COUNT    :  ",len(b))
print("C COUNT    :  ",len(c))
print("FAIL COUNT :  ",len(fail))
print("--------------------------------")
print("TOTAL STUDENTS: ", len(nums))

