'''
8.
=========================================
ALLOWED CHARACTER VALIDATOR
=========================================

Allowed characters are:
A-Z, a-z, 0-9

Store allowed characters in a Frozen Set.

Menu:
1. Enter Username
2. Validate Username
3. Display Allowed Characters
4. Exit

Requirements:
- Use Frozen Set.
- Username should contain only allowed characters.
-
'''
allowed = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")

username = ""

while True:
    print("\n===== ALLOWED CHARACTER VALIDATOR =====")
    print("1. Enter Username")
    print("2. Validate Username")
    print("3. Display Allowed Characters")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")

    elif choice == "2":
        if username == "":
            print("Please enter username first.")
        else:
            valid = True

            for ch in username:
                if ch not in allowed:
                    valid = False
                    break

            if valid:
                print("Username is valid")
            else:
                print("Username is invalid")

    elif choice == "3":
        print("Allowed Characters:")
        print(allowed)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")