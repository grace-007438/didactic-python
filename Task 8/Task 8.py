students = {}

# Add Student
def add_student():
    roll = int(input("Enter Roll Number: "))
    if roll in students:
        print("Student already exists!")
    else:
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))
        students[roll] = {"name": name, "marks": marks}
        print("Student added successfully")

# View Students
def view_students():
    if not students:
        print("No student records found.")
    else:
        print("\nRoll\tName\tMarks")
        for roll, details in students.items():
            print(f"{roll}\t{details['name']}\t{details['marks']}")

# Update Student
def update_student():
    roll = int(input("Enter Roll Number to update: "))
    if roll in students:
        name = input("Enter new Name: ")
        marks = float(input("Enter new Marks: "))
        students[roll]["name"] = name
        students[roll]["marks"] = marks
        print("Student updated successfully")
    else:
        print("Student not found!")

# Delete Student
def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    if roll in students:
        del students[roll]
        print("Student deleted successfully")
    else:
        print("Student not found!")

# Main Menu
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!")
