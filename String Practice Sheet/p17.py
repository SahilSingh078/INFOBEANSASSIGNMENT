'''
17. Remove the first, last, or all occurrences of a given character.
'''
a = input("Enter the string: ")
b = input("Enter the character: ")
print("1. First occurrence")
print("2. Last occurrence")
print("3. All occurrences")
choice = int(input("Enter your choice (1, 2, or 3): "))
match choice:
    case 1:
        ind = a.find(b)
        if ind != -1:
            a = a[:ind] + a[ind+1:]
        print("result:", a)
    case 2:
        ind = a.rfind(b)
        if ind != -1:
            a = a[:ind] + a[ind+1:]
        print("result:", a)
    case 3:
        a = a.replace(b, "")
        print("result:", a)
    case _:
        print("Invalid choice")