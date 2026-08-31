'''
4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.

'''
subjects = []
n = int(input("Enter number of subjects: "))
for i in range(n):
    subject = input("Enter subject: ")
    subjects.append(subject)
subjects = frozenset(subjects)
while True:
    print("\n===== SUBJECT MANAGEMENT =====")
    print("1. Display Subjects")
    print("2. Search Subject")
    print("3. Count Subjects")
    print("4. Attempt to Add Subject")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Subjects:")
        for subject in subjects:
            print(subject)
    elif choice == "2":
        name = input("Enter subject to search: ")
        if name in subjects:
            print("Subject found")
        else:
            print("Subject not found")
    elif choice == "3":
        print("Total Subjects:", len(subjects))
    elif choice == "4":
            print("Modification is not allowed!")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice")