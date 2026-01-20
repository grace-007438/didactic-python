import os

FILE_NAME = "users.txt"

# Load users from file
def load_users():
    users = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                users[username] = password
    return users


# Register a new user
def register():
    users = load_users()
    username = input("Enter username: ")

    if username in users:
        print("Username already exists")
        return

    password = input("Enter password: ")

    with open(FILE_NAME, "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful")


# Login user
def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful")
    else:
        print("Invalid username or password")


# Main Menu
def main():
    while True:
        print("\n--- Login System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Exiting program")
            break
        else:
            print("Invalid choice")


# Run the program
main()
