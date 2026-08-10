'''
67
Count how many times a substring appears. 
S = "abab", 
Sub = "ab" 
2
'''
a = input("Enter the string: ")
sub = input("Enter the substring: ")
for i in a:
    print("Count is: ", a.count(sub))
    break