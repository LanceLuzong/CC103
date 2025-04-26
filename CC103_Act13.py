import os

def create_account():
    os.system('cls')
    print("== Create Account ==")
    username = input("Enter username: ")
    password = input("Enter password: ")
    account_type = input("Enter account type (admin/user): ")

    with open("users.txt", "a") as file:
        file.write(f"{username},{password},{account_type}\n")

    print("Account created successfully!")
    input("Press Enter to continue...")

def login():
    os.system('cls')
    print("== Login ==")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        user_info = user.strip().split(",")
        if username == user_info[0] and password == user_info[1]:
            print("Login successful!")
            print(f"Welcome, {user_info[0]} ({user_info[2]})")
            input("Press Enter to continue...")
            return user_info[2]
    
    print("Invalid username or password.")
    input("Press Enter to continue...")
    return None

def menu():
    while True:
        os.system('cls')
        print("== Menu ==")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            account_type = login()
            if account_type == "admin":
                print("Admin menu here...")
            elif account_type == "user":
                print("User menu here...")
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")
            input("Press Enter to continue...")

menu()