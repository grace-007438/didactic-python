import os

FILE_NAME = "bank.txt"

# Load accounts from file
def load_accounts():
    accounts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                accounts[acc_no] = {
                    "name": name,
                    "balance": float(balance)
                }
    return accounts


# Save accounts to file
def save_accounts(accounts):
    with open(FILE_NAME, "w") as file:
        for acc_no, data in accounts.items():
            file.write(f"{acc_no},{data['name']},{data['balance']}\n")


# Create account
def create_account(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account already exists!")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit: "))

    accounts[acc_no] = {
        "name": name,
        "balance": balance
    }
    save_accounts(accounts)
    print("Account created successfully!")


# Deposit money
def deposit(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter deposit amount: "))
    accounts[acc_no]["balance"] += amount
    save_accounts(accounts)
    print("Amount deposited successfully!")


# Withdraw money
def withdraw(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter withdraw amount: "))
    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
        return

    accounts[acc_no]["balance"] -= amount
    save_accounts(accounts)
    print("Amount withdrawn successfully!")


# Check balance
def check_balance(accounts):
    acc_no = input("Enter Account Number: ")
    if acc_no in accounts:
        print("Account Holder:", accounts[acc_no]["name"])
        print("Balance:", accounts[acc_no]["balance"])
    else:
        print("Account not found!")


# Main menu
def main():
    accounts = load_accounts()

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit(accounts)
        elif choice == "3":
            withdraw(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            print("Thank you for using the Bank Management System")
            break
        else:
            print("Invalid choice! Try again.")


main()
