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
        index = a.find(b)
        if index != -1:
            a = a[:index] + a[index+1:]
        print("Result:", a)
    case 2:
        index = a.rfind(b)
        if index != -1:
            a = a[:index] + a[index+1:]
        print("Result:", a)
    case 3:
        a = a.replace(b, "")
        print("Result:", a)
    case _:
        print("Invalid choice")