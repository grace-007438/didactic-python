import os

FILE_NAME = "Employee_payroll.txt"

# Load employees from file
def load_employees():
    employees = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                emp_id, name, basic, allowance, tax, net = line.strip().split(",")
                employees[emp_id] = {
                    "name": name,
                    "basic": float(basic),
                    "allowance": float(allowance),
                    "tax": float(tax),
                    "net": float(net)
                }
    return employees


# Save employees to file
def save_employees(employees):
    with open(FILE_NAME, "w") as file:
        for emp_id, data in employees.items():
            file.write(f"{emp_id},{data['name']},{data['basic']},{data['allowance']},{data['tax']},{data['net']}\n")


# Add employee
def add_employee():
    employees = load_employees()

    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowances: "))
    tax = float(input("Enter Tax Percentage: "))

    gross_salary = basic + allowance
    tax_amount = (tax / 100) * gross_salary
    net_salary = gross_salary - tax_amount

    employees[emp_id] = {
        "name": name,
        "basic": basic,
        "allowance": allowance,
        "tax": tax,
        "net": net_salary
    }

    save_employees(employees)
    print("Employee added successfully!")


# Display employees
def display_employees():
    employees = load_employees()
    if not employees:
        print("No employee records found.")
        return

    for emp_id, data in employees.items():
        print("\nEmployee ID:", emp_id)
        print("Name:", data["name"])
        print("Net Salary:", data["net"])


# Main Menu
while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
